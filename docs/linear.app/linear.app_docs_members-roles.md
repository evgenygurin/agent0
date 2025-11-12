# Members and roles

Linear offers several role types to help you manage access and permissions across your workspace. Each role is designed to provide the appropriate level of access for different team members, from full administrative control to limited guest access.

## Overview

Admins can manage members and assign roles through the Members page in Settings, accessible at [Settings > Administration > Members](https://linear.app/settings/members). This page shows a list of current and suspended members, and allows you to filter based on roles and status (Pending invites, Suspended, or members who have left the workspace).

> [!NOTE]
> On Enterprise plans with [SCIM](https://linear.app/docs/scim) enabled, some or all member management will be accomplished through your IdP instead of the Members settings page.

## Role types

### Admin

The admin role provides elevated permissions to manage routine workspace tasks. This role is ideal for team leads and managers who need to handle day-to-day administrative work.

On free plans, all members of the workspace have Admin privileges. Once a workspace upgrades to a paid plan, the member who upgrades the workspace to a paid subscription is granted the Admin role.

### Member

Members can work with all workspace-wide features and collaborate across teams they have access to. They do not have administrative capabilities and thus, cannot modify workspace-level settings or access administration pages.

### Guest

> [!NOTE]
> Guest accounts are only available on Business and Enterprise plans.

Guest accounts provide limited access to specific teams within your workspace. This role is ideal for external contractors, clients, or partners who need to collaborate on specific projects without seeing your entire workspace.

They can only access issues, projects, and related documents in the teams they’ve been invited to join.  They can take the same actions as members on data they can access, but cannot see any workspace-wide features like workspace views, customer requests or initiatives. In settings, Guests can only view the Account section managing personal details and preferences.

**Sharing projects with guests**

When a project is shared between multiple teams, guests can only see issues in the project that belong to their assigned teams. For example, if a guest belongs to Team A and Project 1 is shared between Teams A and B, the guest can see the project itself but only issues associated with Team A.

**Integration security**

Integrations enabled for the workspace will be accessible to guest users, which could potentially allow them to access Linear data from teams outside those they're invited to join. To prevent data leakage:

* For Linear-built integrations (GitHub, GitLab, Figma, Sentry, Intercom, Zapier, Airbyte): Ensure guest users don't have access to your accounts on those services
* For integrations requiring email authentication (Slack, Discord, Front, Zendesk): These should automatically limit access to only issues and data in invited teams
* For third-party integrations: review access individually or contact the integration provider in the [Integrations directory](https://linear.app/integrations).

## Managing User Roles

### Changing Roles

To manage roles, navigate to the Members page at **Settings > Administration > Members** and click the overflow menu (three dots) next to the member's name that appears when hovering over that row.

### Viewing Workspace Admins

Members who need to see a list of workspace admins for assistance can:

* Open Command menu `Cmd/Ctrl` `K` and select **View workspace admins**
* Navigate directly to [linear.app/settings/view-admins](https://linear.app/settings/view-admins)

### Suspending Members

Admins can suspend a member from the workspace:

1. Go to [Settings > Administration > Members](https://linear.app/settings/members)
2. Click on the three dot menu next to the member's name
3. Select **Suspend user...**

Suspended users are removed from the workspace and cannot access it unless unsuspended. They will be removed from your next bill, as detailed in our [Billing documentation](https://linear.app/docs/billing-and-plans#billing).

Suspended users remain visible in the member list for historical reasons (they appear in issues where they were mentioned or involved), but you can filter the list to hide them.

To view issues created by or assigned to suspended users, navigate to their profile at `linear.app/workspace-name/profiles/username`. Admins can find this link by clicking on the user's photo or filtering for "Suspended" members in the Members page.