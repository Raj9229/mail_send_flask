
# mail_send_flask

A simple Flask-based application for sending emails. This project demonstrates how to integrate email sending capabilities into a Python Flask web application.

## Features

- Send emails via an easy-to-use web interface
- Configurable sender email and SMTP settings
- Basic frontend using HTML/JavaScript
- Example usage with Gmail SMTP (customize for your provider)

## Requirements

- Python 3.x
- Flask
- Other dependencies (see [Installation](#installation))

## Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/Raj9229/mail_send_flask.git
   cd mail_send_flask
   ```

2. **Create a virtual environment (optional but recommended):**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

## Configuration

Create a `.env` file (or edit the config in your script) with your email settings:

```env
MAIL_SERVER=smtp.gmail.com
MAIL_PORT=587
MAIL_USE_TLS=True
MAIL_USERNAME=your_email@gmail.com
MAIL_PASSWORD=your_email_password
```

**Note:** For Gmail, you may need to enable "Less secure app access" or set up an App Password.

## Usage

1. **Run the application:**
   ```bash
   flask run
   ```
   or, if your main file is named differently:
   ```bash
   python app.py
   ```

2. **Open your browser** and go to [http://localhost:5000](http://localhost:5000).  
   Fill in the form and send an email!

## Project Structure

```
mail_send_flask/
├── app.py
├── templates/
│   └── index.html
├── static/
│   └── (optional JS/CSS files)
├── requirements.txt
└── README.md
```

## Contributing

Pull requests are welcome! For major changes, please open an issue first to discuss what you would like to change.

