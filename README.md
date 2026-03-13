# **Study Session Tracker**

## **Description**
### I built a small study session tracker web-app that uses a SQLite data that stores, retrieves, updates, and deletes data with the help of Claude AI. 

### I want to become more efficient with studying as semester progresses, so keeping tracker can help me analyze myself and better my time management.

### Features of Table:
- id (automated integer)
- date (text in the form of 'YYYY-MM-DD')
- duration (real)
- task_type (text)
- focus_rating (integer 1-5)

## **How to install and run it**
1. Clone the repository
2. Navigate into the project folder
3. Install Flask 'python -m pip install flask'
4. Run the app in Terminal 'python app.py' or to run through locally without user interface 'python tracker.py'
5. Open your browser and go to 'http://127.0.0.1:5000/'

## **How to use Flask Version**
- View Sessions: shows all study sessions recorded (READ)
- Add Session: allows you to log a new session including data, duration studied, subject, task type, and focus rating (CREATE)
- Filter by subject: allows you to filter to see the study sessions specifically for one subject (need to make sure you typed it exactly) (READ)
- Edit: allows you to edit any one of the boxes in a certain session (UPDATE)
- Delete: prompts you with confirmation before allowing you to delete the study session log (DELETE)

## **How to use CLI Version**
- Main menu provides a main menu with 6 options for you to choose from
- Based on what you choose, you can do the same as what you would do in the Flask Version
- All CRUD operations work the same

## **Future Improvements**
- Enhance UI design
- Add more unique features that improve UX