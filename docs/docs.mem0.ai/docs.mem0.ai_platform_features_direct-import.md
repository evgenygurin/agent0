# Direct Import - Mem0
Source: https://docs.mem0.ai/platform/features/direct-import
Downloaded: 2025-11-12 21:20:18
================================================================================


## ​How to Use Direct Import
[​](https://docs.mem0.ai/platform/features/direct-import#how-to-use-direct-import)`infer``False``add`
```
messages = [
    {"role": "user", "content": "Alice loves playing badminton"},
    {"role": "assistant", "content": "That's great! Alice is a fitness freak"},
    {"role": "user", "content": "Alice mostly cooks at home because of her gym plan"},
]


client.add(messages, user_id="alice", infer=False)

```
`infer=True`
## ​How to Retrieve Memories
[​](https://docs.mem0.ai/platform/features/direct-import#how-to-retrieve-memories)`search`
```
client.search("What is Alice's favorite sport?", user_id="alice")

```

## ​How to Retrieve All Memories
[​](https://docs.mem0.ai/platform/features/direct-import#how-to-retrieve-all-memories)`get_all`
```
client.get_all(query="What is Alice's favorite sport?", user_id="alice")

```
[DiscordJoin our community](https://mem0.dev/DiD)
## Discord
[GitHubAsk questions on GitHub](https://github.com/mem0ai/mem0/discussions/new?category=q-a)
## GitHub
[SupportTalk to founders](https://cal.com/taranjeetio/meet)
## Support
