# Twitter-Sentiment-NLP-Project-
Tweets Sentiment Classification
#### Model Architectue :- 
1) Embedding Layer (1) , units = 80
2) LSTM Layer (2) , units = 40,20
3) Dense Layer (2), units = 40,2
4) Dropout Layer (2) , dropout = 0.4,0.4
5) Optimizer = Adam
6) Metrics = Accuracy
7) Loss  = Binary Crossentropy

#### Model Save :-
1) h5 Model (Models/final_model.h5)
2) json file (Models/final_model.json)
3) Weights (tmp_weights)

#### Model Deployemnet :-
1) Model is Deployed via REST API by Flask (main_app.py)
2) Loading Model and input data preparation is done as a standalone (processing.py)
3) An exampler request with a dummy input is made, to check the deployement on the local server. (request.py)
#### Requirements :-
1) TensorFlow
2) Keras
3) Pandas
4) Numpy
5) Matplotlib
6) Seaborn