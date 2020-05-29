import gitlab
import os
import pandas as pd
from dotenv import load_dotenv

load_dotenv()

# private token or personal token authentication
URL = 'https://gitlab.com/'
USER_ID = os.getenv('GITLAB_USER_ID')
PROJECT_NAME = os.getenv('PROJECT_NAME')
private_token = os.getenv('GITLAB_API_TOKEN')

project_namespace = f'{USER_ID}/{PROJECT_NAME}'

gl = gitlab.Gitlab(URL, private_token=private_token)
project = gl.projects.get(project_namespace)
issues = project.issues.list()
issue_attribs = [issue.attributes for issue in issues]
df = pd.DataFrame(issue_attribs)

df.to_csv('project_issues.csv')
