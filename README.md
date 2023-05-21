# Schedule Management System Backend

<p style="text-align: center">Work in progress</p>
<p> This is a rest api for a schedule management system. It is written in Python using the Django framework and login with JWT. It sends an email when a student or teacher is registered </p>

## Installation

1. Clone the repository
2. Install the requirements using `pip install -r requirements.txt`
3. Run the server with `python manage.py runserver`
4. The server will be running on `localhost:8000`

## API Endpoints

## Documentation
`/docs/` - CoreAPI documentation

### User

- `POST /student/register` - Register a new student
- `POST /teacher/register` - Register a new teacher
- `GET /student/` - Get a list of all students
- `GET /student/<int:pk>` - Get a student by id
- `GET /teacher/` - Get a list of all teachers
- `GET /teacher/<int:pk>` - Get a teacher by id
- `POST /token/` - Login a user and get a JWT token
- `GET /token/refresh` - Refresh a JWT token
- `POST /logout/` - Logout a user and blacklist the JWT token

### Schedule

- `GET /career/` - Get a list of all careers
- `POST /career/` - Register a new career
- `GET /career/<int:pk>` - Get a career by id
- `GET /subject/` - Get a list of all subjects
- `POST /subject/` - Register a new subject
- `GET /subject/<int:pk>` - Get a subject by id
- `GET /classroom/` - Get a list of all classrooms
- `POST /classroom/` - Register a new classroom
- `GET /classroom/<int:pk>` - Get a classroom by id
- `GET /course/` - Get a list of all courses
- `POST /course/` - Register a new course
- `GET /course/<int:pk>` - Get a course by id
- `GET /enrollment/` - Get a list of all enrollments
- `GET /enrollment/<int:pk>` - Get a enrollment by id
- `GET /schedule/` - Get a list of all schedules
- `POST /schedule/` - Register a new schedule
