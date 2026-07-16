from flask import Blueprint, jsonify

welcome_bp = Blueprint('welcome', __name__)

@welcome_bp.route('/', methods=['GET'])
def welcome():
    """Welcome endpoint that returns a greeting message.
    
    Returns:
        Response: JSON response with welcome message and HTTP 200 status
    
    Acceptance Criteria:
        - Navigating to http://localhost:5000/ displays "Hello Neurostack User"
        - The endpoint returns an HTTP 200 OK response
    """
    return jsonify({'message': 'Hello Neurostack User'}), 200
