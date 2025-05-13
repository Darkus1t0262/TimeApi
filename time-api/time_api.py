from flask import Flask, jsonify
from flask_cors import CORS
import datetime

app = Flask(__name__)
CORS(app)  # Enable CORS for all domains

@app.route('/time', methods=['GET'])
def get_time():
    return jsonify({"time": datetime.datetime.now().strftime("%H:%M:%S")})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)