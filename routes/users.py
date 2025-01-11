from flask import g, render_template

from main import *
from middleware import admin_required, user_required
from model.user import User


@app.route("/users/me")
@user_required
def users_me():
    user = g.user
    return render_template('user_info.html',
                           username=user.username,
                           user_id=user.id,
                           email=user.email,
                           role=user.role)


@app.route("/admin")
@admin_required
def users_admin():
    user = g.user
    users = User.query.all()
    return render_template('admin.html',
                           username=user.username,
                           user_id=user.id,
                           email=user.email,
                           role=user.role,
                           users=users)
