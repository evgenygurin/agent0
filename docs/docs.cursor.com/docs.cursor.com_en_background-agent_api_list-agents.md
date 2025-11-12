# List Agents

> Retrieve a paginated list of all background agents for the authenticated user.

## OpenAPI

````yaml en/background-agent/api/openapi.yaml get /v0/agents
paths:
  path: /v0/agents
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
      query:
        limit:
          schema:
            - type: integer
              required: false
              description: Number of background agents to return
              maximum: 100
              minimum: 1
              default: 20
        cursor:
          schema:
            - type: string
              required: false
              description: Pagination cursor from the previous response
              minLength: 1
              example: bc_xyz789
      header: {}
      cookie: {}
    body: {}
  response:
    '200':
      application/json:
        schemaArray:
          - type: object
            properties:
              agents:
                allOf:
                  - type: array
                    description: List of agents
                    items:
                      type: object
                      required:
                        - id
                        - name
                        - status
                        - source
                        - target
                        - createdAt
                      properties:
                        id:
                          type: string
                          description: Unique identifier for the background agent
                          example: bc_abc123
                        name:
                          type: string
                          description: Name for the agent
                          example: Add README Documentation
                        status:
                          type: string
                          enum:
                            - RUNNING
                            - FINISHED
                            - ERROR
                            - CREATING
                            - EXPIRED
                          description: Current status of the background agent
                          example: RUNNING
                        source:
                          type: object
                          properties:
                            repository:
                              type: string
                              description: The GitHub repository URL
                              example: https://github.com/your-org/your-repo
                            ref:
                              type: string
                              description: Git ref (branch/tag) used as the base branch
                              example: main
                        target:
                          type: object
                          required:
                            - url
                          properties:
                            branchName:
                              type: string
                              description: The Git branch name where the agent is working
                              example: cursor/add-readme-1234
                            url:
                              type: string
                              description: URL to view the agent in Cursor Web
                              example: https://cursor.com/agents?id=bc_abc123
                            prUrl:
                              type: string
                              description: URL to view the pull request in GitHub, if any
                              example: https://github.com/your-org/your-repo/pull/1234
                            autoCreatePr:
                              type: boolean
                              description: >-
                                Whether a pull request will be automatically
                                created
                              example: false
                        summary:
                          type: string
                          description: Summary of the agent's work
                          example: >-
                            Added README.md with installation instructions and
                            usage examples
                        createdAt:
                          type: string
                          format: date-time
                          description: When the agent was created
                          example: '2024-01-15T10:30:00Z'
              nextCursor:
                allOf:
                  - type: string
                    description: Cursor for fetching the next page of results
                    example: bc_def456
            requiredProperties:
              - agents
        examples:
          example:
            value:
              agents:
                - id: bc_abc123
                  name: Add README Documentation
                  status: RUNNING
                  source:
                    repository: https://github.com/your-org/your-repo
                    ref: main
                  target:
                    branchName: cursor/add-readme-1234
                    url: https://cursor.com/agents?id=bc_abc123
                    prUrl: https://github.com/your-org/your-repo/pull/1234
                    autoCreatePr: false
                  summary: >-
                    Added README.md with installation instructions and usage
                    examples
                  createdAt: '2024-01-15T10:30:00Z'
              nextCursor: bc_def456
        description: Agents retrieved successfully
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
        description: Invalid request - bad query parameters
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