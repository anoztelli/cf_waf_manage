# Cloudflare Management Without Dashboard

This project provides a solution for managing Cloudflare settings without accessing the Cloudflare dashboard. It enables internal employees to perform simple redirections without needing individual Cloudflare accounts. By integrating this solution into any internally provided public web page, users can log in through a hidden login page and quickly take action through a hidden page.

## Features
- **Nginx**: Ensures first-layer security by managing traffic redirections within the server.
- **Node.js**: Keeps the public pages running.
- **Django**: Publishes hidden pages and stores user names and passwords.
- **Flask**: Allows sending requests without encountering CORS issues.

## Simple Setup
1. Run the Docker Compose file in the project directory.
2. Complete the Django superuser setup by running the following commands in another terminal within the same project directory.

### Step-by-Step Guide

1. **Find the Container ID or Name:**
   ```bash
   docker ps

1. **Access the Container:**
   ```bash
   docker exec -it my_django_app bash

1. **Apply Django Migrations:**
   ```bash
   python manage.py migrate
   
1. **Create Django Superuser:**
   ```bash
   python manage.py createsuperuser

After entering the necessary parameters, the Django library will be active, and the login page will be available.


## Recommended Configurations Before Setup
You can customize the project to your needs by editing the following files:
- `django/templates`
- `node.js/public`
- `flask_app/app.py`

For more information and inquiries, please contact us at [anoztelli.com](https://anoztelli.com).

   
