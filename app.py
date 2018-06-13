from flask import Flask
app = Flask(__name__)

@app.route('/')
def index():
    return '<html><head></head><body>Hello World!</body></html>'

@app.route('/health')
def health():
    return '0'

if __name__ == '__main__':
    app.run(debug=False, host='0.0.0.0', port=8080)
