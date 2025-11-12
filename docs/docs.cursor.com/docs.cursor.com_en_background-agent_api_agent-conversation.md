# Agent Conversation

> Retrieve the conversation history of a background agent.

## OpenAPI

````yaml en/background-agent/api/openapi.yaml get /v0/agents/{id}/conversation
paths:
  path: /v0/agents/{id}/conversation
  method: get
  servers:
    - url: https://api.cursor.com
      description: Production server
  request:
    security:
      - title: bearerAuth
        parameters:
          query: {}
          header:
            Authorization:
              type: http
              scheme: bearer
              description: API key from Cursor Dashboard
          cookie: {}
    parameters:
      path:
        id:
          schema:
            - type: string
              required: true
              description: Unique identifier for the background agent
              example: bc_abc123
      query: {}
      header: {}
      cookie: {}
    body: {}
  response:
    '200':
      application/json:
        schemaArray:
          - type: object
            properties:
              id:
                allOf:
                  - type: string
                    description: Unique identifier for the background agent
                    example: bc_abc123
              messages:
                allOf:
                  - type: array
                    description: Array of conversation messages ordered chronologically
                    items:
                      type: object
                      required:
                        - id
                        - type
                        - text
                      properties:
                        id:
                          type: string
                          description: Unique identifier for the message
                          example: msg_123
                        type:
                          type: string
                          enum:
                            - user_message
                            - assistant_message
                          description: Type of message - either from the user or the model
                          example: user_message
                        text:
                          type: string
                          description: The content of the message
                          example: Add a README.md file with installation instructions
            requiredProperties:
              - id
              - messages
        examples:
          example:
            value:
              id: bc_abc123
              messages:
                - id: msg_123
                  type: user_message
                  text: Add a README.md file with installation instructions
        description: Conversation retrieved successfully
    '400':
      application/json:
        schemaArray:
          - type: object
            properties:
              error:
                allOf:
                  - &ref_0
                    type: object
                    properties:
                      message:
                        type: string
                        description: Human-readable error message
                      code:
                        type: string
                        description: Machine-readable error code
            refIdentifier: '#/components/schemas/Error'
        examples:
          example:
            value:
              error:
                message: <string>
                code: <string>
        description: Invalid request - bad agent ID format
    '401':
      application/json:
        schemaArray:
          - type: object
            properties:
              error:
                allOf:
                  - *ref_0
            refIdentifier: '#/components/schemas/Error'
        examples:
          example:
            value:
              error:
                message: <string>
                code: <string>
        description: Unauthorized - invalid or missing API key
    '403':
      application/json:
        schemaArray:
          - type: object
            properties:
              error:
                allOf:
                  - *ref_0
            refIdentifier: '#/components/schemas/Error'
        examples:
          example:
            value:
              error:
                message: <string>
                code: <string>
        description: Forbidden - insufficient permissions
    '404':
      application/json:
        schemaArray:
          - type: object
            properties:
              error:
                allOf:
                  - *ref_0
            refIdentifier: '#/components/schemas/Error'
        examples:
          example:
            value:
              error:
                message: <string>
                code: <string>
        description: Agent not found or access denied
    '409':
      application/json:
        schemaArray:
          - type: object
            properties:
              error:
                allOf:
                  - *ref_0
            refIdentifier: '#/components/schemas/Error'
        examples:
          example:
            value:
              error:
                message: <string>
                code: <string>
        description: Conflict - agent is deleted or archived
    '429':
      application/json:
        schemaArray:
          - type: object
            properties:
              error:
                allOf:
                  - *ref_0
            refIdentifier: '#/components/schemas/Error'
        examples:
          example:
            value:
              error:
                message: <string>
                code: <string>
        description: Rate limit exceeded
    '500':
      application/json:
        schemaArray:
          - type: object
            properties:
              error:
                allOf:
                  - *ref_0
            refIdentifier: '#/components/schemas/Error'
        examples:
          example:
            value:
              error:
                message: <string>
                code: <string>
        description: Internal server error
  deprecated: false
  type: path
components:
  schemas: {}

````