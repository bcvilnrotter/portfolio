import os
import sys
import json
from datetime import datetime, timezone

# Add the project root directory to Python path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from utils.basic_functions import get_secret

# Set Kaggle credentials before importing the API
os.environ['KAGGLE_USERNAME'] = 'brianvilnrotter'
os.environ['KAGGLE_KEY'] = get_secret('KAGGLE_API')

from kaggle.api.kaggle_api_extended import KaggleApi

def setup_kaggle_api():
    """Initialize and authenticate Kaggle API."""
    api = KaggleApi()
    api.authenticate()
    return api

def get_kaggle_notebooks(api):
    """Fetch Kaggle notebooks."""
    notebooks = api.kernels_list(user='brianvilnrotter')
    return notebooks

def get_kaggle_competitions(api):
    """Fetch Kaggle competitions."""
    # Get all competitions and filter for ones where the user has submissions
    competitions = api.competitions_list()
    # TODO: Filter for competitions with submissions once we figure out the API
    return []

def transform_notebook_to_project(notebook):
    """Transform a Kaggle notebook into project format."""
    # Get notebook metadata
    title = notebook.title
    language = notebook.languageNullable or 'Python'
    kernel_type = notebook.kernelTypeNullable or 'Notebook'
    
    # Get the creation date from the notebook metadata
    # Kaggle API returns dates in UTC
    try:
        last_updated = notebook.lastRunTime or notebook.createdTime
        # Convert datetime to UTC ISO format string
        if isinstance(last_updated, datetime):
            if last_updated.tzinfo is None:
                last_updated = last_updated.replace(tzinfo=timezone.utc)
            last_updated = last_updated.isoformat()
    except AttributeError:
        last_updated = datetime.now(timezone.utc).isoformat()
    
    # Extract topic from title
    topics = []
    if any(term in title.lower() for term in ["machine learning", "ml", "ai"]):
        topics.append("Machine Learning")
    if any(term in title.lower() for term in ["cyber", "security"]):
        topics.append("Cybersecurity")
    if "mars" in title.lower():
        topics.append("Space Science")
    if any(term in title.lower() for term in ["r practice", "dplyr"]):
        topics.append("R")
    if "python" in title.lower():
        topics.append("Python")
    if "regression" in title.lower():
        topics.append("Statistical Analysis")
    if "forecasting" in title.lower():
        topics.append("Time Series Analysis")
    if any(term in title.lower() for term in ["anxiety", "panic"]):
        topics.append("Healthcare Analytics")
    
    # Default topics if none found
    if not topics:
        topics = ["Data Science"]
    
    return {
        "id": f"kaggle-notebook-{notebook.ref}",
        "title": title,
        "description": f"A data science project exploring {', '.join(topics).lower()} using {language}.",
        "technologies": [language] + topics + ["Kaggle"],
        "github_url": "",
        "live_url": f"https://www.kaggle.com/{notebook.ref}",
        "source": "kaggle",
        "featured": True,
        "last_updated": last_updated
    }

def transform_competition_to_project(competition):
    """Transform a Kaggle competition into project format."""
    # Print competition attributes for debugging
    print("Competition attributes:", dir(competition))
    
    return {
        "id": f"kaggle-competition-{competition.ref}",
        "title": getattr(competition, 'title', 'Untitled Competition'),
        "description": "A machine learning competition project focused on developing predictive models.",
        "technologies": ["Python", "Machine Learning", "Kaggle", "Competition"],
        "github_url": "",
        "live_url": f"https://www.kaggle.com/c/{competition.ref}",
        "source": "kaggle",
        "featured": True,
        "last_updated": datetime.now(timezone.utc).isoformat()
    }

def load_existing_projects():
    """Load existing projects from _data/projects.json."""
    try:
        with open('_data/projects.json', 'r', encoding='utf-8') as f:
            return json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        return []

def merge_and_sort_projects(notion_projects, kaggle_projects):
    """Merge Notion and Kaggle projects, sort by last_updated."""
    # Create a dictionary to track unique projects by ID
    unique_projects = {}
    
    # Add Notion projects
    for project in notion_projects:
        if 'source' not in project:
            project['source'] = 'notion'
        unique_projects[project['id']] = project
    
    # Add Kaggle projects (will overwrite any duplicates)
    for project in kaggle_projects:
        unique_projects[project['id']] = project
    
    # Convert back to list and sort by last_updated
    all_projects = list(unique_projects.values())
    
    # Parse ISO dates for sorting
    def get_date(project):
        date_str = project.get('last_updated', '')
        try:
            # Convert to UTC datetime for consistent comparison
            dt = datetime.fromisoformat(date_str.replace('Z', '+00:00'))
            if dt.tzinfo is None:
                dt = dt.replace(tzinfo=timezone.utc)
            return dt
        except (ValueError, AttributeError):
            return datetime.min.replace(tzinfo=timezone.utc)
    
    all_projects.sort(key=get_date, reverse=True)
    
    return all_projects

def save_projects(projects):
    """Save projects to _data/projects.json."""
    output_path = '_data/projects.json'
    with open(output_path, 'w', encoding='utf-8') as f:
        json.dump(projects, f, indent=4, ensure_ascii=False)
    print(f"Saved {len(projects)} projects to {output_path}")

def main():
    """Main function to sync Kaggle projects."""
    try:
        print("Setting up Kaggle API...")
        api = setup_kaggle_api()
        
        print("Fetching Kaggle notebooks...")
        notebooks = get_kaggle_notebooks(api)
        notebook_projects = [transform_notebook_to_project(nb) for nb in notebooks]
        
        print("Fetching Kaggle competitions...")
        competitions = get_kaggle_competitions(api)
        competition_projects = [transform_competition_to_project(comp) for comp in competitions]
        
        print("Loading existing projects...")
        notion_projects = load_existing_projects()
        
        print("Merging and sorting projects...")
        kaggle_projects = notebook_projects + competition_projects
        all_projects = merge_and_sort_projects(notion_projects, kaggle_projects)
        
        print("Saving combined projects...")
        save_projects(all_projects)
        
        print("Kaggle sync completed successfully")
        
    except Exception as e:
        print(f"Error syncing Kaggle projects: {str(e)}")
        raise

if __name__ == "__main__":
    main()
