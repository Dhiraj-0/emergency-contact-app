# Emergency Contact Application - Specification

## Project Overview
- **Project Name**: Emergency Contact Application
- **Type**: Console-based Python Application
- **Core Functionality**: Allow users to save emergency contacts and simulate sending emergency alerts
- **Target Users**: Beginners learning Python

## Features

### 1. Add Emergency Contact
- Input: Name (string), Phone number (string)
- Storage: Python dictionary inside a list
- Validation: Both fields required

### 2. View Saved Contacts
- Display all saved contacts in a formatted list
- Show name and phone number for each contact
- Handle empty contact list gracefully

### 3. Emergency Alert
- Trigger simulated emergency message
- Print "Emergency message sent" to console
- Show which contacts would receive the alert

## Data Structure
- contacts_list: List of dictionaries
  - Each dictionary: {"name": "John", "phone": "1234567890"}

## User Interface
- Console-based menu with numbered options
- Clear prompts and feedback messages
- Exit option to close application

## Code Requirements
- Beginner-level Python (no complex frameworks)
- Use lists and dictionaries for data storage
- Simple functions for each feature
- Input validation with error handling

## Acceptance Criteria
1. User can add a contact with name and phone
2. User can view all saved contacts
3. User can trigger emergency alert (prints "Emergency message sent")
4. Application runs in console
5. Code is beginner-friendly with comments
