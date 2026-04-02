# Arialyn Barillo — Personal Portfolio Website

ITS 305 Midterm Project | Section A

A personal portfolio website built with Django, showcasing personal information, technical skills, projects, and education. Deployed on PythonAnywhere.

---

## Live Website

https://arialyn_barillo.pythonanywhere.com

## GitHub Repository

https://github.com/arialynbarillo/portfolio

---

## Tech Stack

- Python 3.10+
- Django 4.2
- HTML / CSS (custom, no Bootstrap)
- JavaScript (vanilla)
- SQLite (development) / MySQL (production)
- PythonAnywhere (hosting)

---

## Project Structure

```
portfolio_project/
├── myportfolio/
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── portfolio/
│   ├── migrations/
│   ├── static/portfolio/
│   │   ├── css/style.css
│   │   ├── js/main.js
│   │   └── images/
│   ├── templates/portfolio/
│   │   └── index.html
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── urls.py
│   └── views.py
├── manage.py
├── requirements.txt
└── README.md
```

---

## Models

| Model | Description |
|---|---|
| `Profile` | Name, tagline, bio, career goals, contact info, photo |
| `Skill` | Skill name, proficiency level, percentage |
| `Project` | Title, description, tools used, GitHub/live links |
| `Education` | School, degree, years attended, description |
| `ContactMessage` | Messages submitted via the contact form |

---

## Setup Instructions (Local)

### 1. Clone the repository

```bash
git clone https://github.com/arialynbarillo/portfolio.git
cd portfolio
```

### 2. Create and activate a virtual environment

```bash
python -m venv venv

# Windows
venv\Scripts\activate

# macOS / Linux
source venv/bin/activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Apply migrations

```bash
python manage.py migrate
```

### 5. Create a superuser for the admin panel

```bash
python manage.py createsuperuser
```

### 6. Collect static files

```bash
python manage.py collectstatic
```

### 7. Run the development server

```bash
python manage.py runserver
```

Visit http://127.0.0.1:8000 in your browser.

---

## Admin Panel

Visit http://127.0.0.1:8000/admin and log in with your superuser credentials.

From the admin panel you can:
- Add or edit your Profile information
- Manage Skills (with proficiency percentages)
- Add, edit, or reorder Projects
- Manage Education entries
- View contact form submissions (ContactMessage)

---

## Deployment on PythonAnywhere

### 1. Sign up at pythonanywhere.com

Use the username format: `firstname_lastname`
Example: `arialyn_barillo`

### 2. Open a Bash console and clone the repo

```bash
git clone https://github.com/arialynbarillo/portfolio.git
cd portfolio
```

### 3. Create a virtual environment

```bash
mkvirtualenv --python=python3.10 portfolio-env
pip install -r requirements.txt
```

### 4. Configure the web app

- Go to the Web tab on PythonAnywhere
- Click Add a new web app
- Choose Manual configuration, Python 3.10
- Set the source code path to `/home/arialyn_barillo/portfolio`
- Set the virtualenv path to `/home/arialyn_barillo/.virtualenvs/portfolio-env`

### 5. Edit the WSGI file

In the WSGI configuration file on PythonAnywhere, replace the contents with:

```python
import os
import sys

path = '/home/arialyn_barillo/portfolio'
if path not in sys.path:
    sys.path.append(path)

os.environ['DJANGO_SETTINGS_MODULE'] = 'myportfolio.settings'

from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
```

### 6. Configure static files

In the Web tab under Static files:
- URL: `/static/`
- Directory: `/home/arialyn_barillo/portfolio/staticfiles`

### 7. Update settings for production

In `myportfolio/settings.py`:
- Set `DEBUG = False`
- Set `ALLOWED_HOSTS = ['arialyn_barillo.pythonanywhere.com']`

### 8. Run migrations and collect static files

```bash
python manage.py migrate
python manage.py collectstatic
python manage.py createsuperuser
```

### 9. Reload the web app

Click Reload in the Web tab. Your site will be live at:
https://arialyn_barillo.pythonanywhere.com

---

## Features

- Fully dynamic content managed through Django admin
- Responsive design — works on desktop, tablet, and mobile
- Contact form that saves messages to the database
- Skill bars with scroll-triggered animation
- Active nav link highlighting on scroll
- Profile photo upload support via Django admin

---

## Instructor Collaborator

GitHub username added as collaborator: natzjun2@gmail.com

---

## Author

**Arialyn Barillo**
ITS 305 — Web Development
Section A
