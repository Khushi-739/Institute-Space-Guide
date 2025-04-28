Institute Space Guide Using Machine Learning

Overview

The Institute Space Guide is a comprehensive 3D interactive navigation and academic management system developed using Blender 4.0 and Python (bpy). Designed for the university environment, it allows students and faculty to virtually explore the department floor, access real-time room schedules, and interact with the campus environment in a seamless manner. The system also integrates a sentiment-based feedback mechanism and a parent-teacher communication feature powered by Google Firebase Firestore and Twilio SMS API. The project aims to enhance campus accessibility, improve communication between stakeholders, and streamline academic organization.

Key Features

This system features a fully interactive 3D floor model developed in Blender, enabling users to navigate the college department virtually with zoom and search capabilities. Real-time academic schedules are integrated into the system, allowing students and faculty to stay updated with class timings and faculty availability. A sentiment analysis-based feedback system, developed using TextBlob, enables students and faculty to provide valuable input, which is analyzed and categorized to generate actionable insights. The project also introduces a real-time student progress tracking system, where teachers can submit performance updates directly to Firebase, and parents receive instant notifications through Twilio’s SMS service. All data exchanges are secured with encrypted storage and role-based access control to maintain user privacy and system integrity.

Technology Stack

The project is built primarily using Blender 4.0 for 3D modeling and user interaction. Python 3.x serves as the programming backbone, utilizing the Blender Python API (bpy) for scripting dynamic interactions and the Mathutils library for precise 3D manipulations. Cloud-based data management is handled through Google Firebase Firestore, while real-time SMS notifications are managed using Twilio’s API. Sentiment analysis for feedback is performed using the TextBlob library. Together, these technologies ensure a responsive, reliable, and secure platform for campus navigation and communication.

System Architecture

The architecture of the system is designed to offer an immersive and intuitive user experience. The front-end provides a highly detailed 3D model interface, allowing users to interact with classrooms and laboratories in real time. Backend services, including data storage and notifications, are managed through cloud platforms like Firebase and Twilio. Dynamic interactions, such as schedule updates and feedback processing, are scripted using Python libraries. The system emphasizes real-time data synchronization, secure information access, and an intuitive user interface to create a unified academic management experience.

Future Enhancements

Future development plans include integrating AI-driven voice assistance to further improve accessibility, enabling users to navigate and retrieve information through voice commands. Expanding the project to cover the entire campus instead of a single department will create a more holistic solution. The addition of Augmented Reality (AR) features and real-time classroom occupancy tracking will further enhance the system's usability. Implementation of Multi-Factor Authentication (MFA) and mobile application development are also planned to ensure better security and wider accessibility across devices.

Contributors

This project was developed by Arjun Dangle, Sharvari Kamble, Om Kendre, and Gargi Khurud under the guidance of Prof. Samrin Pabrekar. It was carried out as a part of the curriculum for the Department of Artificial Intelligence and Data Science at the University of Mumbai.
