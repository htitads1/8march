from flask import Flask, request, jsonify
import numpy as np
import pickle

app = Flask(__name__)

@app.route('/predict', methods=['GET'])
def predict():
    data = request.get_json()
    features = np.array(data['features']).reshape(1, -1)
    with open('best_model.pkl', 'rb') as file:
        model = pickle.load(file)
    prediction = model.predict(features)
    return jsonify({'prediction': int(prediction[0])})

if __name__ == '__main__':
    # Make the API accessible to external networks (for deployment)
    app.run(host='0.0.0.0', port=5000)