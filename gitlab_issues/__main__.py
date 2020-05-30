import sys
from pathlib import Path
path_to_extend = f"{Path(__file__).parent.parent.absolute()}"
sys.path.extend([path_to_extend])

from gitlab_issues.custom_objects import CustomIssuesManager
from gitlab_issues.operations import GitlabProjectIssues
from gitlab_issues.utils import get_secret

project_issues = GitlabProjectIssues(get_secret('PROJECT_NAME'))
issues = project_issues.get_all_issues()
CustomIssuesManager(issues).write_issues_to_csv()
