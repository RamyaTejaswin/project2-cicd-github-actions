from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return '''
    <html>
        <body style="font-family: Arial; text-align: center; padding: 50px;">
            <h1>🚀 Hello from Ramya's DevOps Pipeline!</h1>
            <p>This app was deployed automatically using GitHub Actions CI/CD</p>
            <p>Built with Python Flask on Azure App Service</p>
        </body>
    </html>
    '''

@app.route('/health')
def health():
    return {"status": "healthy", "message": "App is running!"}

if __name__ == '__main__':
    app.run(debug=True)
