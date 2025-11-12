# Initiatives

Use initiatives to group projects by company objective to align on your organization's goals and track progress towards achieving them. 

![Initiatives on a Linear workspace called RideShare](https://webassets.linear.app/images/ornj730p/production/6da64501f5bd32cedef0dbf9b1faf9b09f676e58-3024x1730.png?q=95&auto=format&dpr=2)

## Overview

An Initiative is a manually curated list of projects with an accompanying document. All Initiatives are shown within a single Initiatives view at the workspace level. Their purpose is to express the goals and objectives an organization aims to achieve and to monitor progress towards those aims. This enables high-level planning across multiple projects and long timelines.

Leadership can use the top-level Initiatives view to see a quick overview of ongoing goals, objectives, and their progress. This allows them to assess overall progress without needing to drill down into each individual project.

## Basics

### Create and view initiatives

Navigate to the Initiatives page in your sidebar to create and view existing Initiatives. This page contains all active Initiatives in your workspace. Each Initiative name appears with a short summary, Initiative owner, associated teams, number of projects within, target date, and health status. You can also create a new Initiative from here.

To create an Initiative, all you need is a name. You are automatically assigned as the Initiative owner, but can change ownership later if needed. Initiatives will be visible by all members of your workspace except for guests. 

There is no concept of a “private” Initiative—Initiatives are always shared workspace-wide. If a project belonging to a private team is added to an initiative, the project remains visible only to those in the private team but the Initiative is viewable by others.

### Initiative Health and Active Projects

When viewing Initiatives, use the Initiative Health and Active projects columns to quickly assess how work is progressing. 

![Initiative health and active projects displayed](https://webassets.linear.app/images/ornj730p/production/bd52bb969d596bccc676f6f49c388ea80beb55ce-954x480.png?q=95&auto=format&dpr=2)

**Initiative Health** shows whether the latest initiative update indicated work was on track, at risk, or off track. Click on it to read the full update.

**Active Projects** rolls up data for individual projects in the initiative based on each project's latest project update. These are color coded, and clicking on them shows the associated updates:

* **Green**: On track
* **Yellow**: At risk
* **Red**: Off track
* **Gray**: No recent update 

For projects marked as at risk or off track, consider commenting and to check in and offer assistance. For projects without a recent update, you can mention the project lead to check for any missed updates or potential blockers. Read more about Project and Initiative Updates [here](https://linear.app/docs/initiative-and-project-updates).

### Lifecycle management

Designating Initiatives as planned, active or complete clearly signals the Initiative's current state. When an Initiative is completed, it will move to the completed section to maintain a historical record of work. To change the status of an Initiative, click on the Initiative and update its status from the Initiatives overview page.

### Initiatives overview page

Use the Overview page to share detailed information about the overall Initiative and the projects within it. From this page, you can access and modify the following Initiative properties:

  * **Status:** Indicates if an Initiative is Planned, Active, or Completed.
  * **Owner:** Initially set to the creator of the Initiative but can be reassigned to another workspace member.
  * **Target Date:** The expected completion date of the Initiative.
  * **Resources:** Relevant documents or links associated with the Initiative.
  * **Latest update:** The most recent Initiative update.
  * **Descriptions:** Detailed information about the Initiative.
  * **Project List:** Each project included in the Initiative.



## Sub-initiatives 

Use sub-initiatives to organize your company goals, workstreams, or OKRs into a structured hierarchy. This feature allows Initiatives to be nested inside one another, enabling deeper planning and visibility across large programs of work.

> [!NOTE]
> **Available to workspaces on our Enterprise plan.**
> Available to workspaces on our [Enterprise](https://linear.app/pricing) plan.

![Sub-initiatives](https://webassets.linear.app/images/ornj730p/production/751d06e6c76d6b75b21fcd71da3cf91770d27a8b-2368x1780.png?q=95&auto=format&dpr=2)

### How sub-initiatives work

Sub-initiatives let you nest Initiatives up to five levels deep in a tree-like structure. A parent Initiative automatically includes all the projects it owns directly, as well as all the projects from its sub-initiatives. This makes it easy to roll up work from multiple departments, teams, or quarters into one overarching goal.  


You can use sub-initiatives to:

* Structure company-wide objectives across multiple departments
* Break down a large strategic goal into phased delivery Initiatives
* Group Initiatives by quarter, theme, or ownership

Each Initiative can only have one parent. Projects added to any sub-initiative will automatically be included in the parent’s view of progress.

### Creating and managing sub-initiatives

You can create and organize sub-initiatives from two places in Linear:

**From the workspace Initiative views (Active, Planned, Completed)**

* Create a new Initiative using the `+ New` Initiative button or the keyboard shortcut `N` then `I`. You can also choose a parent Initiative during creation.
* Nest Initiatives by holding `Option` (`Alt` on Windows) while dragging one beneath another.
* To remove a parent, drag the Initiative out of the nested section and drop it elsewhere in the list to return it to the top level.
* These pages are best for managing structure across multiple teams or quarters.

**From an Initiative Overview page**

* Use the `+ Add` button in the top right, or the ... menu beside the Initiative title, to create or attach sub-initiatives.
* Use the `+` icon above the sub-initiative list (if shown) to add more.
* Use the command menu (`Cmd` + `K`) or shortcut `Cmd` + `Shift` + `P` to set or change the parent.

Sub-initiatives created from an Overview page are nested under that Initiative automatically.

### Viewing sub-initiatives

Sub-initiatives appear nested beneath their parent Initiative both on the full workspace Initiative views (_Active_, _Planned_, or _Completed_) and on the parent’s Initiative Overview page. If you’d like to temporarily collapse or expand a nested list, press `T` — this affects only your own view.  


By default, a parent Initiative’s project list includes all projects from its sub-initiatives. You can adjust this using the display settings in the top right of the project list to show only directly owned projects. Each sub-initiative displays a project count, which includes all projects from any further sub-initiatives nested within it.



When Initiatives are grouped by owner or other properties, parent Initiatives will still appear above their sub-initiatives to provide context — but they’ll be shown grayed out if they don’t directly match the grouping property.

### Visibility and filtering

Sub-initiatives follow the same visibility rules as standard Initiatives: they’re visible to all workspace members except guests. If a project belongs to a private team, its details remain restricted — but the Initiative itself will still be listed.

  
When viewing a parent Initiative, filters (such as by team, status, or project health) will include projects from all of its sub-initiatives. This gives you a complete picture of progress at every level of the hierarchy.

## Example use cases

* **Engineering managers** might look at a pipeline view to help them manage immediately upcoming staffing needs
* **Product leaders** may want to use and revise a scenario plan across multiple quarters
* **Marketing leaders** might look at a release timeline filtered only on projects that require serious GTM communication
* **Product leaders** may want to see an overview of all larger asks from customers that are currently being prioritized and actively worked on

## Initiatives vs. Project Views

Initiatives are manually curated lists of projects that typically align with organizational goals, allowing leadership to easily track progress towards these goals.

If you want to group and filter projects automatically — but they don’t align with clear organizational goals or need close progress tracking — we recommend using [project views](https://linear.app/docs/projects#attach-project-views-to-workspace-projects-page) instead. You can also use [project labels](https://linear.app/docs) to help further categorize and organize projects. 

The advantage of project views is that once you set up relevant project filters, all future projects matching these criteria will be automatically included. These views are also visible to all members of your workspace.

For example, you can create a project view to filter all projects with an “In Progress” status, allowing you to see all such projects across your workspace in one place. Another example is creating a view that filters all projects involving your team members, providing a consolidated view of team activities.