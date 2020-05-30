import gitlab
from lab_issues.utils import get_secret


class GitlabAuthenticate:
    _url: str = 'https://gitlab.com/'
    _PRIVATE_TOKEN = get_secret('GITLAB_API_TOKEN')
    USER_ID = get_secret('GITLAB_USER_ID')

    def __init__(self):
        self.gl_authenticated = gitlab.Gitlab(
            url=self._url,
            private_token=self._PRIVATE_TOKEN
        )
