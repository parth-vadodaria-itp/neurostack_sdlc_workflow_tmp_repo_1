from flask import Blueprint

home_bp = Blueprint('home', __name__)

@home_bp.route('/', methods=['GET'])
def welcome():
    """Return welcome message.
    
    Returns:
        str: Welcome message with HTTP 200 status
    """
    return 'Hello Neurostack User', 200
