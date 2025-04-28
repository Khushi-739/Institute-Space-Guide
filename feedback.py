import bpy
import smtplib
import os
from email.mime.text import MIMEText
from textblob import TextBlob  # NLP for sentiment analysis

# Store feedback in the user's home directory
FEEDBACK_FILE = os.path.join(os.path.expanduser("~"), "feedback_log.txt")

class FeedbackPanel(bpy.types.Panel):
    bl_label = "User Feedback"
    bl_idname = "PT_Feedback"
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"
    bl_category = "Feedback"

    def draw(self, context):
        layout = self.layout
        layout.label(text="Submit Your Feedback:")
        layout.prop(context.scene, "user_name")
        layout.prop(context.scene, "user_email")
        layout.prop(context.scene, "feedback_text")
        layout.operator("feedback.submit")
        layout.separator()
        layout.operator("feedback.view")

class SubmitFeedbackOperator(bpy.types.Operator):
    bl_idname = "feedback.submit"
    bl_label = "Submit Feedback"

    def execute(self, context):
        user_name = context.scene.user_name
        user_email = context.scene.user_email
        feedback_text = context.scene.feedback_text
        
        # Perform sentiment analysis
        sentiment = TextBlob(feedback_text).sentiment.polarity
        sentiment_label = "Positive" if sentiment > 0 else "Neutral" if sentiment == 0 else "Negative"
        
        try:
            with open(FEEDBACK_FILE, "a") as file:
                file.write(f"User: {user_name} ({user_email})\nFeedback: {feedback_text}\nSentiment: {sentiment_label}\n---\n")
            self.report({'INFO'}, f"Feedback submitted! Sentiment: {sentiment_label}")
        except PermissionError:
            self.report({'ERROR'}, "Permission denied: Cannot write feedback.")
        
        return {'FINISHED'}

class ViewFeedbackOperator(bpy.types.Operator):
    bl_idname = "feedback.view"
    bl_label = "View Feedback"

    def execute(self, context):
        try:
            with open(FEEDBACK_FILE, "r") as file:
                feedback_data = file.read()
            self.report({'INFO'}, "Feedback loaded. Check console.")
            print(feedback_data)
            send_feedback_email(feedback_data, context.scene.user_email)
        except FileNotFoundError:
            self.report({'WARNING'}, "No feedback found.")
        except PermissionError:
            self.report({'ERROR'}, "Permission denied: Cannot read feedback.")
        
        return {'FINISHED'}

def send_feedback_email(feedback_data, sender_email):
    sender_email =  "khushi.kamble739@gmail.com"  # Fixed sender email
    sender_password = "esvmiujcosgyoxkt"  # App Password
    receiver_email = "khushi.kamble739@gmail.com"
    subject = "New Feedback Received"
    body = f"Here is the latest feedback:\n\n{feedback_data}"

    msg = MIMEText(body)
    msg["Subject"] = subject
    msg["From"] = sender_email
    msg["To"] = receiver_email

    smtp_server = "smtp.gmail.com"
    smtp_port = 587

    try:
        print("Connecting to SMTP server...")
        with smtplib.SMTP(smtp_server, smtp_port) as server:
            server.starttls()
            print("Logging in with sender email:", sender_email)
            server.login(sender_email, sender_password)
            print("Sending email...")
            server.sendmail(sender_email, receiver_email, msg.as_string())
        print("Feedback email sent successfully to:", receiver_email)
    except smtplib.SMTPAuthenticationError:
        print("ERROR: Authentication failed. Check your App Password.")
    except smtplib.SMTPConnectError:
        print("ERROR: Could not connect to SMTP server.")
    except Exception as e:
        print(f"Failed to send email: {e}")

def register():
    bpy.utils.register_class(FeedbackPanel)
    bpy.utils.register_class(SubmitFeedbackOperator)
    bpy.utils.register_class(ViewFeedbackOperator)
    bpy.types.Scene.user_name = bpy.props.StringProperty(name="Name")
    bpy.types.Scene.user_email = bpy.props.StringProperty(name="Email")
    bpy.types.Scene.feedback_text = bpy.props.StringProperty(name="Feedback")

def unregister():
    bpy.utils.unregister_class(FeedbackPanel)
    bpy.utils.unregister_class(SubmitFeedbackOperator)
    bpy.utils.unregister_class(ViewFeedbackOperator)
    del bpy.types.Scene.user_name
    del bpy.types.Scene.user_email
    del bpy.types.Scene.feedback_text

if __name__ == "__main__":
    register()