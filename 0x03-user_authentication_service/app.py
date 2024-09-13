#!/usr/bin/env python3
"""Basic Flask app"""


from flask import Flask, Response, abort, jsonify, request

from auth import Auth

app = Flask(__name__)
AUTH = Auth()


@app.route('/', methods=['GET'])
def root():
    """ root route for the api service """
    msg = {"message": "Bienvenue"}
    return jsonify(msg)


@app.route('/users', methods=['POST'])
def users():
    email = request.form['email']
    password = request.form['password']

    try:
        AUTH.register_user(email, password)
    except ValueError:
        return jsonify({"message": "email already registered"}), 400

    message = {"email": email, "message": "user created"}
    return jsonify(message)


@app.route('/sessions', methods=['POST'])
def login():
    email = request.form['email']
    password = request.form['password']

    if not AUTH.valid_login(email, password):
        abort(401)

    AUTH.create_session(email)
    return jsonify({"email": email, "message": "logged in"})


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
