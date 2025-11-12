# Multimodal Support - Mem0
Source: https://docs.mem0.ai/platform/features/multimodal-support
Downloaded: 2025-11-12 21:20:18
================================================================================


## ​How It Works
[​](https://docs.mem0.ai/platform/features/multimodal-support#how-it-works)
```
import os
from mem0 import MemoryClient

os.environ["MEM0_API_KEY"] = "your-api-key"

client = MemoryClient()

messages = [
    {
        "role": "user",
        "content": "Hi, my name is Alice."
    },
    {
        "role": "assistant",
        "content": "Nice to meet you, Alice! What do you like to eat?"
    },
    {
        "role": "user",
        "content": {
            "type": "image_url",
            "image_url": {
                "url": "https://www.superhealthykids.com/wp-content/uploads/2021/10/best-veggie-pizza-featured-image-square-2.jpg"
            }
        }
    },
]

# Calling the add method to ingest messages into the memory system
client.add(messages, user_id="alice")

```

## ​Supported Media Types
[​](https://docs.mem0.ai/platform/features/multimodal-support#supported-media-types)- Images- JPG, PNG, and other common image formats
- Documents- MDX, TXT, and PDF files

## ​Integration Methods
[​](https://docs.mem0.ai/platform/features/multimodal-support#integration-methods)
### ​1. Images
[​](https://docs.mem0.ai/platform/features/multimodal-support#1-images)
#### ​Using an Image URL
[​](https://docs.mem0.ai/platform/features/multimodal-support#using-an-image-url)
```
# Define the image URL
image_url = "https://www.superhealthykids.com/wp-content/uploads/2021/10/best-veggie-pizza-featured-image-square-2.jpg"

# Create the message dictionary with the image URL
image_message = {
    "role": "user",
    "content": {
        "type": "image_url",
        "image_url": {
            "url": image_url
        }
    }
}
client.add([image_message], user_id="alice")

```

#### ​Using Base64 Image Encoding for Local Files
[​](https://docs.mem0.ai/platform/features/multimodal-support#using-base64-image-encoding-for-local-files)
```
import base64

# Path to the image file
image_path = "path/to/your/image.jpg"

# Encode the image in Base64
with open(image_path, "rb") as image_file:
    base64_image = base64.b64encode(image_file.read()).decode("utf-8")

# Create the message dictionary with the Base64-encoded image
image_message = {
    "role": "user",
    "content": {
        "type": "image_url",
        "image_url": {
            "url": f"data:image/jpeg;base64,{base64_image}"
        }
    }
}
client.add([image_message], user_id="alice")

```

### ​2. Text Documents (MDX/TXT)
[​](https://docs.mem0.ai/platform/features/multimodal-support#2-text-documents-mdx%2Ftxt)
#### ​Using a Document URL
[​](https://docs.mem0.ai/platform/features/multimodal-support#using-a-document-url)
```
# Define the document URL
document_url = "https://www.w3.org/TR/2003/REC-PNG-20031110/iso_8859-1.txt"

# Create the message dictionary with the document URL
document_message = {
    "role": "user",
    "content": {
        "type": "mdx_url",
        "mdx_url": {
            "url": document_url
        }
    }
}
client.add([document_message], user_id="alice")

```

#### ​Using Base64 Encoding for Local Documents
[​](https://docs.mem0.ai/platform/features/multimodal-support#using-base64-encoding-for-local-documents)
```
import base64

# Path to the document file
document_path = "path/to/your/document.txt"

# Function to convert file to Base64
def file_to_base64(file_path):
    with open(file_path, "rb") as file:
        return base64.b64encode(file.read()).decode('utf-8')

# Encode the document in Base64
base64_document = file_to_base64(document_path)

# Create the message dictionary with the Base64-encoded document
document_message = {
    "role": "user",
    "content": {
        "type": "mdx_url",
        "mdx_url": {
            "url": base64_document
        }
    }
}
client.add([document_message], user_id="alice")

```

### ​3. PDF Documents
[​](https://docs.mem0.ai/platform/features/multimodal-support#3-pdf-documents)
```
# Define the PDF URL
pdf_url = "https://www.w3.org/WAI/ER/tests/xhtml/testfiles/resources/pdf/dummy.pdf"

# Create the message dictionary with the PDF URL
pdf_message = {
    "role": "user",
    "content": {
        "type": "pdf_url",
        "pdf_url": {
            "url": pdf_url
        }
    }
}
client.add([pdf_message], user_id="alice")

```

## ​Complete Example with Multiple File Types
[​](https://docs.mem0.ai/platform/features/multimodal-support#complete-example-with-multiple-file-types)
```
import base64
from mem0 import MemoryClient

client = MemoryClient()

def file_to_base64(file_path):
    with open(file_path, "rb") as file:
        return base64.b64encode(file.read()).decode('utf-8')

# Example 1: Using an image URL
image_message = {
    "role": "user",
    "content": {
        "type": "image_url",
        "image_url": {
            "url": "https://example.com/sample-image.jpg"
        }
    }
}

# Example 2: Using a text document URL
text_message = {
    "role": "user",
    "content": {
        "type": "mdx_url",
        "mdx_url": {
            "url": "https://www.w3.org/TR/2003/REC-PNG-20031110/iso_8859-1.txt"
        }
    }
}

# Example 3: Using a PDF URL
pdf_message = {
    "role": "user",
    "content": {
        "type": "pdf_url",
        "pdf_url": {
            "url": "https://www.w3.org/WAI/ER/tests/xhtml/testfiles/resources/pdf/dummy.pdf"
        }
    }
}

# Add each message to the memory system
client.add([image_message], user_id="alice")
client.add([text_message], user_id="alice")
client.add([pdf_message], user_id="alice")

```
[DiscordJoin our community](https://mem0.dev/DiD)
## Discord
[GitHubAsk questions on GitHub](https://github.com/mem0ai/mem0/discussions/new?category=q-a)
## GitHub
[SupportTalk to founders](https://cal.com/taranjeetio/meet)
## Support
