import bpy
import os
from twilio.rest import Client
import firebase_admin
from firebase_admin import credentials, firestore

# ---- Firebase Initialization with Named App ----
FIREBASE_KEY_PATH = r"D:\Blender\stuff\parent-b66ad-firebase-adminsdk-fbsvc-da327b0af0.json"
APP_NAME = "portal_app"

# Check if Firebase app is already initialized
if APP_NAME not in firebase_admin._apps:
    cred = credentials.Certificate(FIREBASE_KEY_PATH)
    firebase_admin.initialize_app(cred, name=APP_NAME)

# Access Firestore with the named app
app = firebase_admin.get_app(APP_NAME)
db = firestore.client(app)

# ---- Twilio Configuration ----
TWILIO_ACCOUNT_SID = "AC15a93fd814afadf83b6e0fec5250fe02"
TWILIO_AUTH_TOKEN = "8c58655b486a6601b0f0ef7fd6fd5f05"
TWILIO_PHONE_NUMBER = "+16089039653"  # Twilio active number 

# ---- Utility Functions ----

def format_phone_number(phone):
    """Ensure phone number is in E.164 format (+country_code)."""
    if not phone.startswith('+'):
        phone = f"+{phone}"
    return phone

def send_sms(phone, message):
    """Send SMS via Twilio with error handling."""
    try:
        client = Client(TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN)
        
        phone = format_phone_number(phone)  # Ensure E.164 format

        sms = client.messages.create(
            body=message,
            from_=TWILIO_PHONE_NUMBER,
            to=phone
        )

        print(f" SMS sent to {phone}: {sms.sid}")

    except Exception as e:
        print(f"❌ Failed to send SMS: {e}")

# ---- Parent Registration Panel ----
class ParentLoginPanel(bpy.types.Panel):
    bl_label = "Parent Login"
    bl_idname = "PANEL_PT_ParentLogin"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = "Portal"

    def draw(self, context):
        layout = self.layout
        scene = context.scene

        layout.label(text="Parent Registration")
        layout.prop(scene, "parent_name")
        layout.prop(scene, "parent_password")
        layout.prop(scene, "parent_phone")

        row = layout.row()
        row.operator("portal.register_parent", text="Register")


# ---- Register Parent Operator ----
class RegisterParentOperator(bpy.types.Operator):
    bl_idname = "portal.register_parent"
    bl_label = "Register Parent"

    def execute(self, context):
        scene = context.scene
        name = scene.parent_name.strip()
        password = scene.parent_password.strip()
        phone = scene.parent_phone.strip()

        if name and password and phone:
            try:
                # Store parent info in Firebase
                doc_ref = db.collection('parents').document(phone)
                doc_ref.set({
                    'name': name,
                    'password': password,
                    'phone': phone
                })

                # Send SMS notification
                message = f"Hello {name}, you have successfully registered in the Parent Portal."
                send_sms(phone, message)

                self.report({'INFO'}, f"Parent {name} registered and notified!")

            except Exception as e:
                self.report({'ERROR'}, f"Error: {e}")

        else:
            self.report({'WARNING'}, " Please fill all fields!")

        return {'FINISHED'}


# ---- Teacher Portal Panel ----
class TeacherPortalPanel(bpy.types.Panel):
    bl_label = "Teacher Portal"
    bl_idname = "PANEL_PT_TeacherPortal"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = "Portal"

    def draw(self, context):
        layout = self.layout
        scene = context.scene

        layout.label(text="Enter Student Progress")
        layout.prop(scene, "student_name")
        layout.prop(scene, "parent_phone")
        layout.prop(scene, "student_marks")
        layout.prop(scene, "student_suggestions")

        row = layout.row()
        row.operator("portal.save_student_data", text="Save & Notify")


# ---- Save Student Data Operator ----
class SaveStudentDataOperator(bpy.types.Operator):
    bl_idname = "portal.save_student_data"
    bl_label = "Save Student Progress"

    def execute(self, context):
        scene = context.scene
        student_name = scene.student_name.strip()
        parent_phone = scene.parent_phone.strip()
        marks = scene.student_marks.strip()
        suggestions = scene.student_suggestions.strip()

        if student_name and parent_phone and marks:
            try:
                # Store student progress in Firebase
                doc_ref = db.collection('students').document(student_name)
                doc_ref.set({
                    'parent_phone': parent_phone,
                    'marks': marks,
                    'suggestions': suggestions
                })

                # Send SMS notification to parent
                message = (
                    f"Progress Report for {student_name}:\n"
                    f"Marks: {marks}\n"
                    f"Suggestions: {suggestions}"
                )
                
                send_sms(parent_phone, message)

                self.report({'INFO'}, f" Progress saved and notification sent for {student_name}!")

            except Exception as e:
                self.report({'ERROR'}, f" Error: {e}")
        else:
            self.report({'WARNING'}, " Please fill all fields!")

        return {'FINISHED'}

# ---- Register Properties and Panels ----
def register():
    bpy.utils.register_class(ParentLoginPanel)
    bpy.utils.register_class(RegisterParentOperator)
    bpy.utils.register_class(TeacherPortalPanel)
    bpy.utils.register_class(SaveStudentDataOperator)

    # Register custom properties with default values
    bpy.types.Scene.parent_name = bpy.props.StringProperty(name="Parent Name", default="")
    bpy.types.Scene.parent_password = bpy.props.StringProperty(name="Password", subtype='PASSWORD', default="")
    bpy.types.Scene.parent_phone = bpy.props.StringProperty(name="Phone Number", default="")

    bpy.types.Scene.student_name = bpy.props.StringProperty(name="Student Name", default="")
    bpy.types.Scene.student_marks = bpy.props.StringProperty(name="Marks", default="")
    bpy.types.Scene.student_suggestions = bpy.props.StringProperty(name="Suggestions", default="")

    print(" Portal registered successfully!")


def unregister():
    bpy.utils.unregister_class(ParentLoginPanel)
    bpy.utils.unregister_class(RegisterParentOperator)
    bpy.utils.unregister_class(TeacherPortalPanel)
    bpy.utils.unregister_class(SaveStudentDataOperator)

    del bpy.types.Scene.parent_name
    del bpy.types.Scene.parent_password
    del bpy.types.Scene.parent_phone
    del bpy.types.Scene.student_name
    del bpy.types.Scene.student_marks
    del bpy.types.Scene.student_suggestions

    print("Portal unregistered!")


if __name__ == "__main__":
    register()
