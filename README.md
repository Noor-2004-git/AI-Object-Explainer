# AI Object Explainer

## Overview

AI Object Explainer is a real-time computer vision application that detects everyday objects using YOLOv8 and generates AI-powered descriptions using Google's Gemini API. The application captures an image from the webcam, identifies objects, and explains their purpose, common uses, and interesting facts through an interactive web interface.

<img width="932" height="947" alt="Screenshot 2026-06-27 170318" src="https://github.com/user-attachments/assets/66c3c080-f203-49f1-bf2f-3a7149a27c60" />
<img width="936" height="768" alt="Screenshot 2026-06-27 170449" src="https://github.com/user-attachments/assets/4b810428-28f2-4f0d-8335-de6c21f4089d" />
<img width="945" height="847" alt="Screenshot 2026-06-27 170204" src="https://github.com/user-attachments/assets/20daf005-2a6a-48b1-8f28-f01c649eee52" />
<img width="930" height="797" alt="Screenshot 2026-06-27 170249" src="https://github.com/user-attachments/assets/c096463a-df7a-42c4-a340-11db941b843b" />




## Features

* Real-time webcam integration
* Object detection using YOLOv8
* AI-generated object explanations using Gemini
* Flask-based backend
* Interactive web interface
* Supports detection of multiple everyday objects

## Tech Stack

* Python
* Flask
* OpenCV
* Ultralytics YOLOv8
* Google Gemini API
* HTML
* CSS
* JavaScript

## Project Workflow

Webcam
→ Capture Image
→ Flask Backend
→ YOLOv8 Object Detection
→ Gemini AI Explanation
→ Display Result

## Folder Structure

```
AI-Object-Explainer/
│── app.py
│── detector.py
│── gemini_helper.py
│── requirements.txt
│── README.md
│── .gitignore
│
├── templates/
│     └── index.html
│
├── static/
│     ├── script.js
│     └── style.css
│
├── uploads/
│
└── model/
      └── yolov8n.pt
```

## Installation

### Clone the repository

```bash
git clone https://github.com/your-username/AI-Object-Explainer.git
cd AI-Object-Explainer
```

### Create a virtual environment

Windows

```bash
python -m venv venv
venv\Scripts\activate
```

### Install dependencies

```bash
pip install -r requirements.txt
```

### Configure Gemini API

Create a `.env` file in the project root.

```
GEMINI_API_KEY=YOUR_API_KEY
```

### Run the application

```bash
python app.py
```

Open:

```
http://127.0.0.1:5000
```

## Example

1. Open the web application.
2. Allow camera access.
3. Point the camera toward an object.
4. Click **Capture Image**.
5. View the AI-generated explanation.

## Future Improvements

* Live object detection without capturing images
* AR-style floating labels
* Detection confidence display
* Voice-based explanation
* Detection history
* Mobile-friendly interface

## License

This project is intended for educational and portfolio purposes.

## Author
Noor Tandon
B Tech Computer Engineering
