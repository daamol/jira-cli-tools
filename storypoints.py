#!python3
import os
import sys
import asyncio
from jira import JIRA

jira = JIRA(
    os.environ.get('JIRA_SERVER'),
    basic_auth=(os.environ.get('JIRA_USER'), os.environ.get('JIRA_PASS'))
)

if len(sys.argv) == 1:
    print("\n".join(["{:7}\t{:20}".format(p.key, p.name) for p in jira.projects()]))

project_key = sys.argv[1] if len(sys.argv) > 1 else input("What is the project you want to estimate: ")

issues = jira.search_issues(
    'project = {} AND "Story points" is EMPTY AND resolution  = Unresolved'.format(project_key)
)
def add_points(issue, points):
    issue.update(fields={"customfield_10011": points})

loop = asyncio.get_event_loop()
keys = []
for i in issues:
    print("\n\n{:10}\t{:20}\t{}\n{}".format(i.key, i.fields.status.name, i.fields.summary, i.fields.description))
    points = int(input("What is your estimate (points): "))
    loop.run_in_executor(None, add_points, i, points)
