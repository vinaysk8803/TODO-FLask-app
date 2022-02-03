from flask import Flask , request,jsonify
app = Flask(__name__)

@app.route('/',methods=['POST'])
def add():
    raw_json=request.get_json()
    num1 = int(raw_json['num1'])
    num2 = int(raw_json['num2'])

    return f"{num1 + num2}";

if __name__=="main_":
    app.run(debug=True)
    app.run(debug=True)