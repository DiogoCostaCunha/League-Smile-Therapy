import json
import cv2
import dlib
import numpy as np
import time
from terminate_league_client import terminate_league_client
import pygame
detector = dlib.get_frontal_face_detector()
predictor = dlib.shape_predictor("shape_predictor_68_face_landmarks.dat")

def create_progress_bar(width=100, height=300):
    bar = np.ones((height, width, 3), dtype=np.uint8) * 255
    cv2.rectangle(bar, (10, 10), (width-10, height-10), (0, 0, 0), 2)
    return bar

def update_progress_bar(bar, progress, width=100, height=300):
    bar_copy = bar.copy()
    fill_height = int((height - 20) * progress)
    cv2.rectangle(bar_copy, (10, height-10-fill_height), (width-10, height-10), (0, 255, 0), -1)
    cv2.putText(bar_copy, f"{int(progress * 100)}%", (10, height-20), 
                cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 0), 2)
    return bar_copy

def get_eye_region(frame, landmarks, start_idx, end_idx):
    eye_points = np.array([[landmarks.part(i).x, landmarks.part(i).y] for i in range(start_idx, end_idx)])
    
    x_min = np.min(eye_points[:, 0]) - 10
    x_max = np.max(eye_points[:, 0]) + 10
    y_min = np.min(eye_points[:, 1]) - 10
    y_max = np.max(eye_points[:, 1]) + 10
    
    x_min = max(0, x_min)
    x_max = min(frame.shape[1], x_max)
    y_min = max(0, y_min)
    y_max = min(frame.shape[0], y_max)
    
    return frame[int(y_min):int(y_max), int(x_min):int(x_max)]

def get_smile_region(frame, rect, landmarks):
    mouth_points = np.array([[landmarks.part(i).x, landmarks.part(i).y] for i in range(48, 68)])
    
    x_min = np.min(mouth_points[:, 0]) - 10
    x_max = np.max(mouth_points[:, 0]) + 10
    y_min = np.min(mouth_points[:, 1]) - 10
    y_max = np.max(mouth_points[:, 1]) + 10
    
    x_min = max(0, x_min)
    x_max = min(frame.shape[1], x_max)
    y_min = max(0, y_min)
    y_max = min(frame.shape[0], y_max)
    
    return frame[int(y_min):int(y_max), int(x_min):int(x_max)]

def calculate_eye_aspect_ratio(landmarks, start_idx, end_idx):
    eye_points = np.array([[landmarks.part(i).x, landmarks.part(i).y] for i in range(start_idx, end_idx)])
    
    eye_width = np.linalg.norm(eye_points[3] - eye_points[0])
    eye_height = np.linalg.norm(eye_points[1] - eye_points[4])
    
    return eye_width / eye_height

def calculate_mouth_aspect_ratio(landmarks, start_idx, end_idx):
    mouth_points = np.array([[landmarks.part(i).x, landmarks.part(i).y] for i in range(start_idx, end_idx)])
    
    mouth_width = np.linalg.norm(mouth_points[6] - mouth_points[0])
    mouth_height = np.linalg.norm(mouth_points[9] - mouth_points[3])
    
    return mouth_width / mouth_height

def detect_smile(landmarks, mouth_ratio_threshold=1.8, eyes_ratio_threshold=2.3):
    left_eye_ratio = calculate_eye_aspect_ratio(landmarks, 36, 42)
    right_eye_ratio = calculate_eye_aspect_ratio(landmarks, 42, 48)
    mouth_ratio = calculate_mouth_aspect_ratio(landmarks, 48, 68)
    
    mouth_condition = mouth_ratio > 1.8
    eyes_ratio_mean = (left_eye_ratio + right_eye_ratio) / 2
    eyes_condition = eyes_ratio_mean > 2.3
    
    return mouth_condition and eyes_condition

def main():
    cap = cv2.VideoCapture(-0)
    pygame.mixer.init()
    pygame.mixer.music.load("assets/fart.mp3")

    cv2.namedWindow("Smile Region", cv2.WINDOW_NORMAL)
    cv2.namedWindow("Left Eye", cv2.WINDOW_NORMAL)
    cv2.namedWindow("Right Eye", cv2.WINDOW_NORMAL)
    cv2.namedWindow("Smile Progress", cv2.WINDOW_NORMAL)

    cv2.moveWindow("Smile Region", 50, 100)
    cv2.moveWindow("Left Eye", 0, 0)
    cv2.moveWindow("Right Eye", 150, 0)
    cv2.moveWindow("Smile Progress", 1300, 50)

    cv2.resizeWindow("Smile Region", 300, 75)
    cv2.resizeWindow("Left Eye", 100, 50)
    cv2.resizeWindow("Right Eye", 100, 50)
    cv2.resizeWindow("Smile Progress", 100, 300)

    cv2.setWindowProperty("Smile Region", cv2.WND_PROP_TOPMOST, 1)
    cv2.setWindowProperty("Left Eye", cv2.WND_PROP_TOPMOST, 1) 
    cv2.setWindowProperty("Right Eye", cv2.WND_PROP_TOPMOST, 1)
    cv2.setWindowProperty("Smile Progress", cv2.WND_PROP_TOPMOST, 1)

    with open("config.json", "r") as f:
        config = json.load(f)
    
    progress_bar = create_progress_bar()
    current_progress = 1.0
    last_update_time = time.time()

    decay_rate = config["decay_rate"]   
    fill_rate = config["fill_rate"]
    mouth_ratio_threshold = config["mouth_ratio_threshold"]
    eyes_ratio_threshold = config["eyes_ratio_threshold"]
    
    while True:
        ret, frame = cap.read()
        if not ret:
            break
            
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        
        faces = detector(gray)
        
        for face in faces:
            landmarks = predictor(gray, face)
            
            smile_region = get_smile_region(frame, face, landmarks)
            left_eye_region = get_eye_region(frame, landmarks, 36, 42)
            right_eye_region = get_eye_region(frame, landmarks, 42, 48)
            
            is_smiling = detect_smile(landmarks, mouth_ratio_threshold=mouth_ratio_threshold, eyes_ratio_threshold=eyes_ratio_threshold)
            
            current_time = time.time()
            time_diff = current_time - last_update_time
            last_update_time = current_time
            
            if is_smiling:
                current_progress = min(1.0, current_progress + fill_rate * time_diff)
            else:
                current_progress = max(0.0, current_progress - decay_rate * time_diff)

            if current_progress == 0:
                pygame.mixer.music.play()
                terminate_league_client()
                time.sleep(3)
                exit()
            
            x, y = face.left(), face.top()
            x2, y2 = face.right(), face.bottom()
            color = (0, 255, 0) if is_smiling else (0, 0, 255)
            cv2.rectangle(frame, (x, y), (x2, y2), color, 2)
        
            text = "Smiling" if is_smiling else "Not Smiling"
            cv2.putText(frame, text, (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, color, 2)
            
            if smile_region.size > 0:
                cv2.imshow("Smile Region", smile_region)
            
            if left_eye_region.size > 0:
                cv2.imshow("Left Eye", left_eye_region)
            
            if right_eye_region.size > 0:
                cv2.imshow("Right Eye", right_eye_region)

            progress_bar_updated = update_progress_bar(progress_bar, current_progress)
            cv2.imshow("Smile Progress", progress_bar_updated)
        
        if cv2.waitKey(1) & 0xFF == ord('z'):
            break
    
    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main() 