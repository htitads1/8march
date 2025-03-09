from flask import Flask, request, render_template
import numpy as np
import pickle

app = Flask(__name__)

# Load the model once at startup
with open('best_model.pkl', 'rb') as file:
    model = pickle.load(file)

@app.route('/', methods=['GET', 'POST'])
def home():
    prediction = None  # Default value

    if request.method == 'POST':
        try:
            # Get user input from the form
            features = [float(x) for x in request.form.values()]
            features = np.array(features).reshape(1, -1)

            # Make prediction
            prediction = model.predict(features)[0]

        except Exception as e:
            prediction = f"Error: {str(e)}"

    return render_template('index.html', prediction=prediction)

if __name__ == '__main__':
    app.run(debug=True)
