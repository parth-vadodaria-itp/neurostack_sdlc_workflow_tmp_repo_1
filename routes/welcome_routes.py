from flask import Blueprint, jsonify
from services.welcome_service import WelcomeService

welcome_bp = Blueprint('welcome', __name__)
welcome_service = WelcomeService()

@welcome_bp.route('/', methods=['GET'])
def welcome():
    """Welcome endpoint that returns greeting message.
    
    Returns:
        Plain text response with welcome message and 200 status code.
    """
    message = welcome_service.get_welcome_message()
    return message, 200, {'Content-Type': 'text/plain; charset=utf-8'}

@welcome_bp.route('/health', methods=['GET'])
def health_check():
    """Health check endpoint.
    
    Returns:
        JSON response with health status and 200 status code.
    """
    health_status = welcome_service.get_health_status()
    return jsonify(health_status), 200
