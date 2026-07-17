import os
from flask import Flask
from config import config

def create_app(env='default'):
    """Application factory pattern."""
    app = Flask(__name__)
    app.config.from_object(config[env])

    # Register blueprints
    from routes.welcome_routes import welcome_bp
    app.register_blueprint(welcome_bp)

    # Error handlers
    @app.errorhandler(404)
    def not_found(error):
        return {'error': 'Not found'}, 404

    @app.errorhandler(500)
    def internal_error(error):
        return {'error': 'Internal server error'}, 500

    return app

if __name__ == '__main__':
    app = create_app(os.getenv('FLASK_ENV', 'default'))
    port = int(os.getenv('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
