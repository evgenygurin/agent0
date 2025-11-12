# Launch an Agent

> Start a new background agent to work on your repository.

## OpenAPI

````yaml en/background-agent/api/openapi.yaml post /v0/agents
paths:
  path: /v0/agents
  method: post
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
    body:
      application/json:
        schemaArray:
          - type: object
            properties:
              prompt:
                allOf:
                  - type: object
                    required:
                      - text
                    properties:
                      text:
                        type: string
                        minLength: 1
                        description: The task or instructions for the agent to execute
                        example: Add a README.md file with installation instructions
                      images:
                        type: array
                        maxItems: 5
                        items:
                          $ref: '#/components/schemas/Image'
                        description: Optional array of base64 encoded images (max 5)
                        example:
                          - data: iVBORw0KGgoAAAANSUhEUgAA...
                            dimension:
                              width: 1024
                              height: 768
              model:
                allOf:
                  - type: string
                    minLength: 1
                    description: The LLM to use
                    example: claude-4-sonnet
              source:
                allOf:
                  - type: object
                    required:
                      - repository
                    properties:
                      repository:
                        type: string
                        minLength: 1
                        description: The GitHub repository URL
                        example: https://github.com/your-org/your-repo
                      ref:
                        type: string
                        minLength: 1
                        description: Git ref (branch/tag) to use as the base branch
                        example: main
              target:
                allOf:
                  - type: object
                    properties:
                      autoCreatePr:
                        type: boolean
                        description: >-
                          Whether to automatically create a pull request when
                          the agent completes
                        default: false
                      branchName:
                        type: string
                        minLength: 1
                        description: Custom branch name for the agent to create
                        example: feature/add-readme
              webhook:
                allOf:
                  - type: object
                    required:
                      - url
                    properties:
                      url:
                        type: string
                        format: uri
                        maxLength: 2048
                        description: >-
                          URL to receive webhook notifications about agent
                          status changes
                        example: https://example.com/webhooks/cursor-agent
                      secret:
                        type: string
                        minLength: 32
                        maxLength: 256
                        description: Secret key for webhook payload verification
                        example: your-webhook-secret-key-minimum-32-characters
            required: true
            refIdentifier: '#/components/schemas/CreateAgentRequest'
            requiredProperties:
              - prompt
              - source
        examples:
          example:
            value:
              prompt:
                text: Add a README.md file with installation instructions
                images:
                  - data: iVBORw0KGgoAAAANSUhEUgAA...
                    dimension:
                      width: 1024
                      height: 768
              model: claude-4-sonnet
              source:
                repository: https://github.com/your-org/your-repo
                ref: main
              target:
                autoCreatePr: false
                branchName: feature/add-readme
              webhook:
                url: https://example.com/webhooks/cursor-agent
                secret: your-webhook-secret-key-minimum-32-characters
  response:
    '201':
      application/json:
        schemaArray:
          - type: object
            properties:
              id:
                allOf:
                  - type: string
                    description: Unique identifier for the background agent
                    example: bc_abc123
              name:
                allOf:
                  - type: string
                    description: Name for the agent
                    example: Add README Documentation
              status:
                allOf:
                  - type: string
                    enum:
                      - CREATING
                    description: Initial status of the newly created agent
                    example: CREATING
              source:
                allOf:
                  - type: object
                    required:
                      - repository
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
                allOf:
                  - type: object
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
                      autoCreatePr:
                        type: boolean
                        description: Whether a pull request will be automatically created
                        example: false
              createdAt:
                allOf:
                  - type: string
                    format: date-time
                    description: When the agent was created
                    example: '2024-01-15T10:30:00Z'
            requiredProperties:
              - id
              - name
              - status
              - source
              - target
              - createdAt
        examples:
          example:
            value:
              id: bc_abc123
              name: Add README Documentation
              status: CREATING
              source:
                repository: https://github.com/your-org/your-repo
                ref: main
              target:
                branchName: cursor/add-readme-1234
                url: https://cursor.com/agents?id=bc_abc123
                autoCreatePr: false
              createdAt: '2024-01-15T10:30:00Z'
        description: Agent created successfully
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
        description: Invalid request
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
        description: >-
          Forbidden - insufficient permissions, plan limits exceeded, or storage
          full
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
  schemas:
    ImageDimension:
      type: object
      required:
        - width
        - height
      properties:
        width:
          type: integer
          minimum: 1
          description: Width must be a positive integer
        height:
          type: integer
          minimum: 1
          description: Height must be a positive integer
    Image:
      type: object
      required:
        - data
      properties:
        data:
          type: string
          minLength: 1
          description: Base64 encoded image data
          example: iVBORw0KGgoAAAANSUhEUgAA...
        dimension:
          $ref: '#/components/schemas/ImageDimension'

````