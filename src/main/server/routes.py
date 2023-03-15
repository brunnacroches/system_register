from flask import request, jsonify
from .server import app
from ...views.register_view import RegisterView
from ...views.search_view import SearchRegisterView

@app.route("/register", methods=["POST"])
def register_user():
    register_view = RegisterView()

    http_response = register_view.register_user_view(request)

    return jsonify(http_response["data"]), http_response["status_code"]

@app.route("/register/name_user", methods=["POST"])
def search_user():
    search_user = SearchRegisterView()

    http_response = search_user.search_user_view(request)
    
    return jsonify(http_response["data"]), http_response["status_code"]
