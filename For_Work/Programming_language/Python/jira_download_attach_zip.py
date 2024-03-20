#собирает по запросу JQL все атачи в зип архиве + список, что хранится в этом архиве
#ссылка - название задачи
#заворачивает все в html , креды не стал добавлять

from my_creds import JIRA_PASSWORD, JIRA_LOGIN
from jira import JIRA

# Ключ проекта для поиска
project = "<PROJECT>"

# Сколько максимально будем получать тикетов
max_tickets = "<MAX_TICKETS>"

# Начальный год для поиска
start_year = "<START_YEAR>"

# Конечный год для поиска
last_year = "<LAST_YEAR>"



url = '<URL>'
jira = JIRA(server=url, basic_auth=(JIRA_LOGIN, JIRA_PASSWORD))
for curr_year in range(start_year,last_year+1,1):
    issues = jira.search_issues('project = '+project+' AND created >= ' + str(curr_year) + '-01-01 AND created <= ' + str(curr_year+1)+ '-01-01',maxResults=max_tickets)
    string4out = "<html>\n"
    string4out += "<p>" + str(curr_year) + " - " + str(curr_year+1) + "</p>"
    counter = 0
    for curr_issue in issues:
        if len(curr_issue.fields.attachment) != 0:
            #print("Curr. issue is "+ curr_issue.key)
            string4out += "<a href=\"<YOUR_DOMAIN>/secure/attachmentzip/"+curr_issue.id+".zip\"" "download=\""+curr_issue.key+".zip\">" + curr_issue.key+ "</a><br />\n"
            for curr_attach in curr_issue.fields.attachment:
                #print("     "+curr_attach.filename)
                string4out +="      " + str(curr_attach.filename) + "<br />"
            counter += 1
        else:
            continue
    string4out += "</html>"

    if counter == 0:
        print("Not found any issues with attachments by "+ str(curr_year) + " - " +str(curr_year+1) + " year")
    else:
        print("Year: " + str(curr_year) + " - " + str(curr_year+1))
        print("Total: "+str(len(issues)))
        print("With attachments: "+ str(counter))
        filename = project+ "-" +str(curr_year) + ".html"
        f = open(filename, "w")
        f.write(string4out)
        f.close()

