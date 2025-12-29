# Little Lemon Django Project

This project is developed as part of the **Full-Stack Django Web Development Course** offered by **Coursera**. The goal is to build a restaurant web application for **Little Lemon**, implementing full-stack functionality using Django and SQLite.

## 🚀 Project Overview

The Little Lemon project simulates a restaurant management system with key features such as:

- Customer reservations
- Menu management
- Order tracking
- Backend admin interface

## 🛠️ Technologies Used

- **Python** (Django Framework)
- **SQLite** (Database)
- **HTML/CSS** (Templates)
- **Bootstrap** (UI styling)
- **Django Admin** (Backend management)

## 📁 Project Structure

littlelemon/
├── littlelemon/ # Django project configuration
│ ├── settings.py
│ └── urls.py
├── reservations/ # Django app for managing bookings
├── menu/ # Django app for menu items
├── db.sqlite3 # SQLite database
└── manage.


## 🧪 How to Run the Project

1. Clone the repository:
   ```bash
   git clone <your-repo-url>
   cd littlelemon
python -m venv env
source env/bin/activate   # On Windows: env\Scripts\activate

pip install -r requirements.txt

python manage.py migrate

python manage.py runserver




🔒 Admin Panel Access
To access the Django Admin:

python manage.py createsuperuser
Then log in at: http://127.0.0.1:8000/admin/



