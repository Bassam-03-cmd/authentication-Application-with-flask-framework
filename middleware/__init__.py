from functools import wraps

from flask import g, json
from flask_jwt_extended import get_jwt_identity, verify_jwt_in_request

from model.user import User
from routes.utils import create_error_response


def role_required(required_role):
    """
    Decorator to check the role of the user in the JWT token.
    If the user is not in the required role, it will return a 403 Forbidden error.
    Args:
        required_role: The role required to access the route.
    """

    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            verify_jwt_in_request()

            # Extract the user information from the JWT token.
            identity = get_jwt_identity()
            if identity is None:
                return create_error_response('Unauthorized access', 401)
            identity = json.loads(identity)

            # Compute the list of permissible roles allowed to access this route.
            permissible_roles = [required_role]
            if required_role == 'user':
                permissible_roles.append('admin')

            # Check if the user is in the database.
            user = User.query.filter_by(id=identity.get("id")).first()
            if user is None:
                return create_error_response('Unauthorized access', 401)

            # Check the role of the user is among the permissible roles.
            if not user.role in permissible_roles:
                return create_error_response(f'{required_role.capitalize()} access required', 401)

            # Store the user information in the global context.
            g.user = user

            # If the user is in the required role, execute the function.
            return func(*args, **kwargs)

        return wrapper

    return decorator


def admin_required(func):
    """
    Shortcut for role_required("admin")
    """
    return role_required("admin")(func)


def user_required(func):
    """
    Shorthand for role_required("user")
    """
    return role_required("user")(func)
