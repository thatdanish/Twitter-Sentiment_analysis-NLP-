from flask import Flask,request,jsonify
from processing import call_model,prep_data
import pandas as pd
import numpy as np


app = Flask(__name__)

@app.route("/predict",methods=['POST'])

def make_predict():
    if request.method == "POST":
        data = {'success': False}

        user = request.get_json()
        df = pd.DataFrame([user['text']],columns=['text'])
        pred_df = df['text'][0]
        final_text = prep_data(pred_df)
        y_pred = model.predict(final_text)
        #y_pred = int(y_pred[0])

        y_pred = np.argmax(y_pred)
        y_pred = np.squeeze(y_pred)
        y_pred = str(y_pred)

        data['prediction'] = y_pred
        data['success'] = True

    return jsonify(data)

if __name__ == '__main__':
    print('**********Loading Model*********')
    model = call_model()
    app.run(debug=True,port=5000,threaded=False)