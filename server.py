from flask import Flask, request, jsonify

app = Flask(__name__)

# Simple dictionary to store user credentials
users = {}

@app.route('/register', methods=['POST'])
def register():
    data = request.json
    email = data.get("email")
    password = data.get("password")

    if email in users:
        return jsonify({"success": False, "message": "Email already registered!"})

    users[email] = password
    return jsonify({"success": True, "message": "Registration successful!"})

@app.route('/login', methods=['POST'])
def login():
    data = request.json
    email = data.get("email")
    password = data.get("password")

    if users.get(email) == password:
        return jsonify({"success": True, "message": "Login Successful!", "redirect_url": "https://energyconsumption-ceschyr4zosnkfmjoffaqk.streamlit.app/"})
    
    return jsonify({"success": False, "message": "Invalid Email or Password!"})

if __name__ == '__main__':
    app.run(debug=True)
