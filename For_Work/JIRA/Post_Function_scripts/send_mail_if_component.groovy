import com.atlassian.jira.component.ComponentAccessor
import com.atlassian.jira.issue.MutableIssue

MutableIssue mutableIssue = (MutableIssue) issue

def project = issue.getProjectObject()
def component = ComponentAccessor.getProjectComponentManager().findByComponentName(project.getId(),"<NAME_COMPONENT> ")
components = issue.getComponents()
components.push(component)
mutableIssue.setComponent(components)

comment_text="<TEXT>"
comment = ComponentAccessor.getCommentManager()
comment.create(issue, 'jirman', comment_text, true) 
