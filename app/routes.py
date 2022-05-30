from app import app
@app.route('/')
def home():
    greeting = 'Hello, Universe!'
    print(greeting)
    return 'Hello, World.'