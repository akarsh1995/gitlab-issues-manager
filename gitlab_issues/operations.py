from typing import List

from gitlab.v4.objects import Project, ProjectIssueManager

from gitlab_issues.authentication import GitlabAuthenticate
from gitlab_issues.custom_objects import CustomProjectIssue


class GitlabProjectIssues:
    _gla = GitlabAuthenticate()

    def __init__(self, project_name):
        self.project_name = project_name

    def get_all_issues(self) -> List[CustomProjectIssue]:
        return self.issues_wrap(self.issues_manager.list())

    def get_issues_by_id(self, issue_list) -> List[CustomProjectIssue]:
        return self.issues_wrap(self.issues_manager.list(**{'iids[]': issue_list}))

    @staticmethod
    def issues_wrap(issue_list):
        return list(map(CustomProjectIssue, issue_list))

    @property
    def project(self) -> Project:
        return self._user.projects.get(self.project_namespace)

    @property
    def issues_manager(self) -> ProjectIssueManager:
        return self.project.issues

    @property
    def _user(self):
        return self._gla.gl_authenticated

    @property
    def project_namespace(self) -> str:
        return f"{self._gla.USER_ID}/{self.project_name}"

