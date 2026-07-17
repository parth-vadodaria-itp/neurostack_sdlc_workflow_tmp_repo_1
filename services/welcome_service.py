class WelcomeService:
    """Service for handling welcome message logic."""

    def get_welcome_message(self):
        """Returns the welcome message.
        
        Returns:
            str: The welcome message 'Hello Neurostack User'.
        """
        return "Hello Neurostack User"

    def get_health_status(self):
        """Returns application health status.
        
        Returns:
            dict: Health status information.
        """
        return {
            "status": "healthy",
            "service": "welcome-app",
            "version": "1.0.0"
        }
