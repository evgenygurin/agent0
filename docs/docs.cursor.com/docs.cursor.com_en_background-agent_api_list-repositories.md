# List GitHub Repositories

> Retrieve a list of GitHub repositories accessible to the authenticated user.

## OpenAPI

````yaml en/background-agent/api/openapi.yaml get /v0/repositories
paths:
  path: /v0/repositories
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
              repositories:
                allOf:
                  - type: array
                    description: Array of GitHub repositories the user has access to
                    items:
                      type: object
                      required:
                        - owner
                        - name
                        - repository
                      properties:
                        owner:
                          type: string
                          description: The owner of the repository (user or organization)
                          example: your-org
                        name:
                          type: string
                          description: The name of the repository
                          example: your-repo
                        repository:
                          type: string
                          format: uri
                          description: The full URL to the GitHub repository
                          example: https://github.com/your-org/your-repo
            requiredProperties:
              - repositories
        examples:
          example:
            value:
              repositories:
                - owner: your-org
                  name: your-repo
                  repository: https://github.com/your-org/your-repo
        description: Repositories retrieved successfully
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