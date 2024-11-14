# backend/app/routes.py
from flask import Blueprint, jsonify

main = Blueprint('main', __name__)

@main.route('/')
def home():
    return "Hello, World!"  # Home page route

@main.route('/api', methods=['GET'])
def get_data():
    return jsonify({"message": "Hello from Flask backend!"})
