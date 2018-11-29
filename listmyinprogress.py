import os
from jira import JIRA

jira = JIRA(
    os.environ.get('JIRA_SERVER'),
    basic_auth=(os.environ.get('JIRA_USER'), os.environ.get('JIRA_PASS'))
)

issues = jira.search_issues('assignee = currentUser() AND resolution = unresolved AND status = "In Progress"')

for i in issues:
    print("{}\t{}".format(i.key, i.fields.summary))
