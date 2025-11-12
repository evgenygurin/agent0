# Agent Security

> Security considerations for using Cursor Agent

Prompt injection, AI hallucinations, and other issues may cause AI to behave in unexpected and potentially malicious ways. While we continue to work on solving prompt injection at a more foundational level, our primary protection in Cursor products are guardrails around what an agent can do, including requiring manual approval for sensitive actions by default. The goal of this document is to explain our guardrails and what users can expect from them.

All of the controls and behavior below are our default and recommended settings.

## First-party tool calls

Cursor comes bundled with tools that enable the agent to help our users write code. These include file read, edits, calling terminal commands, searching the web for documentation, and others.

Read tools do not require approval (ie reading files, searching across code). Users may use [.cursorignore](/en/context/ignore-files) to block the agent from accessing specific files at all, but otherwise reads are generally permitted without approval. For actions that carry risk of exfiltrating sensitive data, we require explicit approval.

Modifying files within the current workspace does not require explicit approval with some exceptions. When an agent makes changes to files they are immediately saved to disk. We recommend that Cursor be run in version controlled workspaces, so that the contents of the files can be reverted at any time. We require explicit approval before changing files that modify the configuration of our IDE/CLI, such as the workspace settings file of the editor. However, users automatically reloading on file change should be aware that agent changes to files may trigger automatic execution before they have had a chance to review the changes.

Any terminal command suggested by Agents requires approval by default. We recommend that users review every command before the agent executes it. Users who accept the risk may choose to enable the agent to run all commands without approval. We include an [allowlist](/en/agent/tools) feature in Cursor, but do not consider it to be a security control. Some users choose to allow specific commands, but this is a best effort system and bypasses may be possible. We do not recommend "Run Everything", which bypasses any configured allowlists.

## Third-party tool calls

Cursor enables connecting external tools via [MCP](/en/context/mcp). All third party MCP connections must be explicitly approved by the user. Once a user approves an MCP, by default each tool call suggested in Agent Mode for every external MCP integration must be explicitly approved prior to execution.

## Network requests

Network requests may be used by an attacker to exfiltrate data. We presently do not support any first-party tools making network requests outside of a very select set of hosts (ie Github), explicit link retrieval, and to support web search with a select set of providers. Arbitrary agent network requests are prevented with default settings.

## Workspace trust

The Cursor IDE supports the standard [workspace trust](https://code.visualstudio.com/docs/editing/workspaces/workspace-trust) feature that is *disabled* by default. Workspace trust presents users with a prompt when they open a new workspace to choose normal or restricted mode. Restricted mode breaks AI and other features our users typically use Cursor for. We recommend other tools, such as a basic text editor for working with repos that you do not trust.

Workspace trust may be enabled in a users' settings by performing these steps:

1. Open your user settings.json file
2. Add the following configuration:
   ```json  theme={null}
   "security.workspace.trust.enabled": true
   ```

This setting can also be enforced organization-wide through Mobile Device Management (MDM) solutions.

## Responsible disclosure

If you believe you have found a vulnerability in Cursor, please follow the guide on our GitHub Security page and submit the report there. If you're unable to use GitHub, you may also reach us at [security@cursor.com](mailto:security@cursor.com).

We commit to acknowledging vulnerability reports within 5 business days, and addressing them as soon as we are able to. We will publish the results in the form of security advisories on our GitHub security page. Critical incidents will be communicated both on the GitHub security page and via email to all users.
