# API Key Info

> Retrieve metadata about the API key used for authentication.

## OpenAPI

````yaml en/background-agent/api/openapi.yaml get /v0/me
paths:
  path: /v0/me
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
              apiKeyName:
                allOf:
                  - type: string
                    description: The name of the API key
                    example: Production API Key
              createdAt:
                allOf:
                  - type: string
                    format: date-time
                    description: When the API key was created
                    example: '2024-01-15T10:30:00Z'
              userEmail:
                allOf:
                  - type: string
                    format: email
                    description: >-
                      Email address of the user who owns the API key (if
                      available)
                    example: developer@example.com
            requiredProperties:
              - apiKeyName
              - createdAt
        examples:
          example:
            value:
              apiKeyName: Production API Key
              createdAt: '2024-01-15T10:30:00Z'
              userEmail: developer@example.com
        description: API key information retrieved successfully
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
        description: API key not found
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