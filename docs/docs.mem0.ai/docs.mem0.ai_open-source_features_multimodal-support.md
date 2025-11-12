# Multimodal Support - Mem0
Source: https://docs.mem0.ai/open-source/features/multimodal-support
Downloaded: 2025-11-12 21:20:19
================================================================================

- Users share screenshots, menus, or documents and you want the details to become memories.
- You already collect text conversations but need visual context for better answers.
- You want a single workflow that handles both URLs and local image files.

## ​Feature anatomy
[​](https://docs.mem0.ai/open-source/features/multimodal-support#feature-anatomy)- Vision processing:Mem0 runs the image through a vision model that extracts text and key details.
- Memory creation:Extracted information is stored as standard memories so search, filters, and analytics continue to work.
- Context linking:Visual and textual turns in the same conversation stay linked, giving agents richer context.
- Flexible inputs:Accept publicly accessible URLs or base64-encoded local files in both Python and JavaScript SDKs.

Supported formats

## ​Configure it
[​](https://docs.mem0.ai/open-source/features/multimodal-support#configure-it)
### ​Add image messages from URLs
[​](https://docs.mem0.ai/open-source/features/multimodal-support#add-image-messages-from-urls)
```
from mem0 import Memory

client = Memory()

messages = [
    {"role": "user", "content": "Hi, my name is Alice."},
    {
        "role": "user",
        "content": {
            "type": "image_url",
            "image_url": {
                "url": "https://example.com/menu.jpg"
            }
        }
    }
]

client.add(messages, user_id="alice")

```

### ​Upload local images as base64
[​](https://docs.mem0.ai/open-source/features/multimodal-support#upload-local-images-as-base64)
```
import base64
from mem0 import Memory

def encode_image(image_path):
    with open(image_path, "rb") as image_file:
        return base64.b64encode(image_file.read()).decode("utf-8")

client = Memory()
base64_image = encode_image("path/to/your/image.jpg")

messages = [
    {
        "role": "user",
        "content": [
            {"type": "text", "text": "What's in this image?"},
            {
                "type": "image_url",
                "image_url": {
                    "url": f"data:image/jpeg;base64,{base64_image}"
                }
            }
        ]
    }
]

client.add(messages, user_id="alice")

```

## ​See it in action
[​](https://docs.mem0.ai/open-source/features/multimodal-support#see-it-in-action)
### ​Restaurant menu memory
[​](https://docs.mem0.ai/open-source/features/multimodal-support#restaurant-menu-memory)
```
from mem0 import Memory

client = Memory()

messages = [
    {
        "role": "user",
        "content": "Help me remember which dishes I liked."
    },
    {
        "role": "user",
        "content": {
            "type": "image_url",
            "image_url": {
                "url": "https://example.com/restaurant-menu.jpg"
            }
        }
    },
    {
        "role": "user",
        "content": "I’m allergic to peanuts and prefer vegetarian meals."
    }
]

result = client.add(messages, user_id="user123")
print(result)

```

### ​Document capture
[​](https://docs.mem0.ai/open-source/features/multimodal-support#document-capture)
```
messages = [
    {
        "role": "user",
        "content": "Store this receipt information for expenses."
    },
    {
        "role": "user",
        "content": {
            "type": "image_url",
            "image_url": {
                "url": "https://example.com/receipt.jpg"
            }
        }
    }
]

client.add(messages, user_id="user123")

```

### ​Error handling
[​](https://docs.mem0.ai/open-source/features/multimodal-support#error-handling)
```
from mem0 import Memory
from mem0.exceptions import InvalidImageError, FileSizeError

client = Memory()

try:
    messages = [{
        "role": "user",
        "content": {
            "type": "image_url",
            "image_url": {"url": "https://example.com/image.jpg"}
        }
    }]

    client.add(messages, user_id="user123")
    print("Image processed successfully")

except InvalidImageError:
    print("Invalid image format or corrupted file")
except FileSizeError:
    print("Image file too large")
except Exception as exc:
    print(f"Unexpected error: {exc}")

```

## ​Verify the feature is working
[​](https://docs.mem0.ai/open-source/features/multimodal-support#verify-the-feature-is-working)- After callingadd, inspect the returned memories and confirm they include image-derived text (menu items, receipt totals, etc.).
`add`- Run a follow-upsearchfor a detail from the image; the memory should surface alongside related text.
`search`- Monitor image upload latency—large files should still complete under your acceptable response time.
- Log file size and URL sources to troubleshoot repeated failures.

## ​Best practices
[​](https://docs.mem0.ai/open-source/features/multimodal-support#best-practices)- Ask for intent:Prompt users to explain why they sent an image so the memory includes the right context.
- Keep images readable:Encourage clear photos without heavy filters or shadows for better extraction.
- Split bulk uploads:Send multiple images as separateaddcalls to isolate failures and improve reliability.
`add`- Watch privacy:Avoid uploading sensitive documents unless your environment is secured for that data.
- Validate file size early:Check file size before encoding to save bandwidth and time.

## ​Troubleshooting
[​](https://docs.mem0.ai/open-source/features/multimodal-support#troubleshooting)`data:image/<type>;base64,`[Connect Vision ModelsReview supported vision-capable models and configuration details.](https://docs.mem0.ai/components/llms/models/openai)
## Connect Vision Models
[Build Multimodal RetrievalFollow an end-to-end workflow pairing text and image memories.](https://docs.mem0.ai/cookbooks/frameworks/multimodal-retrieval)
## Build Multimodal Retrieval
