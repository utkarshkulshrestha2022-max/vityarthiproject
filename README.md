Project Title : Road Lane Detection Using Image Segmentation

Overview of the Project : This project aims to detect road lane markings from driving videos using classical image segmentation techniques. It does not use deep learning; instead, it works with methods like edge detection, thresholding, masking, and filtering. The goal is to highlight lane boundaries in real-time, helping improve road safety and assisting basic driver-assistance systems. The project takes a video as input, processes each frame, extracts the lane region, and displays the detected lanes on the screen.

Features : Processes real videos and identifies lane boundaries , Uses classical image segmentation methods (Canny, masking, thresholding) , Real-time frame-by-frame lane extraction , Simple and lightweight—runs on normal computers , Easy to modify and extend , Clean and readable code for learning purposes.

Technologies / Tools Used : Python 3 , OpenCV for image processing , NumPy for numerical operations , VS Code / any Python IDE , Git & GitHub for version control.

Steps to Install & Run the Project : 
Install Python : Make sure Python 3 is installed on your system.
Install required libraries : Run this in terminal: pip install opencv-python numpy
Download or clone the project : git clone https://github.com/yourusername/vityarthiproject.git cd vityarthiproject
Add your video file : Place the video (e.g., video1.mp4) in the project folder.
Run the Python script : python3 project.py
The output window will show the processed frames with detected lanes.

Instructions for Testing : Use any real road driving video (daytime works best). Try different driving environments: Straight roads , Curvy roads , Highways , Local streets
Compare how segmentation performs with: Bright sunlight , Shadows , Road turns
Adjust Canny thresholds in code to improve detection.

output screenshots: <img width="633" height="394" alt="Image" src="https://github.com/user-attachments/assets/a6525ff1-761b-4162-9e7d-61bc42ec6d2a" />

<img width="634" height="392" alt="Image" src="https://github.com/user-attachments/assets/93695cf5-5f7d-489d-9f6a-6d6f031152b3" />

<img width="1469" height="924" alt="Image" src="https://github.com/user-attachments/assets/62abb70f-b367-439e-b97e-ac4304f661d9" />
