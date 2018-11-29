#!python3
import os

from jira import JIRA

jira = JIRA(
    os.environ.get('JIRA_SERVER'),
    basic_auth=(os.environ.get('JIRA_USER'), os.environ.get('JIRA_PASS'))
)

issues = jira.search_issues(
    '(assignee = currentUser() or reporter = currentUser()) AND resolution = unresolved'
)

keys = []
for i in issues:
    keys.append(i.key)
    print("{:10}\t{:20}\t{}".format(i.key, i.fields.status.name, i.fields.summary))

key = input("Which do you want to start: ")

if key in keys:
    issue = jira.issue(key)
    t_ids = []
    transitions = {t['name']: t['id'] for t in jira.transitions(issue)}
    if "In Progress" in transitions and i.fields.status.name == "To Do":
        jira.transition_issue(issue, transitions['In Progress'])
        print("Issue {} changed to In Progress.")
        exit()
