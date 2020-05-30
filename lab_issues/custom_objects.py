from typing import Any, List

from gitlab.v4.objects import ProjectIssue
import pandas as pd
from pathlib import Path


class CustomAuthor:
    id: int
    name: str
    username: str
    state: str
    avatar_url: str
    web_url: str

    def __init__(self, author_dict):
        for key, value in author_dict.items():
            self.__setattr__(key, value)

    def __str__(self):
        return self.name

    def __repr__(self):
        return f"Author: {self.name}"


class CustomProjectIssue:
    _links: dict
    assignee: Any
    assignees: list
    author: CustomAuthor
    closed_at: Any
    closed_by: Any
    confidential: bool
    created_at: str
    description: str
    discussion_locked: Any
    downvotes: int
    due_date: Any
    has_tasks: bool
    id: int
    iid: int
    labels: list
    merge_requests_count: int
    milestone: Any
    moved_to_id: Any
    project_id: int
    references: dict
    state: str
    task_completion_status: dict
    time_stats: dict
    title: str
    updated_at: str
    upvotes: int
    user_notes_count: int
    web_url: str

    def __init__(self, issue: ProjectIssue):
        self._issue = issue
        for attrib, value in self.issue_attribs.items():
            if attrib == 'author':
                value = CustomAuthor(value)
            self.__setattr__(attrib, value)

    @property
    def issue_attribs(self) -> dict:
        return self._issue.attributes

    def __str__(self):
        return f'Issue#{self.iid}'

    def __repr__(self):
        return f'Issue(id={self.id}, author={self.author.name})'


class CustomIssuesManager:
    _default_attribs = ['author', 'created_at', 'iid', 'title']

    def __init__(self, issues: List[CustomProjectIssue]):
        self._issues = issues

    def write_issues_to_csv(self, desired_attribs: list = None):
        if not desired_attribs:
            desired_attribs = self._default_attribs
        pd.DataFrame(self.get_csv_dict(desired_attribs)).to_csv(self.get_save_dir())

    def get_csv_dict(self, attribs_needed):
        return [{attrib: getattr(issue, attrib) for attrib in attribs_needed} for issue in self._issues]

    @staticmethod
    def get_save_dir():
        write_dir = Path('data')
        write_dir.mkdir(parents=True, exist_ok=True)
        file_path = write_dir.joinpath('output_issues.csv')
        return file_path
