import requests,json,os,sys
sys.path.insert(0,os.path.abspath(os.path.join(os.path.dirname(__file__),'..')))
from utils.basic_functions import get_secrets

url = f"https://api.notion.com/v1/databases/{get_secrets('NOTION_EMAIL_TRENDS_DBID')}"

headers = {
    "Authorization": f"Bearer {get_secrets('NOTION_TOKEN')}",
    "Content-Type": "application/json",
    "Notion-Version": "2022-06-28"
}

response = requests.get(url,headers=headers)
print("update_email_trends.py Status Code: ",response.status_code)
data = response.json()

with open('_data/email_trends.json','w') as f:
    json.dump(data,f,indent=2)

