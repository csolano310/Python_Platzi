from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'hola, sergio lo lograste, ya eres todo un ingeniero :*.'

if __name__ == '__main__':
    app.run()
