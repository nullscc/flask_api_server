from . import user 
from app.services.user import UserService

@user.route("/login", methods=["POST"])
def user_login():
    s = UserService()
    s.login()
    return s.render()

@user.route("/info")
def user_info():
    s = UserService()
    s.get_info()
    return s.render()

@user.route("/logout", methods=["POST"])
def user_logout():
    s = UserService()
    s.logout()
    return s.render()
