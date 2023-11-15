from marshmallow import ValidationError, Schema

# def check_required_params(Schema: Schema):

#     def decorator(fn):
#         @wraps(fn)
#         def wrapper(*args, **kwargs):
#             try:
#                 Schema().validate(request.json)

#             except ValidationError as err:
#                 error = {
#                     "status": "validation error",
#                     "message": err.messages
#                 }

#                 return jsonify(error), 400

#             except Exception as err:
#                 error = {
#                     "status" : "generic error",
#                     "message": err
#                 }

#                 return jsonify(error), 400

#             return fn(*args, **kwargs)

#         return wrapper

#     return decorator


def missing_required_params(
    Schema: Schema, request_data: dict, enable_partial=False
) -> tuple[bool, dict]:
    return_data = {"status": "success", "message": "No missing required params"}

    # partial detection (ignoring required fields and enabling unknown fields) should be disabled
    missing_params = Schema().validate(request_data, partial=enable_partial)

    if missing_params:
        return_data.update(
            {
                "status": "Missing or invalid data from request",
                "message": missing_params,
            }
        )
        return True, return_data

    return False, return_data
