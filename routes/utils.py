def create_error_response(message, status_code=400):
    """
    Utility function to create an error response.

    Args:
        message (str): Error message.
        status_code (int): HTTP status code.

    Returns:
        tuple: JSON response with error message and HTTP status code.
    """
    from flask import jsonify
    return jsonify({"error": message}), status_code
