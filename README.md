# Simple Welcome Web Application

## Overview
A minimal Flask web application that displays a welcome message when accessing the home page.

## Story: KAN-124
**Summary:** Develop a Simple Welcome Web Application

**Description:** Develop a minimal web application that displays a welcome message when a user accesses the application's home page. The application exposes a single endpoint (`/`) which returns the message **"Hello Neurostack User"** in the browser.

## Acceptance Criteria
- ✅ The application starts successfully without errors
- ✅ Navigating to `http://localhost:5000/` displays **"Hello Neurostack User"**
- ✅ The endpoint returns an HTTP **200 OK** response
- ✅ No additional pages or APIs are required

## Technology Stack
- **Language:** Python 3.11+
- **Framework:** Flask 3.x
- **Database:** SQLite (for future extensibility)
- **ORM:** Flask-SQLAlchemy 3.x
- **WSGI Server:** Gunicorn 26.x

## Project Structure
```
.
├── requirements.txt       # Python dependencies
├── .env                   # Environment variables (local)
├── .env.example           # Environment variables template
├── .gitignore             # Git ignore rules
├── README.md              # This file
├── config.py              # Application configuration
├── app.py                 # Application factory
├── routes/
│   ├── __init__.py
│   └── welcome_routes.py  # Welcome endpoint
└── services/
    ├── __init__.py
    └── welcome_service.py # Business logic
```

## Setup Instructions

### 1. Clone the repository
```bash
git clone https://github.com/parth-vadodaria-itp/neurostack_sdlc_workflow_tmp_repo_1.git
cd neurostack_sdlc_workflow_tmp_repo_1
```

### 2. Create a virtual environment
```bash
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### 3. Install dependencies
```bash
pip install -r requirements.txt
```

### 4. Configure environment variables
```bash
cp .env.example .env
# Edit .env if needed (defaults work for local development)
```

### 5. Run the application
```bash
python app.py
```

The application will start on `http://localhost:5000/`

### 6. Test the endpoint
Open your browser and navigate to:
```
http://localhost:5000/
```

You should see:
```
Hello Neurostack User
```

## Production Deployment

### Using Gunicorn
```bash
gunicorn --bind 0.0.0.0:5000 --workers 4 "app:create_app()"
```

### Using Docker (optional)
Create a `Dockerfile`:
```dockerfile
FROM python:3.11-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY . .
EXPOSE 5000
CMD ["gunicorn", "--bind", "0.0.0.0:5000", "--workers", "4", "app:create_app()"]
```

Build and run:
```bash
docker build -t welcome-app .
docker run -p 5000:5000 welcome-app
```

## API Documentation

### GET /
Returns a welcome message.

**Response:**
- **Status Code:** 200 OK
- **Content-Type:** text/plain
- **Body:** `Hello Neurostack User`

**Example:**
```bash
curl http://localhost:5000/
# Output: Hello Neurostack User
```

## Development

### Running in debug mode
The `.env` file sets `FLASK_DEBUG=1` by default for local development.

### Adding new endpoints
1. Create a new route file in `routes/`
2. Create corresponding service in `services/`
3. Register the blueprint in `app.py`

## Testing

### Manual testing
```bash
# Start the application
python app.py

# In another terminal
curl http://localhost:5000/
```

Expected output: `Hello Neurostack User`

## Troubleshooting

### Port already in use
If port 5000 is already in use, change the `PORT` value in `.env`:
```
PORT=8000
```

### Module not found errors
Ensure virtual environment is activated and dependencies are installed:
```bash
source venv/bin/activate
pip install -r requirements.txt
```

## License
MIT

## Contact
For questions or issues, please contact the development team.