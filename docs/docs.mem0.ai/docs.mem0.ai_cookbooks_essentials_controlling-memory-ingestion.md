# Control Memory Ingestion - Mem0
Source: https://docs.mem0.ai/cookbooks/essentials/controlling-memory-ingestion
Downloaded: 2025-11-12 21:20:21
================================================================================


## ​Overview
[​](https://docs.mem0.ai/cookbooks/essentials/controlling-memory-ingestion#overview)- Custom instructionsdefine what to remember and what to ignore.
- Confidence thresholdsensure only verified facts persist.
- Memory updateslet you change information without creating duplicates.
- Filter speculative statements with custom instructions
- Configure confidence thresholds for fact verification
- Update stored information without duplication
- Build a complete ingestion pipeline

## ​Setup
[​](https://docs.mem0.ai/cookbooks/essentials/controlling-memory-ingestion#setup)
```
from mem0 import MemoryClient

client = MemoryClient(api_key="your-api-key")

```
`your-api-key`[dashboard](https://app.mem0.ai)
## ​The Problem
[​](https://docs.mem0.ai/cookbooks/essentials/controlling-memory-ingestion#the-problem)
```
# Patient mentions speculation
messages = [{"role": "user", "content": "I think I might be allergic to penicillin"}]
client.add(messages, user_id="patient_123")

# Check what got stored
results = client.search("patient allergies", filters={"user_id": "patient_123"})
print(results['results'][0]['memory'])


```

```
Patient is allergic to penicillin

```

## ​Custom Instructions
[​](https://docs.mem0.ai/cookbooks/essentials/controlling-memory-ingestion#custom-instructions)
```
instructions = """
Only store CONFIRMED medical facts.

Store:
- Confirmed diagnoses from doctors
- Known allergies with documented reactions
- Current medications being taken

Ignore:
- Speculation (words like "might", "maybe", "I think")
- Unverified symptoms
- Casual mentions without confirmation
"""

client.project.update(custom_instructions=instructions)

# Same speculative statement
messages = [{"role": "user", "content": "I think I might be allergic to penicillin"}]
client.add(messages, user_id="patient_123")

# Check what got stored
results = client.get_all(filters={"user_id": "patient_123"})
print(f"Memories stored: {len(results['results'])}")


```

```
Memories stored: 0

```

## ​Designing Custom Instructions
[​](https://docs.mem0.ai/cookbooks/essentials/controlling-memory-ingestion#designing-custom-instructions)
```
# Too strict - filters out useful context
"""
Only store information if explicitly stated by a doctor with full name,
date, time, and medical license number.
"""


```

```
# Too loose - stores speculation as fact
"""
Store any health-related information mentioned.
"""


```

```
# Clear categories with examples
"""
Store CONFIRMED facts:
- Diagnoses: "Dr. Smith diagnosed hypertension on March 15th"
- Allergies: "Patient had hives reaction to penicillin"
- Medications: "Taking Lisinopril 10mg daily"

Ignore SPECULATION:
- "I think I might have..."
- "Maybe it's..."
- "Could be related to..."
"""


```

## ​Confidence Thresholds
[​](https://docs.mem0.ai/cookbooks/essentials/controlling-memory-ingestion#confidence-thresholds)
### ​Setting Thresholds
[​](https://docs.mem0.ai/cookbooks/essentials/controlling-memory-ingestion#setting-thresholds)- High-stakes domains(medical, legal): Require 0.8+ confidence
- General assistants: 0.6+ confidence is often sufficient
- Exploratory systems: Lower thresholds (0.4+) capture more data

```
# Configure stricter instructions
client.project.update(
    custom_instructions="""
Only extract memories with HIGH confidence.
Require specific details (dates, dosages, doctor names) for medical facts.
Skip vague or uncertain statements.
"""
)

# Test with uncertain statement
messages = [{"role": "user", "content": "The doctor mentioned something about my blood pressure"}]
result1 = client.add(messages, user_id="patient_123")

# Test with confirmed fact
messages = [{"role": "user", "content": "Dr. Smith diagnosed me with hypertension on March 15th"}]
result2 = client.add(messages, user_id="patient_123")

print("Vague statement stored:", len(result1['results']) > 0)
print("Confirmed fact stored:", len(result2['results']) > 0)


```

```
Vague statement stored: False
Confirmed fact stored: True

```

## ​Filtering Sensitive Information
[​](https://docs.mem0.ai/cookbooks/essentials/controlling-memory-ingestion#filtering-sensitive-information)
```
client.project.update(
    custom_instructions="""
Medical memory rules:

STORE:
- Confirmed diagnoses
- Verified allergies
- Current medications

NEVER STORE:
- Social Security Numbers
- Insurance policy numbers
- Credit card information
- Full addresses
- Phone numbers

Replace identifiers with generic references if mentioned.
"""
)

# Test with PII
messages = [
    {"role": "user", "content": "My SSN is 123-45-6789 and I'm allergic to penicillin"}
]
client.add(messages, user_id="patient_123")

# Check what was stored
results = client.get_all(filters={"user_id": "patient_123"})
for result in results['results']:
    print(result['memory'])


```

```
Patient is allergic to penicillin

```

## ​Updating Memories
[​](https://docs.mem0.ai/cookbooks/essentials/controlling-memory-ingestion#updating-memories)
```
# Initial allergy stored
result = client.add(
    [{"role": "user", "content": "Patient confirmed allergy to penicillin with documented hives reaction"}],
    user_id="patient_123"
)

memory_id = result['results'][0]['id']
print(f"Stored memory: {memory_id}")

# Later, patient gets retested - allergy was false positive
client.update(
    memory_id=memory_id,
    text="Patient tested negative for penicillin allergy on April 2nd, 2025. Previous allergy was false positive.",
    metadata={"verified": True, "updated_date": "2025-04-02"}
)

# Retrieve the updated memory
updated = client.get(memory_id)
print(f"\\nUpdated memory: {updated['memory']}")
print(f"Metadata: {updated['metadata']}")


```

```
Stored memory: mem_abc123

Updated memory: Patient tested negative for penicillin allergy on April 2nd, 2025. Previous allergy was false positive.
Metadata: {'verified': True, 'updated_date': '2025-04-02'}


```

### ​Benefits of Updating
[​](https://docs.mem0.ai/cookbooks/essentials/controlling-memory-ingestion#benefits-of-updating)- created_atshows when the memory was first stored
`created_at`- updated_atshows when it was modified
`updated_at`- Audit trail for compliance
- No duplicate or contradicting memories
- Single source of truth for each fact
`infer=True``infer=False`- If using graph memory, connections to other entities persist

### ​Pick the right inference mode
[​](https://docs.mem0.ai/cookbooks/essentials/controlling-memory-ingestion#pick-the-right-inference-mode)`infer=True``infer=False``infer=True``app_id``run_id`
## ​Update vs Delete
[​](https://docs.mem0.ai/cookbooks/essentials/controlling-memory-ingestion#update-vs-delete)
### ​Update when:
[​](https://docs.mem0.ai/cookbooks/essentials/controlling-memory-ingestion#update-when%3A)- Information changes but remains relevant
- You need audit history
- The memory has relationships to other data

```
# Medication dosage changed
client.update(
    memory_id=med_id,
    text="Taking Lisinopril 20mg daily (increased from 10mg on March 1st)"
)


```

### ​Delete when:
[​](https://docs.mem0.ai/cookbooks/essentials/controlling-memory-ingestion#delete-when%3A)- Information was completely wrong
- Memory is no longer relevant
- Duplicate entry

```
# Duplicate entry
client.delete(memory_id)


```

## ​Putting It Together
[​](https://docs.mem0.ai/cookbooks/essentials/controlling-memory-ingestion#putting-it-together)
```
from mem0 import MemoryClient
import os

# Initialize client
client = MemoryClient(api_key=os.getenv("MEM0_API_KEY"))

# Configure custom instructions
client.project.update(
    custom_instructions="""
Medical memory assistant rules:

STORE:
- Confirmed diagnoses (with doctor name and date)
- Verified allergies (with reaction details)
- Current medications (with dosage)

IGNORE:
- Speculation (might, maybe, possibly)
- Unverified symptoms
- Personal identifiers (SSN, insurance numbers)

CONFIDENCE:
Require high confidence. Reject vague or uncertain statements.
Require specific details: names, dates, dosages.
"""
)

# Helper function for safe ingestion
def add_medical_memory(content, user_id, metadata=None):
    """Add memory with automatic filtering."""
    result = client.add(
        [{"role": "user", "content": content}],
        user_id=user_id,
        metadata=metadata or {}
    )

    if result['results']:
        print(f"✓ Stored: {result['results'][0]['memory']}")
    else:
        print(f"✗ Filtered: {content}")

    return result

# Test cases
print("Testing ingestion pipeline:\\n")

test_cases = [
    "I think I might be allergic to penicillin",
    "Dr. Johnson confirmed penicillin allergy on Jan 15th with hives reaction",
    "Patient SSN is 123-45-6789",
    "Currently taking Lisinopril 10mg daily for hypertension",
    "Feeling tired lately",
    "Dr. Martinez diagnosed Type 2 diabetes on February 3rd, 2025"
]

for content in test_cases:
    add_medical_memory(content, user_id="patient_123")
    print()


```

```
Testing ingestion pipeline:

✗ Filtered: I think I might be allergic to penicillin

✓ Stored: Patient has confirmed penicillin allergy diagnosed by Dr. Johnson on January 15th with hives reaction

✗ Filtered: Patient SSN is 123-45-6789

✓ Stored: Patient is currently taking Lisinopril 10mg daily for hypertension

✗ Filtered: Feeling tired lately

✓ Stored: Patient diagnosed with Type 2 diabetes by Dr. Martinez on February 3rd, 2025


```

## ​Per-Call Instructions
[​](https://docs.mem0.ai/cookbooks/essentials/controlling-memory-ingestion#per-call-instructions)
```
custom_instructions="""Emergency intake mode:Store ALL symptoms and observations immediately.
Flag for later review and verification."""
 

```

```
# Emergency intake - store everything temporarily
emergency_messages = [
    {"role": "user", "content": "Patient arrived with chest pain and shortness of breath"}
]

client.add(
    emergency_messages,
    user_id="patient_456",
    custom_instructions=custom_instructions,
    metadata={"type": "emergency", "review_required": True}
)


```
- Different conversation types (emergency vs routine)
- Channel-specific rules (phone vs in-person)
- Temporary data collection that needs review

## ​What You Built
[​](https://docs.mem0.ai/cookbooks/essentials/controlling-memory-ingestion#what-you-built)- Custom instructions- Filter speculation and enforce confirmed facts only
- Confidence thresholds- Gate extractions below 0.7 confidence score
- Memory updates- Modify stored information without creating duplicates
- Per-call instructions- Apply temporary rules for specific conversations
- PII filtering- Block sensitive data (SSNs, insurance numbers) automatically

## ​Summary
[​](https://docs.mem0.ai/cookbooks/essentials/controlling-memory-ingestion#summary)[Expire Short-Term DataAutomatically clean up session context before it clutters retrieval.](https://docs.mem0.ai/cookbooks/essentials/memory-expiration-short-and-long-term)
## Expire Short-Term Data
[Choose Your Memory ArchitectureLearn when to layer graph memory alongside vectors for multi-hop queries.](https://docs.mem0.ai/cookbooks/essentials/choosing-memory-architecture-vector-vs-graph)
## Choose Your Memory Architecture
