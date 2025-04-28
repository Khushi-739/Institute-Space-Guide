import bpy
import os
import mathutils  # Correct import

# Define search properties
class SearchProperties(bpy.types.PropertyGroup):
    search_text: bpy.props.StringProperty(name="Search Room")

# UI Panel
class SEARCH_PT_Panel(bpy.types.Panel):
    bl_label = "Search for a Room"
    bl_idname = "SEARCH_PT_panel"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = "Search Rooms"

    def draw(self, context):
        layout = self.layout
        props = context.scene.search_props

        layout.prop(props, "search_text")

        search_text = props.search_text.lower()
        global rooms  

        for room, info in rooms.items():
            if search_text in room.lower():
                box = layout.box()
                box.label(text=room)
                box.label(text=f"WiFi: {info.get('WiFi', 'Unknown')}")
                professors = info.get("Professor", "Unknown")
                if isinstance(professors, list):
                    professors = ", ".join(professors)
                box.label(text=f"Professor: {professors}")
                facilities = info.get("Facilities", "N/A")
                if isinstance(facilities, list):
                    facilities = ", ".join(facilities)
                box.label(text=f"Facilities: {facilities}")

                if "Location" in info:
                    box.operator("view3d.zoom_to_room", text="Zoom").room_name = room

# Operator to move camera (Zoom feature)
class VIEW3D_OT_ZoomToRoom(bpy.types.Operator):
    bl_idname = "view3d.zoom_to_room"
    bl_label = "Zoom to Room"

    room_name: bpy.props.StringProperty()

    def execute(self, context):
        room_info = rooms.get(self.room_name, {})
        if not room_info or "Location" not in room_info:
            self.report({'ERROR'}, "No location data available for this room")
            return {'CANCELLED'}

        target_x, target_y, target_z = room_info["Location"]
        target_rotation = room_info.get("Rotation", (0, 0, 0))  # Ensure default rotation

        camera = bpy.context.scene.camera
        if not camera:
            self.report({'ERROR'}, "No active camera found")
            return {'CANCELLED'}

        # Move the camera to the specified room location
        camera.location = (target_x, target_y, target_z)
        camera.rotation_euler = mathutils.Euler(target_rotation, 'XYZ')  # Corrected rotation assignment

        bpy.context.view_layer.update()

        self.report({'INFO'}, f"Camera moved to {self.room_name} at {target_x:.2f}, {target_y:.2f}, {target_z:.2f}")
        return {'FINISHED'}

# Room data
rooms = {
    "B54 Smart Classroom": {
        "WiFi": "Unavailable", 
        "Location": (3.16, 1.10, 3.43),
        "Rotation": (-1.57, -3.14, 3.14)
    },
    "B53 Smart Classroom": {
        "WiFi": "Unavailable",  
        "Location": (-3.41, 1.10, 3.43),
        "Rotation": (-1.57, -3.14, 3.14)
    },
    "B52 Classroom": {
        "WiFi": "Unavailable", 
        "Location": (-9.55, 1.10, 3.43),
        "Rotation": (-1.57, -3.14, 3.14)
    },
    "B50 Classroom": {
        "WiFi": "Unavailable", 
        "Location": (-15.96, 1.10, 3.43),
        "Rotation": (-1.57, -3.14, 3.14)
    },
    "A54 Cloud Computing Lab": {
        "WiFi": "Available", 
        "Facilities": ["High-end PCs", "Printer"], 
        "Professor": ["Prof XYZ, Prof ABC, Prof RA"], 
        "Location": (5.5313, 6.5532, 3.43),
        "Rotation": (-1.57, -3.14, 1.57)
    },
    "A53 Database & Data Science Lab": {
        "WiFi": "Available", 
        "Facilities": ["High-end PCs", "Printer"], 
        "Professor": ["Dr Jyoti Deshmukh", "Prof Samrin Pabrekar", "Prof Divya Tama"], 
        "Location": (5.5313, -0.78725, 3.43),
        "Rotation": (-1.57, -3.14, 1.57)
    },
    "C51 aiml lab": {
        "WiFi": "Available",
        "Facilities": ["Prof Gurvin Kaur", "Prof Sachin Narkhede","Prof Divya "], 
        "Professor": "Dr. Smith",
        "Location": (-18.508, -0.54514, 3.43),
        "Rotation": (-1.57,-3.14,4.71)
    },
    "C53 project lab": {
        "WiFi": "Not Available",
        "Facilities": ["High-end PCs", "Printer"], 
        "Professor": ["Dr Nilesh Bhelkar","Prof Bharti Jadhav"],
        "Location": (-18.508, 5.7981, 3.43),
        "Rotation": (-1.57,-3.14,4.71)
    }
}

def register():
    bpy.utils.register_class(SearchProperties)
    bpy.utils.register_class(SEARCH_PT_Panel)
    bpy.utils.register_class(VIEW3D_OT_ZoomToRoom)
    bpy.types.Scene.search_props = bpy.props.PointerProperty(type=SearchProperties)

def unregister():
    bpy.utils.unregister_class(SearchProperties)
    bpy.utils.unregister_class(SEARCH_PT_Panel)
    bpy.utils.unregister_class(VIEW3D_OT_ZoomToRoom)
    del bpy.types.Scene.search_props

if __name__ == "__main__":
    register()