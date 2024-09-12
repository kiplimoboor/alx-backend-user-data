#!/usr/bin/env python3
"""Basic Flask app"""

from flask import Flask, Response, jsonify

app = Flask(__name__)


@app.get('/', methods=['GET'])
def root() -> Response:
    """Root path for the app"""
    msg = {"message": "Bienvenue"}
    return jsonify(msg)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
