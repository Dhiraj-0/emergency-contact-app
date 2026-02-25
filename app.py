#!/usr/bin/env python3
"""
Emergency Contact Application - Flask Web Version
==================================================
A beginner-friendly web app to manage emergency contacts.

To run:
1. pip install flask
2. python app.py
3. Open http://localhost:5000
"""

from flask import Flask, render_template_string, request, redirect, url_for, flash

# Create Flask app
app = Flask(__name__)
app.secret_key = 'emergency_contact_app_secret_key'

# Data storage - using a list of dictionaries
contacts_list = []

# Indian Government Emergency Contacts
indian_emergency_contacts = [
    {"name": "Police (All India)", "phone": "100"},
    {"name": "Fire Service", "phone": "101"},
    {"name": "Ambulance", "phone": "102"},
    {"name": "Women Helpline", "phone": "1091"},
    {"name": "Child Helpline", "phone": "1098"},
    {"name": "Disaster Management", "phone": "1070"},
    {"name": "National Emergency", "phone": "112"},
    {"name": "Railway Police", "phone": "1512"},
    {"name": "Road Safety", "phone": "1033"},
    {"name": "Anti Terrorist Helpline", "phone": "1930"},
]

# HTML Template
HTML_TEMPLATE = '''
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>🚨 Emergency Contact Application</title>
    <style>
        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }
        
        body {
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            min-height: 100vh;
            padding: 20px;
        }
        
        .container {
            max-width: 800px;
            margin: 0 auto;
        }
        
        .header {
            text-align: center;
            color: white;
            margin-bottom: 30px;
        }
        
        .header h1 {
            font-size: 2.5em;
            margin-bottom: 10px;
        }
        
        .card {
            background: white;
            border-radius: 15px;
            padding: 25px;
            margin-bottom: 20px;
            box-shadow: 0 10px 30px rgba(0,0,0,0.2);
        }
        
        .card h2 {
            color: #333;
            margin-bottom: 20px;
            border-bottom: 2px solid #667eea;
            padding-bottom: 10px;
        }
        
        .form-group {
            margin-bottom: 15px;
        }
        
        label {
            display: block;
            margin-bottom: 5px;
            color: #555;
            font-weight: bold;
        }
        
        input[type="text"] {
            width: 100%;
            padding: 12px;
            border: 2px solid #ddd;
            border-radius: 8px;
            font-size: 16px;
            transition: border-color 0.3s;
        }
        
        input[type="text"]:focus {
            outline: none;
            border-color: #667eea;
        }
        
        .btn {
            padding: 12px 25px;
            border: none;
            border-radius: 8px;
            font-size: 16px;
            cursor: pointer;
            transition: transform 0.2s, box-shadow 0.2s;
            display: inline-block;
            text-decoration: none;
            text-align: center;
        }
        
        .btn:hover {
            transform: translateY(-2px);
            box-shadow: 0 5px 15px rgba(0,0,0,0.2);
        }
        
        .btn-success { background: #28a745; color: white; }
        .btn-danger { background: #dc3545; color: white; }
        .btn-warning { background: #ffc107; color: #333; }
        .btn-info { background: #17a2b8; color: white; }
        .btn-primary { background: #667eea; color: white; }
        
        .btn-group {
            display: flex;
            gap: 10px;
            flex-wrap: wrap;
            margin-top: 20px;
        }
        
        table {
            width: 100%;
            border-collapse: collapse;
            margin-top: 15px;
        }
        
        th, td {
            padding: 12px;
            text-align: left;
            border-bottom: 1px solid #ddd;
        }
        
        th {
            background: #667eea;
            color: white;
        }
        
        tr:hover {
            background: #f5f5f5;
        }
        
        .alert-box {
            padding: 15px;
            border-radius: 8px;
            margin-bottom: 20px;
        }
        
        .alert-success {
            background: #d4edda;
            border: 1px solid #c3e6cb;
            color: #155724;
        }
        
        .alert-danger {
            background: #f8d7da;
            border: 1px solid #f5c6cb;
            color: #721c24;
        }
        
        .alert-warning {
            background: #fff3cd;
            border: 1px solid #ffeaa7;
            color: #856404;
        }
        
        .emergency-alert {
            background: linear-gradient(135deg, #ff416c 0%, #ff4b2b 100%);
            color: white;
            text-align: center;
            padding: 30px;
            border-radius: 15px;
        }
        
        .emergency-alert h3 {
            font-size: 2em;
            margin-bottom: 15px;
        }
        
        .emergency-alert .message {
            font-size: 1.5em;
            font-weight: bold;
        }
        
        .nav-buttons {
            display: flex;
            gap: 10px;
            margin-bottom: 20px;
        }
        
        .nav-buttons a {
            padding: 10px 20px;
            background: rgba(255,255,255,0.2);
            color: white;
            text-decoration: none;
            border-radius: 8px;
            transition: background 0.3s;
        }
        
        .nav-buttons a:hover {
            background: rgba(255,255,255,0.3);
        }
        
        .empty-state {
            text-align: center;
            padding: 40px;
            color: #777;
        }
        
        .indian-contacts {
            background: #f8f9fa;
            padding: 15px;
            border-radius: 8px;
            margin-top: 15px;
        }
        
        .indian-contacts h3 {
            color: #333;
            margin-bottom: 10px;
        }
        
        .indian-contacts ul {
            list-style: none;
            padding: 0;
        }
        
        .indian-contacts li {
            padding: 8px;
            border-bottom: 1px solid #ddd;
            display: flex;
            justify-content: space-between;
        }
        
        .indian-contacts li:last-child {
            border-bottom: none;
        }
    </style>
</head>
<body>
    <div class="container">
        <div class="header">
            <h1>🚨 Emergency Contact Application</h1>
            <p>Manage your emergency contacts and send alerts</p>
            <div class="nav-buttons">
                <a href="/">Home</a>
                <a href="/contacts">View Contacts</a>
                <a href="/emergency">Emergency Alert</a>
            </div>
        </div>
        
        {% with messages = get_flashed_messages(with_categories=true) %}
            {% if messages %}
                {% for category, message in messages %}
                    <div class="alert-box alert-{{ category }}">
                        {{ message }}
                    </div>
                {% endfor %}
            {% endif %}
        {% endwith %}
        
        {% if page == 'home' %}
        <div class="card">
            <h2>📱 Add Emergency Contact</h2>
            <form method="POST" action="/add">
                <div class="form-group">
                    <label for="name">Contact Name:</label>
                    <input type="text" id="name" name="name" placeholder="Enter contact name" required>
                </div>
                <div class="form-group">
                    <label for="phone">Phone Number:</label>
                    <input type="text" id="phone" name="phone" placeholder="Enter phone number" required>
                </div>
                <button type="submit" class="btn btn-success">➕ Add Contact</button>
            </form>
        </div>
        
        <div class="card">
            <h2>🇮🇳 Quick Add Indian Emergency Contacts</h2>
            <p>One-click to add all Indian government emergency numbers:</p>
            <form method="POST" action="/add_indian">
                <button type="submit" class="btn btn-warning">🇮🇳 Load Indian Emergency Contacts</button>
            </form>
            
            <div class="indian-contacts">
                <h3>Available Indian Emergency Numbers:</h3>
                <ul>
                    <li><span>Police</span><strong>100</strong></li>
                    <li><span>Fire Service</span><strong>101</strong></li>
                    <li><span>Ambulance</span><strong>102</strong></li>
                    <li><span>Women Helpline</span><strong>1091</strong></li>
                    <li><span>Child Helpline</span><strong>1098</strong></li>
                    <li><span>National Emergency</span><strong>112</strong></li>
                </ul>
            </div>
        </div>
        
        {% elif page == 'contacts' %}
        <div class="card">
            <h2>📋 Saved Contacts</h2>
            {% if contacts %}
                <p>Total contacts: <strong>{{ contacts|length }}</strong></p>
                <table>
                    <thead>
                        <tr>
                            <th>#</th>
                            <th>Name</th>
                            <th>Phone</th>
                        </tr>
                    </thead>
                    <tbody>
                        {% for contact in contacts %}
                        <tr>
                            <td>{{ loop.index }}</td>
                            <td>{{ contact.name }}</td>
                            <td>{{ contact.phone }}</td>
                        </tr>
                        {% endfor %}
                    </tbody>
                </table>
            {% else %}
                <div class="empty-state">
                    <p>⚠️ No emergency contacts saved yet!</p>
                    <p>Go to Home to add contacts.</p>
                </div>
            {% endif %}
        </div>
        
        {% elif page == 'emergency' %}
        <div class="card">
            <div class="emergency-alert">
                <h3>🚨 EMERGENCY ALERT 🚨</h3>
                {% if contacts %}
                    <p>Notifying {{ contacts|length }} contact(s)...</p>
                    <ul style="list-style: none; padding: 20px; text-align: left;">
                        {% for contact in contacts %}
                        <li>📱 {{ contact.name }} - {{ contact.phone }}</li>
                        {% endfor %}
                    </ul>
                    <p class="message">Emergency message sent</p>
                    <p>✓ All contacts have been notified!</p>
                {% else %}
                    <p>⚠️ No contacts to notify!</p>
                    <p>Please add emergency contacts first.</p>
                {% endif %}
            </div>
        </div>
        {% endif %}
        
        <div class="card">
            <h2>📊 Statistics</h2>
            <p>Total contacts saved: <strong>{{ contacts|length }}</strong></p>
        </div>
    </div>
</body>
</html>
'''

@app.route('/')
def home():
    """Home page with add contact form"""
    return render_template_string(HTML_TEMPLATE, page='home', contacts=contacts_list)

@app.route('/contacts')
def contacts():
    """View all contacts page"""
    return render_template_string(HTML_TEMPLATE, page='contacts', contacts=contacts_list)

@app.route('/emergency')
def emergency():
    """Emergency alert page"""
    return render_template_string(HTML_TEMPLATE, page='emergency', contacts=contacts_list)

@app.route('/add', methods=['POST'])
def add_contact():
    """Add new contact"""
    name = request.form.get('name', '').strip()
    phone = request.form.get('phone', '').strip()
    
    if name and phone:
        contacts_list.append({'name': name, 'phone': phone})
        flash(f'✓ SUCCESS: Contact "{name}" added with phone {phone}!', 'success')
    else:
        flash('⚠ ERROR: Name and phone cannot be empty!', 'danger')
    
    return redirect(url_for('home'))

@app.route('/add_indian', methods=['POST'])
def add_indian_contacts():
    """Add Indian emergency contacts"""
    count = 0
    for contact in indian_emergency_contacts:
        if contact not in contacts_list:
            contacts_list.append(contact)
            count += 1
    
    flash(f'✓ Added {count} Indian emergency contacts!', 'success')
    return redirect(url_for('home'))

if __name__ == '__main__':
    print("="*50)
    print("  🚨 Emergency Contact App Starting...")
    print("="*50)
    print("  Open your browser and go to:")
    print("  http://localhost:5000")
    print("="*50)
    app.run(debug=True, host='0.0.0.0', port=5000)
