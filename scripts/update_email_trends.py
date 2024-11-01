import requests,json,os,sys
sys.path.insert(0,os.path.abspath(os.path.join(os.path.dirname(__file__),'..')))
from utils.basic_functions import get_secret

# function for pulling all data through pagination
def fetch_all_pages(url,headers):
    # initialize variables
    all_pages = []
    has_more = True
    next_cursor = None

    while has_more:
        payload = {'page_size':100}
        if next_cursor:
            payload['start_cursor'] = next_cursor
        
        response = requests.post(url,headers=headers,json=payload)
        data = response.json()

        all_pages.extend(data.get('results',[]))
        has_more = data.get('has_more',False)
        next_cursor = data.get('next_cursor')

    return all_pages

# function to process the data collected
def process_pages(data,headers):
    filtered_data = []
    for item in data:
        
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
    
    return filtered_data

def main():
    url = f"https://api.notion.com/v1/databases/{get_secret('NOTION_EMAIL_TRENDS_DBID')}/query"

    headers = {
        "Authorization": f"Bearer {get_secret('NOTION_TOKEN')}",
        "Content-Type": "application/json",
        "Notion-Version": "2022-06-28"
    }

    # collect and process data
    filtered_data = process_pages(fetch_all_pages(url,headers),headers)

    # write the collected data to file
    with open('_data/email_trends.json','w') as f:
        json.dump(filtered_data,f,indent=2)

if __name__=='__main__':
    main()