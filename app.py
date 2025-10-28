from flask import Flask, render_template, request
from model import SmartIrrigationModel

app = Flask(__name__)
model = SmartIrrigationModel()

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    temperature = float(request.form['temperature'])
    humidity = float(request.form['humidity'])
    moisture = float(request.form['moisture'])
    result = model.predict(temperature, humidity, moisture)
    return render_template('index.html', result=result)

if __name__ == '__main__':
    app.run(debug=True)
