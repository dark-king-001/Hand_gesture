# Snake Game
<p align="center">
  <img src="https://github.com/dark-king-001/Snake_Game/blob/main/Snapshots/Snake%20Game.png" alt="Snake Game" />
</p>
<p align="center">
  <h4 align="center">Be Smart with a hand gesture system control</h4>
</p>


## About The Project

### Overview

This script allows you to control the system volume using hand gestures recognized by a computer vision model. It uses the MediaPipe library for hand tracking and a pre-trained model for gesture recognition.

### Features


- **Increase Volume**: Thumbs Up: Increases the system volume.
- **Decrease Volume**: Thumbs Down: Decreases the system volume.

### Dependencies

- **Hardware Access**: The script will start capturing the video from the webcam and display the output frame.
- **System Requirements**: Make sure your system has audio capabilities and the necessary audio drivers are installed for volume control to work properly.

### Purpose

To learn concepts of OOPS in a Fun and Interesting ways.

## Build With
- [https://img.shields.io/badge/Python%203.6%20-Python%20Programming%20Language%20-green?style=flat&logo=SG](https://img.shields.io/badge/Python%203.6%20-Python%20Programming%20Language%20-green?style=flat&logo=SG)
- [TensorFlow]
- [Keras]

## Getting Started

### Installation

1. Clone the repo: 
```sh
git clone https://github.com/dark-king-001/Hand_gesture.git
```
2. Install the required packages:
```sh
pip install opencv-python numpy mediapipe tensorflow keras
```
3. Enter the Folder: 
```sh
cd Hand_gesture
```
4. run the game: 
```sh
python main.py
```

## Additional libraries

- [OpenCV]
- [NumPy]
- [MediaPipe]

## License
* This project is licensed under the MIT License.

## Troubleshooting
* If the script fails to capture frames from the webcam, make sure the webcam is connected and functional.
* If the hand landmarks are not detected accurately, try adjusting the min_detection_confidence parameter in the script to a lower value.

## Project Images

- **Running Game**
  ![Running Game](https://github.com/dark-king-001/Hand_gesture/blob/main/Snapshots/Directory%20Structure.png)

- **Directory Snapshot**
  ![Directory Snapshot](https://github.com/dark-king-001/Hand_gesture/blob/main/Snapshots/Directory%20Snapshot.png)
  