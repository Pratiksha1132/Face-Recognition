import cv2
import mediapipe as mp

# drawing utility
mp_drawing = mp.solutions.drawing_utils
# Face detection utility
mp_face_detection = mp.solutions.face_detection
# model for detecting face
model_detection = mp_face_detection.FaceDetection()

cap = cv2.VideoCapture('vidmp4.mp4')

while cap.isOpened():
    flag, frame = cap.read()
    if not flag:
        print("could not access the camera")
        break

    results = model_detection.process(cv2.cvtColor(frame, cv2.COLOR_BGR2RGB))
    for landmark in results.detections:
        print(mp_face_detection.get_key_point(landmark, mp_face_detection.FaceKeyPoint.NOSE_TIP))
        mp_drawing.draw_detection(frame, landmark)
    cv2.imshow('Frame', frame)
    if cv2.waitKey(10) & 0xff == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()