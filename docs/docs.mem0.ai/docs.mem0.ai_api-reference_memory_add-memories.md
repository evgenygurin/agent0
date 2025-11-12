# Add Memories - Mem0
Source: https://docs.mem0.ai/api-reference/memory/add-memories
Downloaded: 2025-11-12 21:20:21
================================================================================


## ​Graph Memory
[​](https://docs.mem0.ai/api-reference/memory/add-memories#graph-memory)`enable_graph=True`[Graph Memory documentation](https://docs.mem0.ai/platform/features/graph-memory)
#### Authorizations
[​](https://docs.mem0.ai/api-reference/memory/add-memories#authorization-authorization)
API key authentication. Prefix your Mem0 API key with 'Token '. Example: 'Token your_api_key'

#### Body
[​](https://docs.mem0.ai/api-reference/memory/add-memories#body-messages)
An array of message objects representing the content of the memory. Each message object typically contains 'role' and 'content' fields, where 'role' indicates the sender either 'user' or 'assistant' and 'content' contains the actual message text. This structure allows for the representation of conversations or multi-part memories.

Showchild attributes
[​](https://docs.mem0.ai/api-reference/memory/add-memories#body-agent-id)
The unique identifier of the agent associated with this memory.
[​](https://docs.mem0.ai/api-reference/memory/add-memories#body-user-id)
The unique identifier of the user associated with this memory.
[​](https://docs.mem0.ai/api-reference/memory/add-memories#body-app-id)
The unique identifier of the application associated with this memory.
[​](https://docs.mem0.ai/api-reference/memory/add-memories#body-run-id)
The unique identifier of the run associated with this memory.
[​](https://docs.mem0.ai/api-reference/memory/add-memories#body-metadata)
Additional metadata associated with the memory, which can be used to store any additional information or context about the memory. Best practice for incorporating additional information is through metadata (e.g. location, time, ids, etc.). During retrieval, you can either use these metadata alongside the query to fetch relevant memories or retrieve memories based on the query first and then refine the results using metadata during post-processing.
[​](https://docs.mem0.ai/api-reference/memory/add-memories#body-includes)
String to include the specific preferences in the memory.
`1`[​](https://docs.mem0.ai/api-reference/memory/add-memories#body-excludes)
String to exclude the specific preferences in the memory.
`1`[​](https://docs.mem0.ai/api-reference/memory/add-memories#body-infer)
Whether to infer the memories or directly store the messages.
[​](https://docs.mem0.ai/api-reference/memory/add-memories#body-output-format)
Controls the response format structure.v1.0(deprecated) returns a direct array of memory objects:[{...}, {...}].v1.1(recommended) returns an object with a 'results' key containing the array:{"results": [...]}. Thev1.0format will be removed in future versions.
`v1.0``[{...}, {...}]``v1.1``{"results": [...]}``v1.0`[​](https://docs.mem0.ai/api-reference/memory/add-memories#body-custom-categories)
A list of categories with category name and its description.
[​](https://docs.mem0.ai/api-reference/memory/add-memories#body-custom-instructions)
Defines project-specific guidelines for handling and organizing memories. When set at the project level, they apply to all new memories in that project.
[​](https://docs.mem0.ai/api-reference/memory/add-memories#body-immutable)
Whether the memory is immutable.
[​](https://docs.mem0.ai/api-reference/memory/add-memories#body-async-mode)
Whether to add the memory completely asynchronously.
[​](https://docs.mem0.ai/api-reference/memory/add-memories#body-timestamp)
The timestamp of the memory. Format: Unix timestamp
[​](https://docs.mem0.ai/api-reference/memory/add-memories#body-expiration-date)
The date and time when the memory will expire. Format: YYYY-MM-DD
[​](https://docs.mem0.ai/api-reference/memory/add-memories#body-org-id)
The unique identifier of the organization associated with this memory.
[​](https://docs.mem0.ai/api-reference/memory/add-memories#body-project-id)
The unique identifier of the project associated with this memory.
[​](https://docs.mem0.ai/api-reference/memory/add-memories#body-version)
The version of the memory to use. The default version is v1, which is deprecated. We recommend using v2 for new applications.

#### Response

Successful memory creation.
[​](https://docs.mem0.ai/api-reference/memory/add-memories#response-id)[​](https://docs.mem0.ai/api-reference/memory/add-memories#response-data)
Showchild attributes
[​](https://docs.mem0.ai/api-reference/memory/add-memories#response-event)`ADD``UPDATE``DELETE`