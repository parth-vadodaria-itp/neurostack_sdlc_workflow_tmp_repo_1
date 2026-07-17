import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from config import config

db = SQLAlchemy()
migrate = Migrate()

def create_app(env='default'):
    """Application factory pattern."""
    app = Flask(__name__)
    app.config.from_object(config[env])
    
    db.init_app(app)
    migrate.init_app(app, db)
    
    from routes.welcome_routes import welcome_bp
    app.register_blueprint(welcome_bp)
    
    @app.errorhandler(404)
    def not_found(error):
        return {'error': 'Resource not found'}, 404
    
    @app.errorhandler(500)
    def internal_error(error):
        return {'error': 'Internal server error'}, 500
    
    return app

if __name__ == '__main__':
    env = 'development' if os.getenv('FLASK_DEBUG', '0') == '1' else 'production'
    app = create_app(env)
    port = int(os.getenv('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=(env == 'development'))