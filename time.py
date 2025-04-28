import bpy
import datetime

# Full timetable from Monday to Friday
timetable = {
    "Monday": {
        "2nd Year": [
            {"time": "08:30-09:30", "subject": "EM-4", "room": "B-53", "professor": "Prof Sarla Yadav"},
            {"time": "09:30-10:30", "subject": "MP", "room": "B-53", "professor": "Prof RA"},
            {"time": "10:30-11:30", "subject": "AOA", "room": "B-53", "professor": "Prof ABC"},
            {"time": "11:30-12:30", "subject": "DBMS", "room": "B-53", "professor": "Dr Jyoti Deshmukh"},
            {"time": "01:15-03:30", "subject": "Lab", "groups": {
                "S1": {"subject": "Py", "room": "C-53", "professor": "Prof Bharti Jadhav"},
                "S2": {"subject": "MP", "room": "A-51", "professor": "Prof RA"},
                "S3": {"subject": "AOA", "room": "C-51", "professor": "Prof ABC"},
                "S4": {"subject": "OS", "room": "A-51", "professor": "Prof Divya Tama"}
            }}
        ],
        "3rd Year": [
            {"time": "08:30-09:30", "subject": "ML", "room": "B-54", "professor": "Dr Nilesh Bhelkar"},
            {"time": "09:30-10:30", "subject": "CSS", "room": "B-54", "professor": "Prof Divya Tama"},
            {"time": "10:30-11:30", "subject": "IVP", "room": "B-54", "professor": "Prof Samrin Pabrekar"},
            {"time": "11:30-12:30", "subject": "DAV", "room": "B-54", "professor": "Prof Gurvin Kaur"},
            {"time": "13:15-14:30", "subject": "Lab", "groups": {
                "T3": {"subject": "DAV", "room": "A-51", "professor": "Prof Gurvin Kaur"},
                "S2": {"subject": "SEPM", "room": "A-51", "professor": "Prof Samrin Pabrekar"}
            }}
        ],
        "4th Year": [
            {"time": "08:30-09:30", "subject": "RS", "room": "B-54", "professor": "Prof Deepa Agarwal"},
            {"time": "08:30-09:30", "subject": "SMA", "room": "B-51", "professor": "Prof Sachin Narkhade"},
            {"time": "09:30-10:30", "subject": "AFB", "room": "B-53", "professor": "Prof XYZ"},
            {"time": "10:30-12:30", "subject": "Lab", "groups": {
                "B1": {"subject": "AAI", "room": "C-51", "professor": "Dr Nilesh Bhelkar"},
                "B2": {"subject": "RS", "room": "A-51", "professor": "Prof Deepa Agarwal"},
                "B3": {"subject": "SMA", "room": "C-53", "professor": "Prof Sachin Narkhade"},
                "B4": {"subject": "AFB", "room": "C-51", "professor": "Prof XYZ"}
            }}
        ],
    },

    "Tuesday": {
        "2nd Year": [
            {"time": "08:30-09:30", "subject": "MP", "room": "B-53", "professor": "Prof RA"},
            {"time": "09:30-10:30", "subject": "AOA", "room": "B-53", "professor": "Prof ABC"},
            {"time": "10:30-11:30", "subject": "OS", "room": "B-53", "professor": "Prof Divya Tama"},
            {"time": "11:30-12:30", "subject": "MP", "room": "B-53", "professor": "Prof RA"},
            {"time": "01:15-03:30", "subject": "Miniproject 1B"}
        ],
        "3rd Year": [
            {"time": "08:30-09:30", "subject": "CSS", "room": "B-54", "professor": "Prof Divya Tama"},
            {"time": "09:30-10:30", "subject": "IVP", "room": "B-54", "professor": "Prof Samrin Pabrekar"},
            {"time": "10:30-12:30", "subject": "Lab", "groups": {
                "T1": {"subject": "CCL", "room": "A-51", "professor": "Prof Sachin Narkhade"},
                "T2": {"subject": "SEPM", "room": "C-53", "professor": "Prof Samrin Pabrekar"},
                "T3": {"subject": "CCL", "room": "A-51", "professor": "Prof ABC"},
                "T4": {"subject": "CSS", "room": "A-53", "professor": "Prof Gurvin Kaur"}
            }},
            {"time": "1:15-3:15", "subject": "Lab", "groups": {
                "T1": {"subject": "DAV", "room": "A-53", "professor": "Prof Gurvin Kaur"},
                "T2": {"subject": "CCL", "room": "A-51", "professor": "Prof Sachin Narkhade"}
            }}
        ],
        "4th Year": [
            {"time": "08:30-10:30", "subject": "Lab", "groups": {
                "B1": {"subject": "RS", "room": "A-51", "professor": "Prof Deepa Agarwal"},
                "B2": {"subject": "AFB", "room": "C-51", "professor": "Prof XYZ"},
                "B3": {"subject": "AAI", "room": "C-51", "professor": "Dr Nilesh Bhelkar"},
                "B4": {"subject": "SMA", "room": "C-53", "professor": "Prof Sachin Narkhade"}
            }},
            {"time": "10:30-11:30", "subject": "EM", "room": "B-54", "professor": "Prof GKS"},
            {"time": "10:30-11:30", "subject": "FM", "room": "B-41", "professor": "Prof Sachin Narkhade"},
            {"time": "11:30-12:30", "subject": "AAI", "room": "B-54", "professor": "Dr Nilesh Bhelkar"},
            {"time": "08:30-10:30", "subject": "Lab", "groups": {
                "B1": {"subject": "AFB", "room": "C-51", "professor": "Prof XYZ"},
                "B3": {"subject": "AAI", "room": "C-51", "professor": "Dr Nilesh Bhelkar"}
            }}
        ],
    },

    "Wednesday": {
        "2nd Year": [
            {"time": "22:30-23:30", "subject": "Lab", "groups": {
                "S1": {"subject": "AOA", "room": "C-51", "professor": "Prof ABC"},
                "S2": {"subject": "OS", "room": "A-51", "professor": "Prof Divya Tama"},
                "S3": {"subject": "DBMS", "room": "A-53", "professor": "Dr Jyoti Deshmukh"},
                "S4": {"subject": "MP", "room": "A-51", "professor": "Prof RA"}
            }},
            {"time": "10:30-11:30", "subject": "DBMS", "room": "B-53", "professor": "Dr Jyoti Deshmukh"},
            {"time": "11:30-12:30", "subject": "PY", "room": "B-53", "professor": "Prof xyz"},
            {"time": "1:15-3-15", "subject": "Lab", "groups": {
                "S1": {"subject": "DBMS", "room": "A-53", "professor": "Dr Jyoti Deshmukh"}, 
                "S2": {"subject": "PY", "room": "C-53", "professor": "Prof Bharti Jadhav"},
                "S3": {"subject": "MP", "room": "A-51", "professor": "Prof RA"},
                "S4": {"subject": "AOA", "room": "C-51", "professor": "Prof ABC"}
            }},
            {"time": "3:15-4:15", "subject": "Miniproject 1B"}
        ],
        "3rd Year": [
            {"time": "08:30-09:30", "subject": "SEPM", "room": "B-53", "professor": "Prof Samrin Pabrekar"},
            {"time": "09:30-10:30", "subject": "DAV", "room": "B-53", "professor": "Prof Gurvin Kaur"},
            {"time": "10:30-12:30", "subject": "Lab", "groups": {
                "T1": {"subject": "ML", "room": "C-51", "professor": "Prof Deepa Agarwal"},
                "T2": {"subject": "CCL", "room": "A-51", "professor": "Prof Sachin Narkhade"},
                "T3": {"subject": "CSS", "room": "A-51", "professor": "Prof Gurvin Kaur"},
                "T4": {"subject": "CCL", "room": "A-51", "professor": "Prof ABC"}
            }},
            {"time": "1:15-2-15", "subject": "IVP", "room": "B-54", "professor": "Prof Samrin Pabrekar"},
            {"time": "2:15-3-15", "subject":  "CSS", "room": "B-54", "professor": "Prof Divya Tama"},
            {"time": "3:15-4:15", "subject": "Miniproject 2B"}
        ],
        "4th Year": [
            {"time": "08:30-09:30", "subject": "RS", "room": "B-54", "professor": "Prof Deepa Agarwal"},
            {"time": "08:30-09:30", "subject": "SMA", "room": "B-51", "professor": "Prof Sachin Narkhade"},
            {"time": "09:30-10:30", "subject": "AFB", "room": "B-54", "professor": "Prof XYZ"},
            {"time": "10:30-11:30", "subject": "EM", "room": "B-54", "professor": "Prof GKS"},
            {"time": "10:30-11:30", "subject": "FM", "room": "B-41", "professor": "Prof Sachin Narkhade"},
            {"time": "11:30-12:30", "subject": "AAI", "room": "B-54", "professor": "Dr Nilesh Bhelkar"}
        ],
    },
    "Thursday": {
        "2nd Year": [
            {"time": "08:00-10:30", "subject": "Lab", "groups": {
                "S1": {"subject": "OS", "room": "A-51", "professor": "Prof Divya Tama"},
                "S2": {"subject": "AOA", "room": "A-53", "professor": "Prof ABC"},
                "S3": {"subject": "PY", "room": "C-53", "professor": "Prof Bharti Jadhav"},
                "S4": {"subject": "DBMS", "room": "A-53", "professor": "Dr Jyoti Deshmukh"}
            }},
            {"time": "10:30-11:30", "subject":"OS", "room": "B-53", "professor": "Prof Divya Tama"},
            {"time": "11:30-12:30", "subject": "DBMS", "room": "B-53", "professor": "Dr Jyoti Deshmukh"},
            {"time": "1:15:2:15", "subject": "MP", "room": "B-53", "professor": "Prof RA"},
            {"time": "2:15:3:15", "subject": "EM-4", "room": "B-53", "professor": "Prof Sarla Yadav"}
        ],
        "3rd Year": [
            {"time": "08:30-09:30", "subject": "DAV", "room": "B-53", "professor": "Prof Gurvin Kaur"},
            {"time": "09:30-10:30", "subject": "ML", "room": "B-53", "professor": "Dr Nilesh Bhelkar"},
            {"time": "10:30-12:30", "subject": "Lab", "groups": {
                "T1": {"subject": "CSS", "room": "A-53", "professor": "Prof Samrin Pabrekar"},
                "T2": {"subject": "DAV", "room": "A-53", "professor": "Prof Gurvin Kaur"},
                "T3": {"subject": "ML", "room": "C-51", "professor": "Prof Deepa Agarwal"},
                "T4": {"subject": "CCL", "room": "A-51", "professor": "Prof ABC"}
            }},
            {"time": "1:15-3:15", "subject": "SEPM", "room": "B-53", "professor": "Prof Samrin Pabrekar"},
        ],
        "4th Year": [
            {"time": "08:30-09:30", "subject": "RS", "room": "B-54", "professor": "Prof Deepa Agarwal"},
            {"time": "08:30-09:30", "subject": "SMA", "room": "B-54", "professor": "Prof Sachin Narkhade"},
            {"time": "09:30-10:30", "subject": "AFB", "room": "B-54", "professor": "Prof XYZ"},
            {"time": "09:30-10:30", "subject": "EM", "room": "B-54", "professor": "Prof GKS"},
            {"time": "10:30-11:30", "subject": "FM", "room": "B-41", "professor": "Prof Sachin Narkhade"},
            {"time": "11:30-12:30", "subject": "AAI", "room": "B-54", "professor": "Dr Nilesh Bhelkar"},
            {"time": "1:15-3:15", "subject": "Lab", "groups": {
                "B3": {"subject": "AFB", "room": "C-51", "professor": "Prof XYZ"},
                "B4": {"subject": "AAI", "room": "C-51", "professor": "Dr Nilesh Bhelkar"}
            }}        
            ],
    },
    "Friday": {
        "2nd Year": [
            {"time": "08:30-10:30", "subject": "Lab", "groups": {
                "S1": {"subject": "MP", "room": "A-51", "professor": "Prof RA"},
                "S2": {"subject": "DBMS", "room": "A-53", "professor": "Dr Jyoti Deshmukh"},
                "S3": {"subject": "OS", "room": "A-51", "professor": "Prof Divya Tama"},
                "S4": {"subject": "PY", "room": "C-53", "professor": "Prof Bharti Jadhav"}
            }},
            {"time": "10:30-11:30", "subject": "OS", "room": "B-53", "professor": "Prof Divya Tama"},
            {"time": "11:30-12:30", "subject": "EM-4", "room": "B-53", "professor": "Prof Sarla Yadav"},
            {"time": "1:15-2:15", "subject": "AOA", "room": "B-53", "professor": "Prof ABC"},
            {"time": "2:15-3:15", "subject": "PY", "room": "B-53", "professor": "Prof XYZ"},
        ],
        "3rd Year": [
            {"time": "08:30-09:30", "subject": "ML", "room": "B-54", "professor": "Dr Nilesh Bhelkar"},
            {"time": "09:30-10:30", "subject": "SEPM", "room": "B-54", "professor": "Prof Samrin Pabrekar"},
            {"time": "10:30-12:30", "subject": "Lab", "groups": {
                "T1": {"subject": "SEPM", "room": "A-53", "professor": "Dr Jyoti Deshmukh"},
                "T2": {"subject": "CSS", "room": "A-53", "professor": "Prof Gurvin Kaur"},
                "T3": {"subject": "CCL", "room": "A-51", "professor": "Prof ABC"},
                "T4": {"subject": "ML", "room": "C-51", "professor": "Prof Deepa Agarwal"}
            }},
            {"time": "1:15-3:30", "subject": "Lab", "groups": {
                "T1": {"subject": "CCL", "room": "A-51", "professor": "Prof Sachin Narkhade"},
                "T4": {"subject": "ML", "room": "C-51", "professor": "Prof Deepa Agarwal"},
                "T3": {"subject": "SEPM", "room": "C-53", "professor": "Prof Samrin Pabrekar"},
                "T4": {"subject": "DAV", "room": "A-53", "professor": "Prof Gurvin Kaur"}
            }}
        ],
        "4th Year": [
            {"time": "08:30-12:30", "subject": "Miniproject 3B"}
        ],
    }
    
}

def get_today_classes():
    """Returns today's classes"""
    today = datetime.datetime.today().strftime("%A")  # Get current day
    return timetable.get(today, {})

def get_current_class():
    """Returns the class currently happening"""
    now = datetime.datetime.now().time()  # Get current time
    today_classes = get_today_classes()

    for year, schedule in today_classes.items():
        for entry in schedule:
            if "time" in entry:
                try:
                    start, end = entry["time"].split("-")
                    start_time = datetime.datetime.strptime(start, "%H:%M").time()
                    end_time = datetime.datetime.strptime(end, "%H:%M").time()

                    if start_time <= now <= end_time:
                        # Check if it's a lab session
                        if "groups" in entry:
                            return year, entry["subject"], entry["groups"]
                        return year, entry["subject"], {"room": entry.get("room", "N/A"), "professor": entry.get("professor", "N/A")}
                except ValueError as e:
                    print(f"Error parsing time: {entry['time']}. Skipping entry. Error: {e}")

    return None, None, None  # No active class

class SEARCHROOMS_PT_TimetablePanel(bpy.types.Panel):
    """Creates a Panel in the 3D Viewport that displays only the ongoing class"""
    bl_label = "Ongoing Class"
    bl_idname = "SEARCHROOMS_PT_timetable_panel"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = 'Timetable'  # Adds a new tab in the sidebar

    def draw(self, context):
        layout = self.layout
        year, subject, details = get_current_class()

        if subject:
            layout.label(text=f"Current Class ({year}):")
            layout.label(text=f"{subject}")

            if isinstance(details, dict) and "room" in details:
                layout.label(text=f"Room: {details['room']}")
                layout.label(text=f"Prof: {details['professor']}")
            else:
                layout.label(text="Lab Groups:")
                for group, group_details in details.items():
                    layout.label(text=f"{group}: {group_details['subject']} in {group_details['room']} ({group_details['professor']})")
        else:
            layout.label(text="No class is happening right now.")

# Register classes
def register():
    bpy.utils.register_class(SEARCHROOMS_PT_TimetablePanel)

def unregister():
    bpy.utils.unregister_class(SEARCHROOMS_PT_TimetablePanel)

if __name__ == "__main__":
    register()