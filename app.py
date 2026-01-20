from flask import Flask, render_template_string
import os

app = Flask(__name__)

# 1. READ SETTINGS FROM CONFIGMAP
# We use environment variables that Kubernetes will inject for us
THEME_COLOR = os.getenv('THEME_COLOR', 'white') 
APP_NAME = os.getenv('APP_NAME', 'Generic Pet Shop')

# 2. READ SECRETS
# In a real app, you'd use this to connect to the database
DB_PASSWORD = os.getenv('DB_PASSWORD', 'NOT_SET')

@app.route('/')
def home():
    # This is the "Front Page" of our shop
    return f"""
    <html>
        <body style="background-color: {THEME_COLOR}; font-family: sans-serif; padding: 50px;">
            <h1>Welcome to {APP_NAME}! 🐾</h1>
            <p>Our Database connection is currently: <b>{"SECURE" if DB_PASSWORD != "NOT_SET" else "UNPROTECTED"}</b></p>
            <hr>
            <ul>
                <li><a href="/shop">Go to the Shop</a></li>
                <li><a href="/health">Health Check</a></li>
            </ul>
        </body>
    </html>
    """

@app.route('/shop')
def shop():
    return "<h2>🐶 Puppy Section | 🐱 Kitten Section</h2><p>Coming soon!</p>"

@app.route('/health')
def health():
    # This is what the "Manager" (Deployment) checks to see if we are alive
    return {"status": "healthy"}, 200

if __name__ == "__main__":
    # We run on port 5000 inside the container
    app.run(host='0.0.0.0', port=5000)
