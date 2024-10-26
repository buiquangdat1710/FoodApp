# FoodApp 🍲

A web application for discovering, managing, and ordering delicious meals. Built with Django, FoodApp provides an interactive and user-friendly experience for users to explore various food options, manage their orders, and browse recipes.

## Table of Contents
1. [Project Description](#project-description)
2. [Installation and Setup](#installation-and-setup)
3. [Usage](#usage)
4. [Credits](#credits)
5. [License](#license)
6. [Badges](#badges)
7. [Contributing](#contributing)
8. [Running Tests](#running-tests)

---

## Project Description

**FoodApp** is a food ordering and management application built with Django. It provides users with a platform to explore different types of foods, view recipes, and place orders. The project also includes an admin interface for managing food items, orders, and users.

Key features include:
- User registration and authentication
- Browse and search for food items
- Add food items to the cart
- Place orders
- Admin panel for managing food items, orders, and user data

## Installation and Setup

Follow these steps to install and set up the FoodApp project on your local machine.

### Prerequisites
Ensure you have the following installed on your machine:
- Python 3.x
- Django
- Virtualenv (recommended)

### Steps

1. **Clone the repository**:
   ```bash
   git clone https://github.com/buiquangdat1710/FoodApp.git
   cd mysite
   ```
2. **Set up a virtual environment**:
  ```bash
  python3 -m venv env
  source env/bin/activate
  ```

3. **Install dependencies**:
```bash
pip install -r requirements.txt
```

4. **Set up the database:**
```bash
python manage.py migrate
```
5. **Create a superuser for the admin panel:**
```bash
python manage.py createsuperuser
```
6. **Run the development server:**
```bash
python manage.py runserver
```
7. **Access the application:**
8. Open a web browser and go to *http://127.0.0.1:8000*.

## Usage

### User Guide

1. **Registration and Login**:
   - Go to the registration page to create an account.
   - Once registered, log in to start exploring the food items available.

2. **Browse Food Items**:
   - View a list of available foods and recipes.
   - Use the search function to find specific dishes.

3. **Add to Cart and Place Order**:
   - Add items to your cart.
   - Review the items in your cart and place your order.

4. **Admin Panel**:
   - Visit `http://127.0.0.1:8000/admin` to access the admin panel.
   - Log in with the superuser credentials created during setup.
   - From the admin panel, you can manage food items, orders, and user accounts.

## Credits

- **Django** - [Django](https://www.djangoproject.com/) is a high-level Python web framework that encourages rapid development and clean, pragmatic design.
- **Font Awesome** - Icons used in the project are from [Font Awesome](https://fontawesome.com/).
- **Other Contributors** - Thanks to everyone who contributed to this project.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Badges

![Django](https://img.shields.io/badge/Django-3.x-brightgreen)
![Python](https://img.shields.io/badge/Python-3.x-blue)
![License](https://img.shields.io/badge/License-MIT-yellow)

## Contributing

We welcome contributions! Please follow these steps to contribute to the project:

1. Fork the repository.
2. Create a new branch for your feature or bug fix:
   ```bash
   git checkout -b feature-name
