import requests,json,os,sys
sys.path.insert(0,os.path.abspath(os.path.join(os.path.dirname(__file__),'..')))
from utils.basic_functions import get_secret

url = f"https://api.notion.com/v1/databases/{get_secret('NOTION_EMAIL_TRENDS_DBID')}/query"

headers = {
    "Authorization": f"Bearer {get_secret('NOTION_TOKEN')}",
    "Content-Type": "application/json",
    "Notion-Version": "2022-06-28"
}

# collect relevant data
response = requests.post(url,headers=headers)
print("update_email_trends.py Status Code: ",response.status_code)

# strip the unnecessary data from the giant pull
data = response.json()
filtered_data = []
for item in data['results']:
    
    # initial data cleaning
    sent_time = item['properties'].get("Send Date",{}).get("date",{}).get("start")
    relation_list = item['properties'].get("Email Trend",{}).get("relation",[])
    
    # get the name related to the relation page
    relation_name = "No Email Trend"
    if relation_list:
        relation_id = relation_list[0].get("id")
        relation_url = f"https://api.notion.com/v1/pages/{relation_id}"
        relation_response = requests.get(relation_url,headers=headers)
        relation_data = relation_response.json()
        relation_name = relation_data['properties']['Name']['title'][0]['text']['content']
    
    # add the record as a dictionary
    filtered_record = {
        'sent_time':sent_time,
        'relation_id':relation_name
    }
    filtered_data.append(filtered_record)

with open('_data/email_trends.json','w') as f:
    json.dump(filtered_data,f,indent=2)

