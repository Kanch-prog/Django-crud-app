# 🌐 Django Blogging Platform 📝

Django Blogging Platform is a web application built using Django, a high-level Python web framework. It provides a powerful and flexible foundation to create, publish, and manage blog posts on a website, offering a user-friendly content management system for bloggers.

https://github.com/Kanch-prog/Django-crud-app/assets/121807277/3042eb99-c997-4ca8-bebe-479629ede7ab

## 🚀 Getting Started

To set up the project folder, run:

```bash
django-admin startproject Django-crud-app
cd Django-crud-app
python manage.py startapp gallery

📦 Features
Product Model: A table to store blog posts with fields for name, description, image, created_at, and updated_at.
Admin Interface: Register the Product model in the admin interface for easy management.
Views: Implement views to display a list of products, detailed view, editing, and deletion functionality.
Forms: Create forms for editing products.
Templates: HTML templates to render the user interface for listing, editing, and deleting products.
URLs: Define URL patterns to map views to URLs.

🎨 Design and Layout
The project includes HTML templates styled with Bootstrap CSS for a clean and responsive design.

🚀 Deployment
Create a superuser to add data to the database:

python manage.py createsuperuser
Add images, names, and descriptions in the admin interface at http://127.0.0.1:8000/admin/.

Migrate data into the database:

python manage.py makemigrations
python manage.py migrate
Deploy the project:

python manage.py runserver
🌟 Contributors
[Kanchana Karunarathna]

📜 License
This README provides a comprehensive overview of the project, including setup instructions, featur
