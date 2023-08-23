from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/calculator/greeting", methods=['GET'])
def greeting():
    return 'Hello, world!'

@app.route("/calculator/add", methods=['POST'])
def add():
    data = request.get_json()
    num1 = data.get('num1')
    num2 = data.get('num2')
    result = num1 + num2
    return jsonify({"result": result})

@app.route("/calculator/subtract", methods=['POST'])
def subtract():
    data = request.get_json()
    num1 = data.get('num1')
    num2 = data.get('num2')
    result = num1 - num2
    return jsonify({"result": result})

if __name__ == '__main__':
    app.run(port=8080, host='0.0.0.0')
