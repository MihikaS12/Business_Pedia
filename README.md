





# BusinessPedia 🧠💼

**BusinessPedia** is a simple Python and MySQL-based tool for managing business-related information. It works like a small encyclopedia where users can add, view, update, and delete business data through a terminal interface. The project is especially useful for those just starting out with databases and Python programming.

---

## 📘 Overview

Managing structured business data doesn't have to be complex. BusinessPedia provides a straightforward way to store and interact with business records using a MySQL database and a basic Python CLI. It's a good hands-on project for anyone learning how to connect Python with SQL databases.

---

## 🔧 Tech Stack

- **Python** – handles the program logic and user interactions
- **MySQL** – stores business information
- **mysql-connector-python** – used to connect Python with the MySQL database

---

## 🎯 Features

- Add new business entries (like name, type, and location)
- Search and view saved businesses
- Edit existing records
- Delete records from the database
- Simple command-line interface
- Good for learning CRUD (Create, Read, Update, Delete) with Python and SQL

---

## 🗂 When to Use

- For small academic or personal projects
- To practice Python-MySQL integration
- As a base for building more advanced systems later

---

## 🚀 Getting Started

###  Install Required Library
```bash
pip install mysql-connector-python
Set Up the MySQL Database
Run the schema.sql file in your MySQL environment to create the required tables.

Ensure your MySQL server is running.

 Configure the Database Connection
Open db_config.py and enter your MySQL host, username, password, and database name.

 Run the Application


python main.py
📂 Project Structure
businesspedia/
├── main.py                # Main script to run the app
├── db_config.py           # Contains MySQL credentials
├── business_operations.py # Handles database operations
├── schema.sql             # SQL setup file for the DB
└── README.md              # Project info
