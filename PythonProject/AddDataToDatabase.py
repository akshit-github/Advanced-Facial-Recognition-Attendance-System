import firebase_admin
from firebase_admin import credentials
from firebase_admin import db

cred = credentials.Certificate("serviceAccountKey.json")
firebase_admin.initialize_app(cred,{
    'databaseURL':"https://akshitattendacerealtime-default-rtdb.firebaseio.com/"
})

ref = db.reference('Students')

data = {
    "321654":
        {
            "name": "Vaibhav",
            "major": "Robotics",
            "starting_year": 2022,
            "total_attendance": 7,
            "standing": "G",
            "year": 4,
            "last_attendance_time": "2023-9-28 00:54:34"
        },
    "696969":
        {
            "name": "Akshit Agrawal",
            "major": "Machine Learning",
            "starting_year": 2022,
            "total_attendance": 15,
            "standing": "G",
            "year": 1,
            "last_attendance_time": "2023-9-28 00:54:34"
        },
    "852741":
        {
            "name": "Harsh",
            "major": "Economics",
            "starting_year": 2022,
            "total_attendance": 12,
            "standing": "B",
            "year": 1,
            "last_attendance_time": "2023-9-28 00:54:34"
        },
    "963852":
        {
            "name": "Avantika",
            "major": "Physics",
            "starting_year": 2022,
            "total_attendance": 7,
            "standing": "G",
            "year": 2,
            "last_attendance_time": "2023-9-28 00:54:34"
        }

}

for key,value in data.items():
    ref.child(key).set(value)