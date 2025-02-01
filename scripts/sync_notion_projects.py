import os,json,sys
from datetime import datetime
from notion_client import Client
sys.path.insert(0,os.path.abspath(os.path.join(os.path.dirname(__file__),'..')))
from utils.basic_functions import get_secret

def get_notion_client():
    """Initialize and return Notion client."""
    token = get_secret('NOTION_TOKEN')
    if not token:
        raise ValueError("NOTION_TOKEN environment variable is required")
    return Client(auth=token)

def get_database_id():
    """Get the Notion database ID from environment variables."""
    database_id = get_secret('NOTION_PROJECT_DBID')
    if not database_id:
        raise ValueError("NOTION_PROJECTS_DBID environment variable is required")
    return database_id

def query_notion_database(notion, database_id):
    """Query the Notion database for all projects."""
    response = notion.databases.query(database_id=database_id)
    return response.get('results', [])

def parse_project(page):
    """Parse a Notion page into a project dictionary."""
    properties = page.get('properties', {})
    
    # Get the title and description
    title = properties.get('Name', {}).get('title', [{}])[0].get('plain_text', '')
    description = properties.get('Description', {}).get('rich_text', [{}])[0].get('plain_text', '')
    
    # Get technologies as a list
    technologies = [
        tag.get('name', '') 
        for tag in properties.get('Technologies', {}).get('multi_select', [])
    ]
    
    # Get URLs
    supporting_url = properties.get('Supporting URL', {}).get('url', '')
    live_url = properties.get('Live Demo URL', {}).get('url', '')
    
    # Create project dictionary
    project = {
        "id": page.get('id'),
        "title": title,
        "description": description,
        "technologies": technologies,
        "github_url": "",  # Keep empty for now as it's not used
        "supporting_url": supporting_url,  # Add supporting_url as its own field
        "live_url": live_url,
        "featured": properties.get('Featured', {}).get('checkbox', False),
        "last_updated": page.get('last_edited_time'),
        "source": "notion"
    }
    
    return project

def save_projects(projects):
    """Save projects to the _data directory."""
    output_path = os.path.join('_data', 'projects.json')
    with open(output_path, 'w', encoding='utf-8') as f:
        json.dump(projects, f, indent=4, ensure_ascii=False)
    print(f"Saved {len(projects)} projects to {output_path}")

def main():
    """Main function to sync Notion projects."""
    try:
        notion = get_notion_client()
        database_id = get_database_id()
        
        print("Querying Notion database...")
        pages = query_notion_database(notion, database_id)
        
        print(f"Found {len(pages)} projects")
        projects = [parse_project(page) for page in pages]
        
        save_projects(projects)
        print("Sync completed successfully")
        
    except Exception as e:
        print(f"Error syncing projects: {str(e)}")
        raise

if __name__ == "__main__":
    main()
