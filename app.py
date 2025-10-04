from flask import Flask, request, jsonify
from flask_cors import CORS
from database import get_db

app = Flask(__name__)
CORS(app)  # Allow cross-origin requests for frontend

# Database instance
db = get_db()

@app.route('/')
def home():
    return "Intelligent Battery Management Backend is Running!"

# API to retrieve SOC and SoH data
@app.route('/battery-data', methods=['GET'])
def get_battery_data():
    battery_data = list(db.battery.find({}, {"_id": 0}))
    return jsonify({"status": "success", "data": battery_data}), 200

# API to add battery data
@app.route('/battery-data', methods=['POST'])
def add_battery_data():
    data = request.json
    required_fields = ["soc", "soh", "timestamp"]
    
    if not all(field in data for field in required_fields):
        return jsonify({"status": "error", "message": "Missing required fields"}), 400
    
    db.battery.insert_one(data)
    return jsonify({"status": "success", "message": "Battery data added"}), 201

# API for critical alerts
@app.route('/alerts', methods=['GET'])
def get_alerts():
    alerts = list(db.alerts.find({}, {"_id": 0}))
    return jsonify({"status": "success", "data": alerts}), 200

if __name__ == '__main__':
    app.run(debug=True)
