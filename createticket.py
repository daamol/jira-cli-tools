import os

from jira import JIRA
import sys

jira = JIRA(
    os.environ.get('JIRA_SERVER'),
    basic_auth=(os.environ.get('JIRA_USER'), os.environ.get('JIRA_PASS'))
)
if len(sys.argv) == 1:
    print("\n".join(["{:7}\t{:20}".format(p.key, p.name) for p in jira.projects()]))

project_key = sys.argv[1] if len(sys.argv) > 1 else input("Which project do you want to start: ")
summary = sys.argv[2] if len(sys.argv) > 2 else input("Summary: ")
description = sys.argv[3] if len(sys.argv) > 3 else input("Description: ")

issue_dict = {
    'project': {'key': project_key},
    'summary': '{}'.format(summary),
    'description': "{}".format(description),
    'issuetype': {'name': 'Task'},
    }
print(issue_dict)
child = jira.create_issue(fields=issue_dict)

print("created issue: {}/browse/{}".format(os.environ.get('JIRA_SERVER'), child.key))
