# Teams

Create teams in your workspace to organize different types of work functions.

> [!NOTE]
> Different plans support different numbers of teams: details available [below](https://linear.app/docs/teams#team-limits).

![linear app showing teams page](https://webassets.linear.app/images/ornj730p/production/2aa78477eeb62feb13b2bc41395ee5c69464a763-1771x948.png?q=95&auto=format&dpr=2)

## Overview

A workspace is composed of one or many teams. Teams typically represent groups of people who work together frequently, though in some cases you may choose to structure teams as parts of a product. Teams contain issues, and can have team-specific projects (though projects can also be shared between teams).

 By default, when you create a workspace we'll generate a team for you with the same name. It's up to you how to split up teams and users can be part of one or many teams. 

Consider grouping teams by:

* Teammates who work together frequently.
* Areas of work such as marketing, mobile app, etc.
* Keeping everyone on one team is the simplest approach (best for small teams).

> [!NOTE]
> If you aren't sure how to split up your teams, start with one or two. It's easy to add more teams in the future, copy settings from existing teams, and move issues from one team to another.

## Your teams

Teams you have joined will appear in your sidebar. 

Each team has the following pages to organize your work:

* [Triage](https://linear.app/docs/triage)* Newly created issues to be reviewed, assigned or prioritized before entering the team's workflow
* [Issues](https://linear.app/docs/default-views)  Default views of all issues in this team
* [Cycles](https://linear.app/docs/use-cycles)* Review current, past and upcoming cycles to plan and schedule your team's workload
* [Projects](https://linear.app/docs/projects#view-your-projects) Default views of all projects linked to this team, along with custom views of projects that you can add and edit.
* [Views](https://linear.app/docs/custom-views#overview) Custom views filtered to this team's issue, visible to members of the team

> [!NOTE]
> Sections marked with an * are opt-in and need to be enabled in team settings.

### Team settings

Team settings allow you to configure each team differently to support different workflows. 

To access your team's settings:

* From the app sidebar, hover over the team name, click the three dots `···` menu, and select "Team settings." 
* From Settings, find the team you want to update from Your teams and select it. It'll take you to the team's unique settings page.

From the team's settings page, you can update the name, icon, and identifier for the team. Changing the issue identifier is a safe action to take -- old URLs containing the original identifier will automatically redirect to the new issue URL. 

You can also configure the following settings:

Team settings page | Configure
--- | ---
General | Set timezone. estimates, create issues by email
Members | Manage team members
Issue labels | Manage team-level labels and label groups
Templates | Manage team-level issue, project, and document templates
Recurring issues | View all existing and create new recurring issues
Slack notifications | Set team-level notifications to Slack
Issue statuses & automations | Customize workflows, add and edit statuses, set up git automations and branch naming preferences, enable auto-close and auto-archive
Triage | Enable Triage, assign Triage responsibility (compatible with PagerDuty and incident.io)
Cycles | Enable and configure cycles, set cycle automations

## Working with other teams

### View other teams

Teams you navigate that you are not a member of will show up in your sidebar under a temporary _Exploring_ section. 

You can search for and view issues, projects, and documents from other teams, too, as long as those teams are not private.

### Access control

All members of a workspace can view and join teams as long as the team is not private. 

Anyone in the workspace can create issues for other teams or be assigned issues in other teams, too. You don't have to join teams to collaborate with others unless you use them frequently and want them to show up in your sidebar. 

## Create teams

To join other teams or create a new one, navigate to settings and select "Join or create a team" from the bottom of the settings sidebar.

* In [Settings](https://linear.app/settings) below the list of your existing Teams, click the + "Add team"
* From command bar `Cmd/Ctrl` + `K`, select "Create new team"
* Admins can create teams from their [Teams page](https://linear.app/settings/teams) in settings

### Team limits

The number of teams that can be created is dependent on a workspace's subscription:

Plan | Team limit
--- | ---
Free | 2
Basic | 5
Business | Unlimited
Enterprise | Unlimited

### Team creation settings

**Private teams:** During team creation, you'll have the option to copy over settings from an existing team and make the team [private](https://linear.app/docs/private-teams).

**Copy team settings**: If you want to copy an existing team's settings when creating a team, use the "Copy team settings..." option when creating a new team.

**Restrict team creation**: Admins can restrict team creation to only admin users under [Settings > Administration > Security](https://linear.app/settings/security).

### Tips on structuring teams

Keep these tips in mind when deciding how to structure your workspace's teams:

* **Issues are tied to teams**. Think about how you prefer to manage your work and interact with features such as the backlog and archive.
* **Workflows can be customized per team.** Different work areas or internal teams (e.g. engineering, design, marketing, sales) may require different statuses.
* **Cycles are team-specific**. You can set up cycles so that all teams follow the same schedule, but you can't view more than one team's cycles at once. Think about how you manage your work, run meetings, measure progress, and whose work you'll want to oversee as a manager.
* **Projects** can belong to a single team or be shared across many teams (but issues can only be tied to one team)
* **Sub-issues** can be assigned to any team or member in the workspace, not just the parent issue's team.
* **Other features** are team-specific but also easy to copy over to another team, such as pull request automation and issue templates. Labels are team-specific but you can create views that show issues from multiple teams as long as the label has the same name across them.

## Manage teams

### Make a team private

Business and Enterprise support [private teams](https://linear.app/docs/private-teams). To make an existing team private, go to _Settings > Your teams > Team_ and then scroll down to the Danger Zone.

### Join / leave / invite teams

Admins can add users to a team in [**Settings > Administration > Members**](https://linear.app/settings/members). 

Members can join and leave teams on their own, by hovering over the team name, then clicking the `···` and selecting to **Join team** or **Leave team...** To join a private team, members must be invited by the team owner. 

### Sub-teams

On Business and Enterprise plans, you can organize teams in a hierarchy (for instance, Mobile might be the parent team of iOS and Android). Learn more about sub-teams [here](https://linear.app/docs/sub-teams).

### Delete a team

Deleting the team will also permanently delete its issues. Once the grace period ends, this can't be undone and your data cannot be recovered by Linear. 

You will have **30 day grace period** to restore the team under _Recently deleted teams_. Access this by opening Settings > Teams and selecting the _Recently deleted_ option in the menu. Restore a team through its overflow menu on the far right of its row.

![Recently deleted teams under Settings > Teams](https://webassets.linear.app/images/ornj730p/production/a62173417d0271899459246defc61f4adda4d536-1526x748.png?q=95&auto=format&dpr=2)

If you may need the data in the future, consider making the team private, exporting the team's issues as a CSV before deleting, or moving the issues to a different team. 

###