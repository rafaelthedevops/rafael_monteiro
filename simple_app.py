from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/<anystring>')
def show_anystring(anystring):
    return jsonify(anystring)

if __name__ == '__main__':
    app.run(port=3000)
