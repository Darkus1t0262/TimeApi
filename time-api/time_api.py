# time_api.py
from flask import Flask, jsonify
import datetime

app = Flask(__name__)

@app.route('/time', methods=['GET'])
def get_time():
    return jsonify({"time": datetime.datetime.now().strftime("%H:%M:%S")})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
