from flask import json, jsonify, request, render_template, make_response
from flask_jwt_extended import create_access_token, set_access_cookies
from sqlalchemy import func

from main import *
from model.user import User
from routes.utils import create_error_response
from routes.validation import validate_username_field, validate_email_field, validate_password_field, is_potential_email


@app.route('/login', methods=['GET'])
def login_get():
    return render_template('login.html')


@app.route("/login", methods=['POST'])
def login_post():
    """
    Handles user login requests using POST method.

    Validates the credentials and password before querying the database.
    Returns a JWT access token upon successful authentication.

    Request Body:
        - "credential" (str): Username or email address.
        - "password" (str): User's password.

    Request Response:
        - Upon successful login, the response will contain:
            - "access_token" (str): JWT access token.
            - "user" (dict): User details.
        - Otherwise, it will return an error message.
    """

    # Extract the request data.
    request_data = request.json
    credential = request_data.get("credential")
    password = request_data.get("password")

    # We need to check credential again here before we pass it to validate function
    # so that it produces more specific field name.
    if not credential:
        return create_error_response("Credential field is required.")

    # Check if the credential is a potential email address or a username.
    is_email = is_potential_email(credential)

    # Extract the username and email from the credential.
    email = is_email and credential
    username = not is_email and credential

    # Either email or username must be provided or something has gone wrong.
    assert email or username, "Invalid credential format."

    # Validate the email or username field.
    if is_email:
        credential_validation = validate_email_field(email)
    else:
        credential_validation = validate_username_field(username)
    if credential_validation:
        return create_error_response(credential_validation)

    # Validate the password field.
    password_validation = validate_password_field(password)
    if password_validation:
        return create_error_response(password_validation)

    # Query the database for the user or email (lowercase).
    if username:
        user = User.query.filter_by(username=func.lower(username)).first()
    else:
        user = User.query.filter_by(email=func.lower(email)).first()

    # Check the requested password against the stored password using BCrypt hashing.
    if not user or not bcrypt.check_password_hash(user.password, password):
        return create_error_response("Wrong username or password.")

    # Generate JWT access token based on user details.
    access_token = create_access_token(identity=json.dumps({
        "id": user.id,
        "role": user.role
    }))

    # Return access token and user details.
    response = make_response(jsonify({
        "access_token": access_token,
        "user": user.to_response()
    }))

    # Set the access token as a cookie in the response.
    set_access_cookies(response, access_token)
    return response, 200
