# Editor

Formatting description fields.

![Linear app showing the create issue modal with formatting options](https://webassets.linear.app/images/ornj730p/production/7e24eaf2c9e80406b3fc082445476c0a04a16b03-2160x1327.png?q=95&auto=format&dpr=2)

## Overview

We support most Markdown elements in our text editor. Type in Markdown or paste it directly and it will be converted into rich text automatically.

Read more about Markdown and access full capabilities [here](https://www.markdownguide.org/basic-syntax/).

You can also apply styling with a toolbar, which will pop up after you highlight a word or phrase or using slash commands when typing `/`.

### Keyboard

See below for keyboard shortcuts or search specific ones with `?`

### Mouse

Highlight text in edit mode to launch WYSIWYG editor

### Command menu

`markdown` when viewing an issue to copy issue in Markdown

## Formatting

These styles can be applied using keyboard shortcuts or by highlighting text to bring up a styling toolbar. You can also hit `/` on your keyboard to bring up the formatting options:

### Text styling

* `**text**` or `Cmd/Ctrl` `B` for **bold text**
* `_text_` or `Cmd/Ctrl` `I` or `Cmd/Ctrl` `>` for _italicized text_
* `~text~` or `Cmd/Ctrl` `S` to strikethrough text
* `Cmd/Ctrl` `U` for underlined text
* `Cmd/Ctrl` `E` for inline code
* `#` then `Space` Heading 1
* `##` then `Space` Heading 2
* `###` then `Space` Heading 3

### Lists

* `*`, `-`, or `+` then `space` or `Cmd/Ctrl` `Shift` `8` for a bulleted list
* `1.` or `Cmd/Ctrl` `Shift` `9` for a numbered list
* `[]` or `Cmd/Ctrl` ``Shift`` `7` for a checklist

### Other formatting options

* `Cmd/Ctrl` `K` Turn text into link (or directly paste issue or URLs for clickable links)
* `>` then `Space` for blockquotes
* `>>>` then `Space `for collapsible section
* `Code` or `Cmd/Ctrl` `Shift` `\` for a code block
* _/collapsible section_ to create a toggle/collapsible text
* `___` then `space` for a horizontal divider
* `|--` to create a new table
* _/table_ to create a table element
* _/date_ or @Oct 1 to insert a date

### Attachments

* /file or /inset to attach files
* `Cmd` `Shift` `u` to upload files

### Helpful commands

* `Cmd/Ctrl` `A` to select all content in an issue (to copy or delete)
* `Cmd/Ctrl` `Z` to undo typing
* `Cmd/Ctrl` `Shift` `Z` to redo typing
* Copy the issue description in Markdown by opening the command menu (`Cmd/Ctrl` `K`) when viewing the issue and selecting the command _`copy issue in markdown`_
* `Shift` `Enter` to generate a line break
* `Enter` `Enter` to break out of codeblock or blockquote formatting

### Embeds

Linear automatically detects links from common applications (Youtube, Descript, Loom) and will embed them automatically. Pasting a Figma link will embed a file preview as long as have the [Figma integration](https://linear.app/docs/figma#configure) set up.

If you'd prefer to display the url rather than the embed, click _Keep as link_ or press `esc` after pasting the link.

![Embed options on a Link showing "Keep as link" or "Show embed"](https://webassets.linear.app/images/ornj730p/production/03fa5525ef03ec400de8eabbcb684aa2fc739f1a-555x95.png?q=95&auto=format&dpr=2)

### Emoji

Add emojis to descriptions or comments with our native emoji picker or by typing `:` followed by the emoji name, such as `:100:` for 💯 and `:+1:` for 👍 .

### @ Mentions 

Write `@text` to mention a user, issue, project, date, or document in a description or comment. For users, this will send a notification to their Inbox and subscribe them to the issue. We only support single user mentions at the moment, not user groups.

Pasting an issue ID will also link it in the editor. Referenced issues are added as [related issues](https://linear.app/docs/issue-relations) automatically.