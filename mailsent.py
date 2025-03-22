from flask import Flask, render_template
from flask_mail import Mail, Message
import json
import os

app = Flask(__name__)

# Improve config file handling
try:
    # Get absolute path to the config file
    base_dir = os.path.abspath(os.path.dirname(__file__))
    static_dir = os.path.join(base_dir, 'static')
    config_path = os.path.join(static_dir, 'config.js')
    
    # Create static directory if it doesn't exist
    if not os.path.exists(static_dir):
        os.makedirs(static_dir)
        print(f"Created static directory at: {static_dir}")
    
    # Check if config file exists
    if not os.path.exists(config_path):
        print(f"Config file not found at: {config_path}")
        print("Creating a template config file. Please update with your credentials.")
        
        # Create a template config file
        default_config = {
            "param": {
                "gmail-user": "your-email@gmail.com",
                "gmail-password": "your-app-password"
            }
        }
        
        with open(config_path, 'w') as f:
            json.dump(default_config, f, indent=4)
        
        print(f"Template config file created at: {config_path}")
        print("Please update the file with your Gmail credentials before running again.")
        exit(1)
        
    with open(config_path, 'r') as f:
        config_content = f.read()
        # Handle JavaScript-style comments if present
        if config_content.strip().startswith('//'):
            # Strip JavaScript comments
            config_content = '\n'.join([line for line in config_content.split('\n')
                                      if not line.strip().startswith('//')])
        params = json.loads(config_content)['param']
    print(f"Config loaded successfully from {config_path}")
    
    # Validate required parameters
    if params['gmail-user'] == "your-email@gmail.com" or params['gmail-password'] == "your-app-password":
        print("Error: Default credentials found in config file.")
        print(f"Please update {config_path} with your actual Gmail credentials.")
        exit(1)
        
except json.JSONDecodeError as e:
    print(f"Error parsing config.js: {e}. Check your JSON format.")
    print("Make sure the file contains valid JSON without JavaScript comments.")
    raise
except Exception as e:
    print(f"Error loading config: {e}")
    print("Please ensure config.js in the static folder has the format:")
    print('{"param": {"gmail-user": "your-email@gmail.com", "gmail-password": "your-app-password"}}')
    raise

# Configure Flask-Mail with improved password handling
app.config.update(
    MAIL_SERVER='smtp.gmail.com',
    MAIL_PORT=587,
    MAIL_USERNAME=params['gmail-user'],
    MAIL_PASSWORD=params['gmail-password'].replace(" ", ""),  # Remove any spaces
    MAIL_USE_TLS=True,
    MAIL_USE_SSL=False,
    MAIL_DEFAULT_SENDER=params['gmail-user']
)

mail = Mail(app)

# Add debug information to help troubleshoot
password = params['gmail-password'].replace(" ", "")
print(f"Mail username configured: {app.config['MAIL_USERNAME']}")
print(f"Mail password length: {len(password)} characters")
print(f"First and last 2 chars of password: {password[:2]}...{password[-2:]}")

@app.route('/')
def index():
    try:
        # Create proper email message
        msg = Message(
            subject='Hello from Flask',
            recipients=['rajgupta807633@gmail.com'],
            body='This is a test email sent from Flask using Gmail SMTP server.',
            sender=app.config['MAIL_USERNAME']
        )
        mail.send(msg)
        return 'Mail Sent Successfully!'
    except Exception as e:
        error_details = str(e)
        print(f"Error sending mail: {error_details}")
        
        # Provide helpful error messages based on common issues
        if "Authentication" in error_details:
            return f"Error: Gmail authentication failed. Make sure you're using an App Password if you have 2FA enabled.<br>Details: {error_details}"
        elif "smtplib.SMTPConnectError" in error_details or "refused" in error_details:
            return f"Error: Could not connect to Gmail SMTP server. Check your network/firewall settings.<br>Details: {error_details}"
        else:
            return f"Error sending mail: {error_details}"

if __name__ == '__main__':
    app.run(debug=True)
