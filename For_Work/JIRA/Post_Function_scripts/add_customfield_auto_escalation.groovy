import com.atlassian.jira.component.ComponentAccessor
import com.atlassian.jira.issue.CustomFieldManager
import com.atlassian.jira.issue.fields.CustomField


// Изменение поля OPTIONS

def customFieldManager = ComponentAccessor.getCustomFieldManager()
def customField = customFieldManager.getCustomFieldObject("CUSTOM_FIELD_ID")  
def fieldConfig = customField.getRelevantConfig(issue)
def value = ComponentAccessor.optionsManager.getOptions(fieldConfig)?.find { it.value == 'NAME_VALUE' }
issue.setCustomFieldValue(customField, [value])
