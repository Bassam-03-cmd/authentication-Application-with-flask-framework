from main import *
from routes.register import register_get, register_post
from routes.login import login_get, login_post
from routes.users import users_me, users_admin

# Create the database tables if they do not exist.
with app.app_context():
    db.create_all()

# Initialise the JWT manager.
jwt.init_app(app)

# Register the middlewares.
#app.before_request(middleware_load_user)

# Run the application in debug mode.
app.run(debug=True)
