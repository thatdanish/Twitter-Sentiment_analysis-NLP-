from flask import Flask,request,jsonify

app = Flask(__name__)

@app.route('/prdict',methods=['POST'])
def make_predict():
    pass

if __name__ == '__main__':
    app.run(debug=True,port=5000)