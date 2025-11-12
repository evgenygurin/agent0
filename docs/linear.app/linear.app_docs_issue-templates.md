# Issue templates

Templates speed up issue creation, ensure properties are applied when necessary, and facilitate reporting.

![Linear interface showing the option to select a template during issue creation](https://webassets.linear.app/images/ornj730p/production/dcfe3f8b4e4a4ba005dd5c046bf315048d2f8dab-1930x936.png?q=95&auto=format&dpr=2)

## Overview

Templates help you file issues more quickly, and ensure desired issue properties are applied without having to add each one manually. When a template is set as default for a team, each new issue in that team will be created from that template unless manually changed.

## Create an issue template

![The settings page for Templates showing a button on how to create a template](https://webassets.linear.app/images/ornj730p/production/7a91829a12a45a33528236cb58a98221b2737795-2414x817.png?q=95&auto=format&dpr=2)

Create new templates by navigating to either [_Workspace settings > Templates_](https://linear.app/settings/templates) or _Team settings > Templates_.

### Workspace Templates

You can create issues with a workspace template on any team in your workspace. Team specific properties like team labels or issue statuses cannot be preset in a workspace level template.

Use workspace templates for issue types that are likely to appear across different teams

### Team Templates

When a template is scoped to a particular team, it's available only when creating issues in that team. This template type has full access to team properties like team labels and issue statuses.

Team templates are commonly used in our Asks integration, or for types of issues should always be filed to only one team in your Linear workspace.

## Use issue templates

The fastest way to create an issue by template is to use the keyboard shortcut `Option/Alt` `C`, which brings up a list of available templates. Alternatively, access templates directly from the issue creation modal by clicking on _Template_ next to the team name.

To apply a template in a sub-issue, from the sub-issue creation modal, click on the square icon in the top right, which will show you a list of possible templates.

If you don't see the template, check that you're creating the issue from the right team. In a sub-issue, it will only show templates that do not already contain sub-issues as an option to apply.

## Default templates

Configure default templates from a team's template settings page. Taking this action will cause each new issue on that team to have the set template applied by default. You can configure defaults differently for members of your team or people who are not part of your team.

![Default templates in Linear settings](https://webassets.linear.app/images/ornj730p/production/d6eebc35f66823df066e862e923953b55def74c7-1520x506.png?q=95&auto=format&dpr=2)

## Placeholder text

If you want to prompt the creator to input information in the issue's description, consider using placeholder text in your template. 

To format text as a placeholder, select text while editing your template and click the `Aa` icon on the formatting bar. This formatting type is only available when creating or editing templates.

Placeholder text is particularly useful when formatting templates designed to be used as Asks, so you can define custom sections to receive more structured issues. Read more about Asks [here](https://linear.app/docs/linear-asks#customize-templates).

![Design request Ask](https://webassets.linear.app/images/ornj730p/production/3bb9a51c3df5ad07e991b8b32390b7bba6cca1dc-1322x1394.png?q=95&auto=format&dpr=2)

## Templates in integrations

Templates created in Linear can also be used in integrations to help save time and keep properties applied consistently where needed. 

Integration | Use-case
--- | ---
Intercom & Zendesk | Support agents can select a template for the type of issue being reported, speeding up filing and prefilling needed properties like status Triage and label Bug 
Slack | When creating issues from a Slack message, select a template from the dropdown menu
Asks | Asks is designed to be primarily template driven; users outside your Linear workspace but in your Slack workspace create issues via template enabled in Asks, so their issues end up with the necessary data in Linear
Zapier | Consider creating issues via template in the Create Issue step for Linear in Zapier for more complex, multi-application workflows
Email | Templates can have unique email addresses; sending an email to that address will create an issue with the properties of the template

Add a template to a supported integration by using the overflow menu on the template (in team or workspace settings, depending on where the template was configured.)

![Overflow menu in template settings where you can add templates to integrations](https://webassets.linear.app/images/ornj730p/production/add2283cdbcd877d98db082807dbee1b656e0b0a-1406x664.png?q=95&auto=format&dpr=2)

## Template based Insights

Issues created by template are filterable by their template, regardless of where they were created. For example, for a template Bug Report, filtering for that template will return issues created with that template in created in Slack with our Slack or Asks integrations, Intercom/Zendesk, and Linear's interface. Questions like "What's our breakdown of bug reports vs. feature requests look like, and how many of them are solved" can be explored with [Insights](https://linear.app/docs/insights):

![Insights showing bugs/feature requests/quick wins/mobile feas, broken down by status](https://webassets.linear.app/images/ornj730p/production/590af179a56bf8e74f60838cbb9ff4a42cb759c9-1242x862.png?q=95&auto=format&dpr=2)

Or, investigate the breakdown of template use by intake source:

![Insights sliced by source and segmented by template](https://webassets.linear.app/images/ornj730p/production/af3a7409ca32ae87de8a695ea54f2f3cfc687295-1247x925.png?q=95&auto=format&dpr=2)