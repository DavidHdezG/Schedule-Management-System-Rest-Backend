# Schedule Management System Backend
<p style="text-align: center">Work in progress</p>
<p> This is a rest api for a schedule management system. It is written in Python using the Django framework and login with JWT . </p>

## Installation
1. Clone the repository
2. Install the requirements using `pip install -r requirements.txt`
3. Run the server with `python manage.py runserver`
4. The server will be running on `localhost:8000`

## API Endpoints
### User
- `POST /student/register` - Register a new student
- `POST /teacher/register` - Register a new teacher
- `GET /student/` - Get a list of all students
- `GET /teacher/` - Get a list of all teachers
- `POST /token/` - Login a user and get a JWT token
- `GET /token/refresh` - Refresh a JWT token
### Schedule
- `GET /career/` - Get a list of all careers
- `POST /career/` - Register a new career
- `GET /subject/` - Get a list of all subjects
- `POST /subject/` - Register a new subject
