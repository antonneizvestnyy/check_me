import com.atlassian.jira.component.ComponentAccessor
def customFieldManager = ComponentAccessor.getCustomFieldManager();
def cf = customFieldManager.getCustomFieldObjects(issue).find {it.name == 'NAME_TYPE_ISSUE'}

if (issue.getCustomFieldValue(cf)){
    switch(issue.getCustomFieldValue(cf).value){
        case ['NAME_VALUE']:
        users = ['NAME_USERS']
        watchUsers(users)
        break;
    }
}

def watchUsers(users) {
def watcherManager = ComponentAccessor.getWatcherManager()
def userManager = ComponentAccessor.getUserUtil()
        for (user in users) {
                def appUser = userManager.getUserByName(user)
                watcherManager.startWatching(appUser, issue)
        }
}
