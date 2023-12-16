import com.atlassian.jira.component.ComponentAccessor
import com.atlassian.jira.issue.Issue
import com.atlassian.jira.issue.IssueManager
import com.atlassian.jira.issue.MutableIssue
import com.atlassian.jira.project.Project 

// Добавление компонента 

MutableIssue issue1 = issue
Project project = issue.getProjectObject()
def component = ComponentAccessor.getProjectComponentManager().findByComponentName(project.getId(),"NAME_COMPONENT")
issue1.setComponent([component])
