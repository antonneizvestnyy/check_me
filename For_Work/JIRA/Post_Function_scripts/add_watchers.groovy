import com.atlassian.jira.component.ComponentAccessor

def userManager = ComponentAccessor.getUserManager()
def watcherManager = ComponentAccessor.getWatcherManager()

def watcher = ["USERS"]

watcher.each{userName->
def user=ComponentAccessor.userManager.getUserByName(userName)
watcherManager.startWatching(user, issue)
}
