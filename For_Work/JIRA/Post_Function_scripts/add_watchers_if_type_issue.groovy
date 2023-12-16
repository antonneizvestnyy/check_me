// Добавление в вотчером при определенном типе.

import com.atlassian.jira.component.ComponentAccessor

customFieldManager = ComponentAccessor.getCustomFieldManager();
customField = customFieldManager.getCustomFieldObjectByName('<NAME_COMPONENT>');
customFieldValue = issue.getCustomFieldValue(customField);



if (customField.name == 'NAME_COMPONENT'){   // выбрать компонент

        switch (customFieldValue.toString()) {
            case['IF_VALUE']:
                    def userManager = ComponentAccessor.getUserManager()
                    def watcherManager = ComponentAccessor.getWatcherManager()

                    def watcher = ["<USERS>"] // любое кол-во пользователей

                    watcher.each{userName->
                    def user=ComponentAccessor.userManager.getUserByName(userName)
                    watcherManager.startWatching(user, issue)
                    }
            break
      
        }
}
