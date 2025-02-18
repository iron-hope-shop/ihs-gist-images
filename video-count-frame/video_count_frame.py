"""
Title: Video Frame Counter for Texture Animations in Blender
Author: Brad Jackson
Date: 02/18/2025
Description:
    This script uses OpenCV to count the total number of frames in a given video file.
    It is specifically designed to assist in creating texture animations for Blender by
    providing an accurate frame count. Although originally intended for COCO-SSD annotations,
    this tool can be adapted for any image recognition model.

Technical Highlights:
    - Leverages OpenCV (cv2) for robust video processing.
    - Retrieves the frame count efficiently using cv2.VideoCapture and CAP_PROP_FRAME_COUNT.
    - Seamlessly integrates with Blender for generating texture animations.
    - Compatible across multiple platforms (Windows, macOS, Linux).
    - Minimal dependency: only opencv-python is required.

How to Run:
    1. (Optional but recommended) Set up a Python virtual environment:
         - On Windows:
               python -m venv env
               env\Scripts\activate
         - On macOS/Linux:
               python3 -m venv env
               source env/bin/activate
    2. Install the required dependency:
         pip install opencv-python
    3. Update the 'path_to_your_video.mp4' in the code to point to your video file.
    4. Run the script:
         python video_frame_counter.py

    Gist: https://gist.github.com/iron-hope-shop/4dee2bc66267c170deddbbc8b639e84d

License: MIT License

MIT License
Copyright (c) 2025 Brad Jackson

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:
The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.
THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
"""

# First, ensure you have OpenCV installed:
# pip install opencv-python

import cv2

# Open the video file. Replace 'path_to_your_video.mp4' with the actual path to your video.
cap = cv2.VideoCapture('path_to_your_video.mov')

# Check if the video file was successfully opened.
if not cap.isOpened():
    print("Error opening video file")
    exit()

# Retrieve the total number of frames in the video using CAP_PROP_FRAME_COUNT.
frame_count = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
print("Total frames:", frame_count)

# Release the video capture object to free up resources.
cap.release()
