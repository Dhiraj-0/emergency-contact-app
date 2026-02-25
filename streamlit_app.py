#!/usr/bin/env python3
"""
Emergency Contact Application - Streamlit Web Version
=====================================================
A beginner-friendly web app to manage emergency contacts.

To run:
1. streamlit run streamlit_app.py
2. It will open in your browser automatically
"""

import streamlit as st

# Page configuration
st.set_page_config(
    page_title="🚨 Emergency Contact App",
    page_icon="🚨",
    layout="wide"
)

# Data storage - using session state to persist data
if 'contacts_list' not in st.session_state:
    st.session_state.contacts_list = []

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

# Custom CSS
st.markdown("""
<style>
    .main {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
    }
    .stApp {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
    }
    .card {
        background: white;
        padding: 20px;
        border-radius: 15px;
        box-shadow: 0 10px 30px rgba(0,0,0,0.2);
        margin-bottom: 20px;
    }
    .emergency-alert {
        background: linear-gradient(135deg, #ff416c 0%, #ff4b2b 100%);
        color: white;
        padding: 30px;
        border-radius: 15px;
        text-align: center;
    }
    .success-msg {
        background: #28a745;
        color: white;
        padding: 15px;
        border-radius: 8px;
        margin-bottom: 15px;
    }
</style>
""", unsafe_allow_html=True)

# Title
st.title("🚨 Emergency Contact Application")
st.markdown("### Manage your emergency contacts and send alerts")

# Sidebar
st.sidebar.title("📋 Menu")
menu = st.sidebar.radio("Select Option:", 
    ["🏠 Home", "📋 View Contacts", "🚨 Emergency Alert", "🗑️ Clear All"])

# Main content
if menu == "🏠 Home":
    st.markdown("## 📱 Add Emergency Contact")
    
    with st.form("add_contact_form"):
        col1, col2 = st.columns(2)
        with col1:
            name = st.text_input("Contact Name", placeholder="Enter name")
        with col2:
            phone = st.text_input("Phone Number", placeholder="Enter phone number")
        
        submit = st.form_submit_button("➕ Add Contact")
        
        if submit:
            if name and phone:
                st.session_state.contacts_list.append({"name": name, "phone": phone})
                st.success(f"✓ SUCCESS: Contact '{name}' added with phone {phone}!")
            else:
                st.error("⚠ ERROR: Name and phone cannot be empty!")
    
    st.markdown("---")
    st.markdown("## 🇮🇳 Quick Add Indian Emergency Contacts")
    
    if st.button("🇮🇳 Load Indian Emergency Contacts"):
        count = 0
        for contact in indian_emergency_contacts:
            if contact not in st.session_state.contacts_list:
                st.session_state.contacts_list.append(contact)
                count += 1
        st.success(f"✓ Added {count} Indian emergency contacts!")
    
    # Show available Indian contacts
    with st.expander("📱 Available Indian Emergency Numbers"):
        for contact in indian_emergency_contacts:
            st.markdown(f"**{contact['name']}**: {contact['phone']}")

elif menu == "📋 View Contacts":
    st.markdown("## 📋 Saved Contacts")
    
    if st.session_state.contacts_list:
        st.info(f"Total contacts: **{len(st.session_state.contacts_list)}**")
        
        # Create a table
        for i, contact in enumerate(st.session_state.contacts_list, 1):
            st.markdown(f"""
            <div class="card">
                <h4>Contact #{i}</h4>
                <p><strong>Name:</strong> {contact['name']}</p>
                <p><strong>Phone:</strong> {contact['phone']}</p>
            </div>
            """, unsafe_allow_html=True)
    else:
        st.warning("⚠️ No emergency contacts saved yet!")
        st.info("Go to Home to add contacts.")

elif menu == "🚨 Emergency Alert":
    st.markdown("## 🚨 EMERGENCY ALERT 🚨")
    
    if st.session_state.contacts_list:
        st.markdown(f"""
        <div class="emergency-alert">
            <h2>🚨 EMERGENCY ALERT 🚨</h2>
            <p>Notifying **{len(st.session_state.contacts_list)}** contact(s)...</p>
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown("### 📱 Contacts being notified:")
        for contact in st.session_state.contacts_list:
            st.write(f"📱 {contact['name']} - {contact['phone']}")
        
        st.markdown("---")
        st.markdown("""
        <div style="background: #28a745; color: white; padding: 20px; border-radius: 10px; text-align: center;">
            <h2>✅ Emergency message sent</h2>
            <p>All contacts have been notified!</p>
        </div>
        """, unsafe_allow_html=True)
    else:
        st.error("⚠️ No contacts to notify!")
        st.warning("Please add emergency contacts first.")

elif menu == "🗑️ Clear All":
    st.markdown("## 🗑️ Clear All Contacts")
    
    if st.session_state.contacts_list:
        if st.button("Confirm Clear All"):
            st.session_state.contacts_list = []
            st.success("✓ All contacts cleared!")
    else:
        st.info("No contacts to clear.")

# Footer
st.markdown("---")
st.markdown(f"📊 **Total contacts saved:** {len(st.session_state.contacts_list)}")
