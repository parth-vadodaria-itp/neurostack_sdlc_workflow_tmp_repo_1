from flask import Blueprint
from services.welcome_service import WelcomeService

welcome_bp = Blueprint('welcome', __name__)
welcome_service = WelcomeService()

@welcome_bp.route('/', methods=['GET'])
def get_welcome():
    """GET / - Returns welcome message.
    
    Returns:
        str: Welcome message with 200 status code
    """
    message = welcome_service.get_welcome_message()
    return message, 200