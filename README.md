# jira-cli-tools

## install
install python3

install python-jira
pip3 install jira

Add the folowing to your profile
```bash
export JIRA_PASS="PASS"
export JIRA_USER="USERNAME"
export JIRA_SERVER="https://yourcompany.atlassian.net"
alias jira-create-ticket='python3 $HOME/projects/jira-cli-tools/createticket.py'
alias jira-list-open='python3 $HOME/projects/jira-cli-tools/listmyinprogress.py'
alias jira-start-ticket='python3 $HOME/projects/jira-cli-tools/startprogress.py'
alias jira-storypoints='python3 $HOME/projects/jira-cli-tools/storypoints.py'

```