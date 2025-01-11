import re

MIN_USERNAME_LENGTH = 3
MAX_USERNAME_LENGTH = 32

MIN_PASSWORD_LENGTH = 8
MAX_PASSWORD_LENGTH = 64

MIN_EMAIL_LENGTH = 8
MAX_EMAIL_LENGTH = 255
EMAIL_PATTERN = "(?:[a-z0-9!#$%&'*+/=?^_`{|}~-]+(?:\\.[a-z0-9!#$%&'*+/=?^_`{|}~-]+)*|\"(?:[\\x01-\\x08\\x0b\\x0c\\x0e-\\x1f\\x21\\x23-\\x5b\\x5d-\\x7f]|\\\\[\\x01-\\x09\\x0b\\x0c\\x0e-\\x7f])*\")@(?:(?:[a-z0-9](?:[a-z0-9-]*[a-z0-9])?\\.)+[a-z0-9](?:[a-z0-9-]*[a-z0-9])?|\\[(?:(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\\.){3}(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?|[a-z0-9-]*[a-z0-9]:(?:[\\x01-\\x08\\x0b\\x0c\\x0e-\\x1f\\x21-\\x5a\\x53-\\x7f]|\\\\[\\x01-\\x09\\x0b\\x0c\\x0e-\\x7f])+)\\])"

def validate_username_field(username):
    """
    Validate the username field.

    Args:
        username: The username to validate.

    Returns:
        - An error message if the username is invalid.
        - None if the username is valid.
    """

    # Check if the username is empty.
    if not username:
        return "Username field is required."

    # Validate the length of the requested username.
    if len(username) < MIN_USERNAME_LENGTH:
        return f'Username must be at least {MIN_USERNAME_LENGTH} characters.'
    if len(username) > MAX_USERNAME_LENGTH:
        return f'Username must be less than {MAX_USERNAME_LENGTH} characters.'

    # Validate the format of the username.
    if not username.isalnum():
        return 'Invalid username format.'

    # Return None if the username is valid.
    return None


def validate_email_field(email):
    """
    Validate the email field.

    Args:
        email: The email to validate.

    Returns:
        - An error message if the email is invalid.
        - None if the email is valid.
    """

    # Check if the email is empty.
    if not email:
        return 'Email field is required.'

    # Validate the length of the requested email.
    if len(email) < MIN_EMAIL_LENGTH:
        return f'Email must be at least {MIN_EMAIL_LENGTH} characters.'
    if len(email) > MAX_EMAIL_LENGTH:
        return f'Email must be less than {MAX_EMAIL_LENGTH} characters.'

    # Validate the format of the email.
    if not re.match(EMAIL_PATTERN, email, re.IGNORECASE):
        return 'Invalid email format.'

    # Return None if the email is valid.
    return None


def validate_password_field(password):
    """
    Validate the password field.

    Args:
        password: The password to validate.

    Returns:
        - An error message if the password is invalid.
        - None if the password is valid.
    """

    # Check if the password is empty.
    if not password:
        return 'Password field is required.'

    # Validate the length of the requested password.
    if len(password) < MIN_PASSWORD_LENGTH:
        return f'Password must be at least {MIN_PASSWORD_LENGTH} characters.'
    if len(password) > MAX_PASSWORD_LENGTH:
        return f'Password must be less than {MAX_PASSWORD_LENGTH} characters.'

    # Return None if the password is valid.
    return None


def is_potential_email(credential):
    """
    Check if the credential is a potential email address.

    Args:
        credential: The credential to check.

    Returns:
        - True if the credential is a potential email address.
        - False if the credential is not a potential email address.
    """

    return '@' in credential