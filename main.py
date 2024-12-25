from flask import Flask, render_template, jsonify, request
import os

# Initialize Flask app
app = Flask(__name__)

# In-memory storage for customer locations
customers = [
    {"id": 1, "name": "Customer A", "latitude": 6.9271, "longitude": 79.8612},
    {"id": 2, "name": "Customer B", "latitude": 7.8731, "longitude": 80.7718},
    {"id": 3, "name": "Customer C", "latitude": 6.0322, "longitude": 80.217},
]

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/edit")
def edit():
    # Ensure the `edit.html` file exists in your `templates` folder
    return render_template("edit.html")

@app.route("/api/customers", methods=["GET", "POST", "PUT"])
def manage_customers():
    if request.method == "GET":
        return jsonify(customers)

    if request.method == "POST":
        new_customer = request.json
        new_customer_id = max((customer["id"] for customer in customers), default=0) + 1
        new_customer["id"] = new_customer_id
        customers.append(new_customer)
        return jsonify({"message": "Customer added successfully", "id": new_customer_id}), 201

    if request.method == "PUT":
        updated_customer = request.json
        for customer in customers:
            if customer["id"] == updated_customer["id"]:
                customer.update(updated_customer)
                return jsonify({"message": "Customer updated successfully"}), 200
        return jsonify({"message": "Customer not found"}), 404

if __name__ == "__main__":
    app.run(debug=True)
