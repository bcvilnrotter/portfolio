# %%
import os
import requests

# %%
current_repo_name = os.getenv('GITHUB_REPOSITORY','bcvilnrotter/portfolio').split('/')[1]
current_repo_name
# %%
# Fetch repositories from GitHub API
response = requests.get("https://api.github.com/users/bcvilnrotter/repos")
# %%
repos = response.json()
# %%

# Start creating an HTML file with repo details
html_content = "<html><body><h1>Github Repositories</h1></body>"
for repo in repos:
    if not repo.get("fork") and repo['name'] != current_repo_name:
        html_content += f"""
            <div>
                <h3><a href="{repo['html_url']}" target="_blank">{repo['name']}</a></h3>
                <p>{repo['description']}</p>
            </div>
        """
html_content += "</div></body></html>"

# Write the HTML content to a file
with open("repos.html","w") as file:
    file.write(html_content)

# Print the success command to console
print("HTML file generated successfully!")