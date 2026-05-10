# To-Do List (Django)

A beginner-friendly, modern To-Do web app built with Django. It supports adding, editing, completing, and deleting tasks, plus a dedicated page to review all tasks and view stats.

## Features

- Add new tasks with a title
- Mark tasks complete/incomplete
- Edit task titles
- Delete tasks
- Stats: total, completed, not completed
- Separate "All Tasks" page
- Responsive, modern UI

## Tech Stack

- Python
- Django
- HTML/CSS (with a small JavaScript helper for checkbox toggles)
- SQLite (default Django database)

## Project Structure

```
manage.py
todo_project/
    settings.py
    urls.py
    wsgi.py
    asgi.py
tasks/
    migrations/
    templates/
        tasks/
            index.html
            all_tasks.html
            edit.html
    static/
        tasks/
            style.css
    models.py
    views.py
    urls.py
    admin.py
```

## Setup

From the project root:

```bash
python -m venv .venv
source .venv/bin/activate
pip install django
```

## Database

```bash
python manage.py makemigrations
python manage.py migrate
```

## Run the Server

```bash
python manage.py runserver
```

Open http://127.0.0.1:8000/ in your browser.

## Pages and Routes

- Home (add task and stats): `/`
- All tasks page: `/all/`
- Edit task: `/edit/<id>/`
- Toggle task: `/toggle/<id>/` (POST)
- Delete task: `/delete/<id>/` (POST)

## Notes

- Tasks are hidden on the home page. Use the "See All Tasks" button to view and manage them.
- The app uses Django messages for friendly feedback on actions.

## Optional Improvements

- Search and filters
- Due dates
- User accounts and authentication
- Dark mode
