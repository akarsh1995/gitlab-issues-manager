# Gitlab Project Issues export to CSV

### Quickstart


- Run the below command in shell in the project root.

```shell script
cp sample.env .env
```

- Open `.env` file and substitute the mentioned config variables with your configuration
- It is recommended to have pipenv as a package manager.
    - If pipenv  is your package manager then run
        ```shell script
        pipenv install
        pipenv run python gitlab_issues
        ```
    - If pip is your package manager run
        ```shell script
        pip install -r requirements.txt
        python gitlab_issues
        ```
- Check the exported `project_issues.csv` file in the `data` dir.
