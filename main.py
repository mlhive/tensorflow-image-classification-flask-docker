# Import modules from flask and werkzeug libraries
from flask import Flask, request, jsonify
from werkzeug.utils import secure_filename
from src.Detector import predict

app = Flask(__name__) # create a flask app

@app.route('/')
def index():
    return "App is Working"


@app.route('/predict', methods=['POST'])
def predict_request():
    # Get file and save it
    file = request.files['image']
    filename = secure_filename(file.filename)
    file.save(filename)
    # Send prediction request
    resp = predict(filename)
    
    return jsonify({
        "class" : str(resp[1]),
        "accuracy" : round(float(resp[2]), 4)
    })


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80, debug=True)