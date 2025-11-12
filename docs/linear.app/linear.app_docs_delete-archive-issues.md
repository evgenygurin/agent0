# Delete and archive issues

Linear archives issues automatically to keep your workspace uncluttered and easy to search.

![Linear settings showing the auto-archive preferences](https://webassets.linear.app/images/ornj730p/production/82132ce2f13a09b1638db646a8dc460416fe89c8-2160x1327.png?q=95&auto=format&dpr=2)

## Overview

Linear offers features that helps to manage backlog and stale items in your workspace to streamline your focus on what's current. We introduce our auto-close and auto-archive feature, and talk about deleted issues and the team archives.

## Delete issues

Delete issues with the shortcut `Cmd/Ctrl` `delete`, from an issue's contextual menu, or use command bar `Cmd` `K` and select **Delete issue**.

If you accidentally delete an issue, the fastest way to restore it is to use `Cmd/Ctrl` `Z`. If that isn't an option (e.g. it wasn't the last action you took), go to your team's archives > _Recently deleted issues_ and use the `#` shortcut to restore it. Recently deleted issues are stored in the archives for 30 days, after which they'll be permanently removed from your workspace. It is not possible to restore deleted issues after they have been permanently removed.

## Auto-close

![Auto-close automations settings](https://webassets.linear.app/images/ornj730p/production/e3ab2a2dcae1e075aa611591cc07d4281723f239-1342x810.png?q=95&auto=format&dpr=2)

Linear offers an option to close issues that have not been updated after a certain time period. This can be configured in _Team settings > Workflows_. When auto-closed, an issue is marked with one of the Closed statuses, we publish a history item to its Activity feed, and notify subscribers. You can re-open an auto-closed issue anytime by changing its status.  
  
Issues will not be auto-closed until the associated cycle and project are completed.

## Auto-archive

Archiving happens automatically with no user action required - there is no way to manually archive issues.

![auto-archive issues closed for selection in settings](https://webassets.linear.app/images/ornj730p/production/a6b1715ab09502f90afe419afa83a926a1cb379d-1414x426.png?q=95&auto=format&dpr=2)

You can adjust the auto-archive time period, after which closed issues are auto-archived in _Team Settings > Workflow_. Changes made will apply within 24 hours, so if you have issues that have been completed for 2 months and change to a 1 month auto-archive schedule, you can expect to see those archive within the next day.

Projects and cycles cannot archive before their issues are archived. Once all issues are archived these entities are archived immediately afterwards. 

### Issues are not archiving

There are some scenarios in which issues will not archive:

* Issues will not be archived if the associated cycle is not completed
* Issues will not archive if the associated project is not marked as Completed or Cancelled
* Sub-issues will not archive if the parent issue is not Completed or Cancelled

> [!NOTE]
> If a completed issue is blocked from auto-archiving for one of the above reasons, it will still need to wait the necessary auto-archive period when separated from the project, cycle or sub-issue in question.   
>   
> For example, with a 1 month auto-archive period in place, an issue that's been done for 3 months in an active project will archive 1 month after the project has been completed.

## The archives

![overflow menu on a team showing open archive](https://webassets.linear.app/images/ornj730p/production/e20628c04092db1245ec3354523e019d11e3a6f8-820x454.png?q=95&auto=format&dpr=2)

Each team has its own archives page where you will find archived or deleted issues, initiatives, cycles, projects, and documents. Access it with the shortcut `G` then `X` or find it in the sidebar under the three dot menu beside each team name. To keep the app speedy, archived issues are loaded on demand rather than stored in the client, so you may find the issues load a little slower on this page than elsewhere in the app.

### Restore issues

Restore issues, projects, or initiatives from the archive in order to edit them.