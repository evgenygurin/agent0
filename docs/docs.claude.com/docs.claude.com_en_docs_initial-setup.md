# Get started with Claude - Claude Docs
Source: https://docs.claude.com/en/docs/initial-setup
Downloaded: 2025-11-12 21:19:23
================================================================================


## ​Prerequisites
[​](https://docs.claude.com/en/docs/initial-setup#prerequisites)- An AnthropicConsole account
[Console account](https://console.anthropic.com/)- AnAPI key
[API key](https://console.anthropic.com/settings/keys)
## ​Call the API
[​](https://docs.claude.com/en/docs/initial-setup#call-the-api)- cURL
- Python
- TypeScript
- Java

Set your API key
[Claude Console](https://console.anthropic.com/settings/keys)
```
export ANTHROPIC_API_KEY='your-api-key-here'

```

Make your first API call

```
curl https://api.anthropic.com/v1/messages \
  -H "Content-Type: application/json" \
  -H "x-api-key: $ANTHROPIC_API_KEY" \
  -H "anthropic-version: 2023-06-01" \
  -d '{
    "model": "claude-sonnet-4-5",
    "max_tokens": 1000,
    "messages": [
      {
        "role": "user", 
        "content": "What should I search for to find the latest developments in renewable energy?"
      }
    ]
  }'

```

```
{
  "id": "msg_01HCDu5LRGeP2o7s2xGmxyx8",
  "type": "message", 
  "role": "assistant",
  "content": [
    {
      "type": "text",
      "text": "Here are some effective search strategies to find the latest renewable energy developments:\n\n## Search Terms to Use:\n- \"renewable energy news 2024\"\n- \"clean energy breakthrough\"\n- \"solar/wind/battery technology advances\"\n- \"green energy innovations\"\n- \"climate tech developments\"\n- \"energy storage solutions\"\n\n## Best Sources to Check:\n\n**News & Industry Sites:**\n- Renewable Energy World\n- GreenTech Media (now Wood Mackenzie)\n- Energy Storage News\n- CleanTechnica\n- PV Magazine (for solar)\n- WindPower Engineering & Development..."
    }
  ],
  "model": "claude-sonnet-4-5",
  "stop_reason": "end_turn",
  "usage": {
    "input_tokens": 21,
    "output_tokens": 305
  }
}

```

## ​Next steps
[​](https://docs.claude.com/en/docs/initial-setup#next-steps)[Working with MessagesLearn common patterns for the Messages API.](https://docs.claude.com/en/docs/build-with-claude/working-with-messages)
## Working with Messages
[Features OverviewExplore Claude’s advanced features and capabilities.](https://docs.claude.com/en/api/overview)
## Features Overview
[Client SDKsDiscover Anthropic client libraries.](https://docs.claude.com/en/api/client-sdks)
## Client SDKs
[Claude CookbookLearn with interactive Jupyter notebooks.](https://github.com/anthropics/anthropic-cookbook)
## Claude Cookbook
