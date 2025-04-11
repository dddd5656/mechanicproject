# Mechanic Auto Repair Website

A Django-based website for an auto repair shop with appointment booking functionality.

## Features

- Responsive design
- Service showcase
- Online appointment booking
- Testimonials slider
- Mobile-friendly navigation
- Contact information
- Modern UI with animations

## Setup

1. Clone the repository:
```bash
git clone <repository-url>
cd mechanicproject
```

2. Create a virtual environment and activate it:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Run migrations:
```bash
python manage.py makemigrations
python manage.py migrate
```

5. Create a superuser (optional):
```bash
python manage.py createsuperuser
```

6. Run the development server:
```bash
python manage.py runserver
```

7. Visit http://127.0.0.1:8000/ in your browser

## Project Structure

- `website/` - Main Django app
  - `models.py` - Database models
  - `views.py` - View functions
  - `urls.py` - URL routing
- `templates/` - HTML templates
- `static/` - Static files (CSS, JavaScript, images)
  - `css/` - Stylesheets
  - `js/` - JavaScript files
  - `images/` - Image assets

## Technologies Used

- Django 5.0.2
- HTML5
- CSS3
- JavaScript (ES6+)
- SQLite (default database)

## Contributing

1. Fork the repository
2. Create a new branch
3. Make your changes
4. Submit a pull request

## License

This project is licensed under the MIT License - see the LICENSE file for details. 