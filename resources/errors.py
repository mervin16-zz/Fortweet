class InternalServerError(Exception):
    pass

class SchemaValidationError(Exception):
    pass

class UnauthorizedError(Exception):
    pass

errors = {
    "InternalServerError": {
        "message": "Something went wrong",
        "status": 500
    },
     "SchemaValidationError": {
         "message": "Request is missing fields",
         "status": 400
     },
     "UnauthorizedError": {
         "message": "You are not authorized to proceed",
         "status": 401
     }
}