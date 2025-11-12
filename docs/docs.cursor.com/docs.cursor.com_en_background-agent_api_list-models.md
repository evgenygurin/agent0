# List Models

> Retrieve a list of recommended models for background agents.

## OpenAPI

````yaml en/background-agent/api/openapi.yaml get /v0/models
paths:
  path: /v0/models
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
      path: {}
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
              models:
                allOf:
                  - type: array
                    description: Array of available model names
                    items:
                      type: string
                      minLength: 1
                    example:
                      - claude-4-sonnet-thinking
                      - o3
                      - claude-4-opus-thinking
            requiredProperties:
              - models
        examples:
          example:
            value:
              models:
                - claude-4-sonnet-thinking
                - o3
                - claude-4-opus-thinking
        description: Models retrieved successfully
    '401':
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
        description: Unauthorized - invalid or missing API key
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