from jira import JIRA
import requests
import urllib3

#jira_server = "https://jira-qa.cls.bcs.cnb"
#jira_server = {'server': jira_server, 'verify':False}
#jira = JIRA(options=jira_server, auth=(conf['user'], conf['password']))
options = {'server': "https://chandratech.atlassian.net",}# 'verify': TRUE}

jira = JIRA(options = options , basic_auth = ('surisetty.chandrakiran@gmail.com', 'dCrN8i1Wqefvvp1qU0jJ8CC4'))

#issue = jira.issue('AP-6')
#print('{},{}' .format(issue.fields.project.key,issue.fields.summary))


for singleIssue in jira.search_issues(jql_str='project = AP AND attachments IS EMPTY'):
    print('{}:{}:{}'.format(singleIssue.key, singleIssue.fields.summary,singleIssue.fields.reporter.displayName))

#for attachment in issue.fields.attachment:
#    print("Name: '{filename}', size: {size}".format(
#        filename=attachment.filename, size=attachment.size))
    # to read content use `get` method:
    #print("Content: '{}'".format(attachment.get()))
    
    
#url = 'https://jira-qa.cls.bcs.cnb/rest/com.midori.jira.plugin.pdfview/1.0/pdf/pdf-view/18/render?tempMax=1000&context=single_issue_view&jql=key+%3D+'
#response.ContentType = "application/pdf";
#response = requests.get(url, verify=False)
#response = requests.get(url, auth=(userid, passwd), verify=False)
#response.ContentType = "application/pdf";
