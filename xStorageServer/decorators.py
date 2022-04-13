from flask import request, current_app
import jsonschema
from functools import wraps


def required_schema(schema):
    def validation(func):
        @wraps(func)
        def decorated_function(*args, **kwargs):
            # check content type
            if not request.headers.get('content-type') == 'application/json':
                return {"message": "Invalid content type: %s" % request.headers.get('content-type')}, 400
            try:
                jsonschema.validate(request.json, schema)
            except jsonschema.exceptions.ValidationError as error:
                current_app.logger.error(error)
                return {"message": "Invalid content"}, 400
            return func(*args, **kwargs)
        return decorated_function
    return validation
