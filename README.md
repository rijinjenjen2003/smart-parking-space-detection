# 🚗 Smart Parking Space Detection System

A Computer Vision project built using Python, OpenCV, and Streamlit that automatically detects occupied and vacant parking spaces from parking lot images.

## Features

✅ Parking slot occupancy detection

✅ Free parking space counting

✅ OpenCV image processing

✅ ROI-based parking slot analysis

✅ Streamlit web application

✅ Color-coded visualization

- 🔴 Occupied Slot
- 🟢 Empty Slot

## Technologies Used

- Python
- OpenCV
- NumPy
- Streamlit
- Pickle

## How It Works

1. Select parking slots using mouse clicks.
2. Store parking slot coordinates using Pickle.
3. Upload parking lot image.
4. Process each parking slot individually.
5. Apply:
   - Grayscale Conversion
   - Gaussian Blur
   - Thresholding
   - Dilation
6. Count white pixels.
7. Determine occupancy status.
8. Display available parking spaces.

## Project Structure

parking-space-detector/

├── app.py

├── ParkingSpacePicker.py

├── parkingdetector.py

├── position.pkl

├── requirements.txt

└── README.md

## Future Improvements

- Real-time video detection
- YOLO-based vehicle detection
- Occupancy percentage dashboard
- Parking analytics
- Multi-camera support

## Author

Rijin Jenjen
