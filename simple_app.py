from flask import Flask

app = Flask(__name__)

@app.route('/<anystring>')
def show_anystring(anystring):
    return anystring

if __name__ == '__main__':
    app.run()
