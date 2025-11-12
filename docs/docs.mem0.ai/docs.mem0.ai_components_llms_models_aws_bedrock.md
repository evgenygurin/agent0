# AWS Bedrock - Mem0
Source: https://docs.mem0.ai/components/llms/models/aws_bedrock
Downloaded: 2025-11-12 21:20:19
================================================================================


### ​Setup
[​](https://docs.mem0.ai/components/llms/models/aws_bedrock#setup)- Before using the AWS Bedrock LLM, make sure you have the appropriate model access fromBedrock Console.
[Bedrock Console](https://us-east-1.console.aws.amazon.com/bedrock/home?region=us-east-1#/modelaccess)- You will also need to authenticate theboto3client by using a method in theAWS documentation
`boto3`[AWS documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/guide/credentials.html#configuring-credentials)- You will have to exportAWS_REGION,AWS_ACCESS_KEY, andAWS_SECRET_ACCESS_KEYto set environment variables.
`AWS_REGION``AWS_ACCESS_KEY``AWS_SECRET_ACCESS_KEY`
### ​Usage
[​](https://docs.mem0.ai/components/llms/models/aws_bedrock#usage)
```
import os
from mem0 import Memory

os.environ['AWS_REGION'] = 'us-west-2'
os.environ["AWS_ACCESS_KEY_ID"] = "xx"
os.environ["AWS_SECRET_ACCESS_KEY"] = "xx"

config = {
    "llm": {
        "provider": "aws_bedrock",
        "config": {
            "model": "anthropic.claude-3-5-haiku-20241022-v1:0",
            "temperature": 0.2,
            "max_tokens": 2000,
        }
    }
}

m = Memory.from_config(config)
messages = [
    {"role": "user", "content": "I'm planning to watch a movie tonight. Any recommendations?"},
    {"role": "assistant", "content": "How about thriller movies? They can be quite engaging."},
    {"role": "user", "content": "I’m not a big fan of thriller movies but I love sci-fi movies."},
    {"role": "assistant", "content": "Got it! I'll avoid thriller recommendations and suggest sci-fi movies in the future."}
]
m.add(messages, user_id="alice", metadata={"category": "movies"})

```

### ​Config
[​](https://docs.mem0.ai/components/llms/models/aws_bedrock#config)`aws_bedrock`[Master List of All Params in Config](https://docs.mem0.ai/components/llms/config)