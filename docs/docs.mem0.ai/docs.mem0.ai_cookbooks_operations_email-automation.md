# Automated Email Intelligence - Mem0
Source: https://docs.mem0.ai/cookbooks/operations/email-automation
Downloaded: 2025-11-12 21:20:21
================================================================================


## ​Overview
[​](https://docs.mem0.ai/cookbooks/operations/email-automation#overview)- Stores emails as searchable memories
- Categorizes emails automatically
- Retrieves relevant past conversations
- Prioritizes messages based on importance
- Generates summaries and action items

## ​Setup
[​](https://docs.mem0.ai/cookbooks/operations/email-automation#setup)
```
pip install mem0ai openai

```

## ​Implementation
[​](https://docs.mem0.ai/cookbooks/operations/email-automation#implementation)
### ​Basic Email Memory System
[​](https://docs.mem0.ai/cookbooks/operations/email-automation#basic-email-memory-system)
```
import os
from mem0 import MemoryClient
from email.parser import Parser

# Configure API keys
os.environ["MEM0_API_KEY"] = "your-mem0-api-key"

# Initialize Mem0 client
client = MemoryClient()

class EmailProcessor:
    def __init__(self):
        """Initialize the Email Processor with Mem0 memory client"""
        self.client = client
        
    def process_email(self, email_content, user_id):
        """
        Process an email and store it in Mem0 memory
        
        Args:
            email_content (str): Raw email content
            user_id (str): User identifier for memory association
        """
        # Parse email
        parser = Parser()
        email = parser.parsestr(email_content)
        
        # Extract email details
        sender = email['from']
        recipient = email['to']
        subject = email['subject']
        date = email['date']
        body = self._get_email_body(email)
        
        # Create message object for Mem0
        message = {
            "role": "user",
            "content": f"Email from {sender}: {subject}\n\n{body}"
        }
        
        # Create metadata for better retrieval
        metadata = {
            "email_type": "incoming",
            "sender": sender,
            "recipient": recipient,
            "subject": subject,
            "date": date
        }
        
        # Store in Mem0 with appropriate categories
        response = self.client.add(
            messages=[message],
            user_id=user_id,
            metadata=metadata,
            categories=["email", "correspondence"],
            
        )
        
        return response
    
    def _get_email_body(self, email):
        """Extract the body content from an email"""
        # Simplified extraction - in real-world, handle multipart emails
        if email.is_multipart():
            for part in email.walk():
                if part.get_content_type() == "text/plain":
                    return part.get_payload(decode=True).decode()
        else:
            return email.get_payload(decode=True).decode()
    
    def search_emails(self, query, user_id, sender=None):
        """
        Search through stored emails

        Args:
            query (str): Search query
            user_id (str): User identifier
            sender (str, optional): Filter by sender email address
        """
        # For Platform API, all filters including user_id go in filters object
        if not sender:
            # Simple filter - just user_id and category
            filters = {
                "AND": [
                    {"user_id": user_id},
                    {"categories": {"contains": "email"}}
                ]
            }
            results = self.client.search(query=query, filters=filters)
        else:
            # Advanced filter - add sender condition
            filters = {
                "AND": [
                    {"user_id": user_id},
                    {"categories": {"contains": "email"}},
                    {"sender": sender}
                ]
            }
            results = self.client.search(query=query, filters=filters)

        return results
        
    def get_email_thread(self, subject, user_id):
        """
        Retrieve all emails in a thread based on subject

        Args:
            subject (str): Email subject to match
            user_id (str): User identifier
        """
        # For Platform API, user_id goes in the filters object
        filters = {
            "AND": [
                {"user_id": user_id},
                {"categories": {"contains": "email"}},
                {"subject": {"icontains": subject}}
            ]
        }

        thread = self.client.get_all(filters=filters)

        return thread

# Initialize the processor
processor = EmailProcessor()

# Example raw email
sample_email = """From: [email protected]
To: [email protected]
Subject: Meeting Schedule Update
Date: Mon, 15 Jul 2024 14:22:05 -0700

Hi Bob,

I wanted to update you on the schedule for our upcoming project meeting.
We'll be meeting this Thursday at 2pm instead of Friday.

Could you please prepare your section of the presentation?

Thanks,
Alice
"""

# Process and store the email
user_id = "[email protected]"
processor.process_email(sample_email, user_id)

# Later, search for emails about meetings
meeting_emails = processor.search_emails("meeting schedule", user_id)
print(f"Found {len(meeting_emails['results'])} relevant emails")

```
[[email protected]](https://docs.mem0.ai/cdn-cgi/l/email-protection)[[email protected]](https://docs.mem0.ai/cdn-cgi/l/email-protection)[[email protected]](https://docs.mem0.ai/cdn-cgi/l/email-protection)
## ​Key Features and Benefits
[​](https://docs.mem0.ai/cookbooks/operations/email-automation#key-features-and-benefits)- Long-term Email Memory: Store and retrieve email conversations across long periods
- Semantic Search: Find relevant emails even if they don’t contain exact keywords
- Intelligent Categorization: Automatically sort emails into meaningful categories
- Action Item Extraction: Identify and track tasks mentioned in emails
- Priority Management: Focus on important emails based on AI-determined priority
- Context Awareness: Maintain thread context for more relevant interactions

## ​Conclusion
[​](https://docs.mem0.ai/cookbooks/operations/email-automation#conclusion)[Tag and Organize MemoriesCategorize email threads by sender, topic, and priority for faster retrieval.](https://docs.mem0.ai/cookbooks/essentials/tagging-and-organizing-memories)
## Tag and Organize Memories
[Support Inbox with Mem0Build customer support agents that remember context across tickets.](https://docs.mem0.ai/cookbooks/operations/support-inbox)
## Support Inbox with Mem0
