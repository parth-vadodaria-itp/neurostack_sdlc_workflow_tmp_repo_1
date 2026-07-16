# Simple Welcome Web Application

## Description
A minimal Flask web application that displays a welcome message when accessing the home page.

## Story
**Story ID:** KAN-124  
**Summary:** Develop a Simple Welcome Web Application

## Features
- Single endpoint (`/`) that returns "Hello Neurostack User"
- Returns HTTP 200 OK response
- Runs on port 5000

## Technology Stack
- **Language:** Python 3.11
- **Framework:** Flask 3.x
- **Database:** SQLite (configured but not used for this minimal app)
- **ORM:** Flask-SQLAlchemy 3.x
- **Package Manager:** pip

## Setup Instructions

### Prerequisites
- Python 3.11 or higher
- pip

### Installation

1. Clone the repository:
```bash
git clone https://github.com/parth-vadodaria-itp/neurostack_sdlc_workflow_tmp_repo_1.git
cd neurostack_sdlc_workflow_tmp_repo_1
```

2. Create a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Set up environment variables:
```bash
cp .env.example .env
```

5. Run the application:
```bash
python app.py
```

The application will start on `http://localhost:5000/`

## Usage

Navigate to `http://localhost:5000/` in your browser. You should see:
```
Hello Neurostack User
```

## Acceptance Criteria
- ✅ The application starts successfully without errors
- ✅ Navigating to `http://localhost:5000/` displays "Hello Neurostack User"
- ✅ The endpoint returns an HTTP 200 OK response
- ✅ No additional pages or APIs are required

## Project Structure
```
.
├── requirements.txt       # Python dependencies
├── .env                   # Environment variables (not in git)
├── .env.example          # Example environment variables
├── .gitignore            # Git ignore rules
├── README.md             # This file
├── config.py             # Application configuration
├── app.py                # Application entry point
└── routes/
    ├── __init__.py       # Routes package initializer
    └── home_routes.py    # Home route handler
```

## Development

To run in development mode with debug enabled:
```bash
export FLASK_DEBUG=1  # On Windows: set FLASK_DEBUG=1
python app.py
```

## Production Deployment

For production, use gunicorn:
```bash
gunicorn --bind 0.0.0.0:5000 --workers 4 "app:create_app()"
```

## License
This project is part of the Kanban Board project (KAN).
