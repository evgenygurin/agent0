# Persistent Eliza Characters - Mem0
Source: https://docs.mem0.ai/cookbooks/frameworks/eliza-os-character
Downloaded: 2025-11-12 21:20:21
================================================================================


## ​Overview
[​](https://docs.mem0.ai/cookbooks/frameworks/eliza-os-character#overview)
## ​Setup
[​](https://docs.mem0.ai/cookbooks/frameworks/eliza-os-character#setup)
```
git clone https://github.com/elizaOS/eliza.git

```

```
cd eliza

```

```
pnpm install

```

```
pnpm build

```

## ​Setup ENVs
[​](https://docs.mem0.ai/cookbooks/frameworks/eliza-os-character#setup-envs)`.env``.env.example`
```
# Mem0 Configuration
MEM0_API_KEY= # Mem0 API Key (get from https://app.mem0.ai/dashboard/api-keys)
MEM0_USER_ID= # Default: eliza-os-user
MEM0_PROVIDER= # Default: openai
MEM0_PROVIDER_API_KEY= # API Key for the provider (OpenAI, Anthropic, etc.)
SMALL_MEM0_MODEL= # Default: gpt-4.1-nano
MEDIUM_MEM0_MODEL= # Default: gpt-4o
LARGE_MEM0_MODEL= # Default: gpt-4o

```

## ​Make the default character use Mem0
[​](https://docs.mem0.ai/cookbooks/frameworks/eliza-os-character#make-the-default-character-use-mem0)`eliza``agent/src/defaultCharacter.ts`
```
modelProvider: ModelProviderName.MEM0,

```

## ​Run the project
[​](https://docs.mem0.ai/cookbooks/frameworks/eliza-os-character#run-the-project)
```
pnpm start

```

## ​Conclusion
[​](https://docs.mem0.ai/cookbooks/frameworks/eliza-os-character#conclusion)[Build AI with PersonalitySeparate agent and user memories to maintain consistent character personalities.](https://docs.mem0.ai/cookbooks/essentials/building-ai-with-personality)
## Build AI with Personality
[AI Tutor with Mem0Build another type of personalized companion with memory capabilities.](https://docs.mem0.ai/cookbooks/companions/ai-tutor)
## AI Tutor with Mem0
