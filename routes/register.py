from flask import jsonify, request, render_template
from sqlalchemy import func

from main import *
from model.user import User
from routes.utils import create_error_response
from routes.validation import validate_username_field, validate_password_field, validate_email_field

@app.route("/register", methods=['GET'])
def register_get():
    return render_template("register.html")

@app.route("/register", methods=['POST'])
def register_post():
    """
    Handles user registration requests using POST method.

    Request-Body:
        - "username" (str): User's username.
        - "email" (str): User's email address.
        - "password" (str): User's password.

    Request-Response:
        - Upon successful registration, the response will contain:
            - "message" (str): Success message.
            - "user" (dict): User details.
        - Otherwise, it will return an error
    """
    # Extract the request data.
    request_data = request.json
    username = request_data.get("username")
    email = request_data.get("email")
    password = request_data.get("password")

    # Validate the username field.
    validation = validate_username_field(username) or validate_email_field(email) or validate_password_field(password)
    if validation:
        return create_error_response(validation)

    # Check if the username or email has already been used by another user.
    if User.query.filter_by(email=func.lower(email)).first():
        return create_error_response("The email is already taken.")
    if User.query.filter_by(username=func.lower(username)).first():
        return create_error_response("The username is already taken.")

    # Compute the hashed password.
    hashed_password = bcrypt.generate_password_hash(password).decode('utf-8')

    # Create and commit the user to the database.
    user = User(username, email.lower(), hashed_password)
    db.session.add(user)
    db.session.commit()

    # Return a success response.
    return jsonify({
        "message": "User registered successfully.",
        "user": user.to_response()
    }), 200
