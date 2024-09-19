# Smart-Attendance-Monitoring-System
The **Smart Attendance System** leverages **face recognition technology** to automate the process of recording attendance. Instead of relying on manual entry or RFID card systems, this system uses real-time **facial detection and recognition** to identify individuals and mark their attendance.

**Face Detection:**

The system uses OpenCV to detect faces from a live video feed or captured images.

**Data Storage:**

The system maintains a database of users, typically consisting of their face encodings and associated metadata (e.g., name, ID).

**Attendance Marking:**

Once a face is recognized, the system logs the user's name and timestamp.
Attendance is marked either on a daily or session basis, and this data can be exported as a CSV file or viewed through a dashboard.
