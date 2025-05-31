# BusinessPedia

BusinessPedia is a desktop application built with Python (Tkinter) for managing business information, including registration, search, update, and deletion of business records. It features user and admin roles, a graphical interface, and MySQL database integration. The project also contains a Node.js component (see `package.json`), but the main application is Python-based.

## Features
- User and Admin login system
- Register new users (admin/user roles)
- Add new business records
- Search businesses by various criteria
- Update and delete business records
- GUI built with Tkinter
- MySQL database backend
- Audio/visual welcome screen

## Directory Structure
```
BusinessPedia/
├── BusinessPedia/           # Main Python application
│   ├── *.py                 # Application modules
│   ├── *.ico, *.png, *.jpg  # Icons and images
│   ├── *.wav                # Audio files
│   ├── venv/                # (ignored) Python virtual environment
│   ├── __pycache__/         # (ignored) Python bytecode
│   └── .idea/               # (ignored) IDE settings
├── node_modules/            # (ignored) Node.js modules
├── package.json             # Node.js config (for future/optional use)
├── package-lock.json        # Node.js lock file
├── proj code.txt            # (legacy/backup code)
├── projcode2.txt            # (legacy/backup code)
└── README.md                # Project documentation
```

## Requirements
- Python 3.7+
- MySQL Server (with a database named `businessdb` and table `bizpedia`, and a `users` table)
- Node.js (optional, for future/extra features)

### Python Dependencies
Listed in `requirements.txt`:
- mysql-connector-python
- Pillow
- playsound

Install with:
```bash
pip install -r requirements.txt
```

## Database Setup
You must have a MySQL server running and create the following database and tables:

```sql
CREATE DATABASE businessdb;

CREATE TABLE users (
    username VARCHAR(255) PRIMARY KEY,
    password VARCHAR(255),
    usertype VARCHAR(10) -- 'admin' or 'user'
);

CREATE TABLE bizpedia (
    title VARCHAR(255),
    company VARCHAR(255),
    person VARCHAR(255),
    website VARCHAR(255),
    detail TEXT
);
```

> **Note:** Some modules reference a `policedb` and `fir` table. For BusinessPedia, ensure your code uses `businessdb` and `bizpedia` as above, or adjust as needed.

## Running the Application
Navigate to the `BusinessPedia/BusinessPedia/` directory and run:

```bash
python startbzpedia.py
```

This will launch the welcome screen and then the main application.

## Usage
- **Login:** Use the login window to sign in as a user or admin.
- **Register:** New users can register via the Register button.
- **Admin Panel:** Admins can add, update, delete, and search business records.
- **User Panel:** Users can search for businesses by title, person, or company.

## Contribution
1. Fork this repository
2. Create your feature branch (`git checkout -b feature/YourFeature`)
3. Commit your changes (`git commit -am 'Add some feature'`)
4. Push to the branch (`git push origin feature/YourFeature`)
5. Create a new Pull Request

## License
This project is licensed under the ISC License (see `package.json`).

## Notes
- The `venv/`, `__pycache__/`, `.idea/`, and `node_modules/` directories are excluded via `.gitignore`.
- For any issues, please open an issue or contact the maintainer. 