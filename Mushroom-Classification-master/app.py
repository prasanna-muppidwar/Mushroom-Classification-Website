from flask import Flask, render_template, request
import pickle
import numpy as np

label_encodings = {
    'gill-size': {'b': 0, 'n': 1},
    'gill-color': {'k': 0, 'n': 1, 'b': 2, 'h': 3, 'g': 4, 'r': 5, 'o': 6, 'p': 7, 'u': 8, 'e': 9, 'w': 10, 'y': 11},
    'stalk-root': {'b': 0, 'c': 1, 'u': 2, 'e': 3, 'z': 4, 'r': 5},
    'spore-print-color': {'k': 0, 'n': 1, 'b': 2, 'h': 3, 'r': 4, 'o': 5, 'u': 6, 'w': 7, 'y': 8},
    'population': {'a': 0, 'c': 1, 'n': 2, 's': 3, 'v': 4, 'y': 5}
}
def Mushroom_Predictor(result_data):
    encoded_result = []
    for key, value in result_data.items():
        encoded_value = label_encodings[key][value]
        encoded_result.append(encoded_value)
    prediction = np.array(encoded_result).reshape(1, 5)
    load_model = pickle.load(open('decision_tree_model.pkl', 'rb'))
    #load_model.feature_names = feature_names  # Set the feature names
    result = load_model.predict(prediction)
    return result[0]

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    result_data = request.form.to_dict()
    print(result_data)
    result = Mushroom_Predictor(result_data)
    if int(result) == 1:
        prediction = 'Edible'
    else:
        prediction = 'Poisonous'
    return render_template('result.html', prediction=prediction)

if __name__ == '__main__':
    app.run()
