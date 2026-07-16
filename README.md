# Simple Welcome Web Application

## Overview
A minimal Flask web application that displays a welcome message when accessing the home page.

## Story
**Story ID:** KAN-124  
**Summary:** Develop a Simple Welcome Web Application

## Requirements
- Python 3.11+
- Flask 3.x

## Setup Instructions

### 1. Clone the repository
```bash
git clone https://github.com/parth-vadodaria-itp/neurostack_sdlc_workflow_tmp_repo_1.git
cd neurostack_sdlc_workflow_tmp_repo_1
```

### 2. Create a virtual environment
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### 3. Install dependencies
```bash
pip install -r requirements.txt
```

### 4. Configure environment variables
```bash
cp .env.example .env
# Edit .env if needed (defaults are fine for local development)
```

### 5. Run the application
```bash
python -m flask run
```

Or using the app directly:
```bash
python app.py
```

### 6. Access the application
Open your browser and navigate to:
```
http://localhost:5000/
```

You should see:
```
Hello Neurostack User
```

## Acceptance Criteria
✅ The application starts successfully without errors  
✅ Navigating to `http://localhost:5000/` displays "Hello Neurostack User"  
✅ The endpoint returns an HTTP 200 OK response  
✅ No additional pages or APIs are required  

## Project Structure
```
.
├── requirements.txt       # Python dependencies
├── .env                   # Environment variables (not in git)
├── .env.example          # Environment variables template
├── .gitignore            # Git ignore rules
├── README.md             # This file
├── config.py             # Configuration classes
├── app.py                # Flask application factory
└── routes/
    ├── __init__.py       # Routes package
    └── welcome_routes.py # Welcome endpoint blueprint
```

## Technology Stack
- **Language:** Python 3.11
- **Framework:** Flask 3.x
- **Package Manager:** pip
- **Server:** Flask development server (gunicorn for production)

## Development

### Running in debug mode
The `.env` file has `FLASK_DEBUG=1` enabled by default for development.

### Production deployment
```bash
gunicorn -w 4 -b 0.0.0.0:5000 'app:create_app()'
```

## License
MIT
