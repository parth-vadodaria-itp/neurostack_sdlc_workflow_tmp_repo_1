# Simple Welcome Web Application

## Overview
A minimal Flask web application that displays a welcome message when accessing the home page.

## Story Details
- **Story ID:** KAN-124
- **Summary:** Develop a Simple Welcome Web Application
- **Endpoint:** `GET /` returns "Hello Neurostack User"

## Requirements
- Python 3.11+
- Flask 3.x

## Installation

### 1. Clone the repository
```bash
git clone https://github.com/parth-vadodaria-itp/neurostack_sdlc_workflow_tmp_repo_1.git
cd neurostack_sdlc_workflow_tmp_repo_1
```

### 2. Create virtual environment
```bash
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### 3. Install dependencies
```bash
pip install -r requirements.txt
```

### 4. Configure environment
```bash
cp .env.example .env
# Edit .env if needed
```

## Running the Application

### Development Mode
```bash
flask run
```

Or using Python directly:
```bash
python app.py
```

### Production Mode
```bash
gunicorn --bind 0.0.0.0:5000 --workers 4 "app:create_app()"
```

### Using Docker
```bash
docker-compose up --build
```

## Testing

Once the application is running, navigate to:
```
http://localhost:5000/
```

You should see:
```
Hello Neurostack User
```

## API Endpoints

### GET /
- **Description:** Returns welcome message
- **Response:** Plain text "Hello Neurostack User"
- **Status Code:** 200 OK

### GET /health
- **Description:** Health check endpoint
- **Response:** JSON with status
- **Status Code:** 200 OK

## Project Structure
```
.
├── app.py                      # Flask application factory
├── config.py                   # Configuration classes
├── requirements.txt            # Python dependencies
├── .env                        # Environment variables (not in git)
├── .env.example                # Environment template
├── .gitignore                  # Git ignore rules
├── Dockerfile                  # Container definition
├── docker-compose.yml          # Docker orchestration
├── README.md                   # This file
├── routes/
│   ├── __init__.py            # Routes package
│   └── welcome_routes.py      # Welcome endpoint blueprint
└── services/
    ├── __init__.py            # Services package
    └── welcome_service.py     # Welcome message service
```

## Acceptance Criteria
- ✅ The application starts successfully without errors
- ✅ Navigating to `http://localhost:5000/` displays "Hello Neurostack User"
- ✅ The endpoint returns an HTTP 200 OK response
- ✅ No additional pages or APIs are required

## Technology Stack
- **Language:** Python 3.11
- **Framework:** Flask 3.x
- **WSGI Server:** Gunicorn 26.x
- **Package Manager:** pip

## License
MIT
