# Add Follow-up

> Send an additional instruction to a running background agent.

## OpenAPI

````yaml en/background-agent/api/openapi.yaml post /v0/agents/{id}/followup
paths:
  path: /v0/agents/{id}/followup
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
                        description: The followup instruction for the agent
                        example: Also add a section about troubleshooting
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
            required: true
            requiredProperties:
              - prompt
        examples:
          example:
            value:
              prompt:
                text: Also add a section about troubleshooting
                images:
                  - data: iVBORw0KGgoAAAANSUhEUgAA...
                    dimension:
                      width: 1024
                      height: 768
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
            requiredProperties:
              - id
        examples:
          example:
            value:
              id: bc_abc123
        description: Followup added successfully
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
        description: Invalid request - bad agent ID format or invalid request body
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