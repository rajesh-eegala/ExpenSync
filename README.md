# ExpenSync

## Overview

The ExpenSync is a web application designed to help users manage and track their expenses efficiently. With features like adding, updating, deleting, and viewing expenses, the application offers a comprehensive solution for personal financial management. It also includes user authentication, allowing each user to maintain a personalized account for their expenses.

## About

In today's fast-paced world, keeping track of personal expenses can be challenging. The Expense Tracker aims to simplify this process by providing an easy-to-use platform where users can log and monitor their spending. Whether you're budgeting for groceries, planning a trip, or keeping an eye on entertainment expenses, this application offers the tools you need to stay on top of your finances.

The project emphasizes security and privacy, ensuring that user data is protected through secure authentication and data storage practices. With a focus on user experience, the interface is designed to be intuitive and accessible, catering to users of all technical backgrounds.

## Features

- **User Authentication**: Secure registration and login functionalities to keep user data private.
- **Add Expenses**: Users can log their expenses with detailed inputs including title, category (grocery, travel, entertainment), date, and amount.
- **Update and Delete Expenses**: Edit or remove previously added expenses to keep the records up-to-date.
- **View Expenses**: A comprehensive list of all expenses, easily accessible for review.
- **Expense Summary**: A detailed summary displaying:
  - Total number of expenses and the total amount spent.
  - Breakdown of expenses per category, showing both the number of expenses and the total amount spent in each category.

## Database

All data is securely stored in a local MySQL database, ensuring persistence and quick access.

## User Interface

The application features a clean and intuitive user interface, making it easy for users to navigate and manage their expenses. The design emphasizes simplicity and usability, with clear navigation paths and a responsive layout that adapts to different devices.

## Tech Stack

- **Frontend**: HTML, CSS, JavaScript
- **Backend**: Django
- **Database**: MySQL

## Installation and Setup

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/ExpenSync.git

2. Navigate to the project directory
    ```bash
   cd ExpenSync
    
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   
4. Set up the database:
   - Install MySQL and create a database for the project.
   - Configure the database settings in the Django settings.py file.
   - Run migrations:
     
   ```bash  
   python manage.py migrate

5. Create a superuser to access the admin panel:
    ```bash
   python manage.py createsuperuser

6. Start the server:
     ```bash
   python manage.py runserver

7. Access the application at http://127.0.0.1:8000/.

## Contribution

Contributions are welcome! If you have ideas to improve the application or encounter any issues, please submit a pull request or open an issue on the GitHub repository.
   
