# Todo Project

A full-stack Todo application built with Django (backend) and React (frontend).

## Features
- Add, view, and toggle tasks
- Modern UI/UX with dark/light mode
- REST API powered by Django REST Framework
- CORS enabled for frontend-backend communication

## Project Structure
```
├── settings.py
├── urls.py
├── task-app/
│   ├── package.json
│   ├── README.md
│   ├── public/
│   └── src/
├── tasks/
│   ├── models.py
│   ├── serializers.py
│   ├── urls.py
│   └── views.py
```

## Getting Started

### Backend (Django)
1. Install dependencies:
   ```
   pip install -r requirements.txt
   ```
2. Apply migrations:
   ```
   python manage.py makemigrations
   python manage.py migrate
   ```
3. Run the server:
   ```
   python manage.py runserver
   ```

### Frontend (React)
1. Install dependencies:
   ```
   cd task-app
   npm install
   ```
2. Start the React app:
   ```
   npm start
   ```

## API Endpoints
- `GET /tasks/` - List all tasks
- `POST /tasks/` - Add a new task
- `PATCH /tasks/<id>/` - Toggle task status

## Deployment
- Backend: Render, Railway, or Fly.io (free tiers)
- Frontend: Vercel or Netlify (free tiers)

## License
This project is licensed under the MIT License.
