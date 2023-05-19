# import necessary packages
#%%
import cv2
import numpy as np
import mediapipe as mp
import tensorflow as tf
from keras.models import load_model
import time
print("Num GPUs Available: ", len(tf.config.list_physical_devices('GPU')))
    # Place your code that requires GPU acceleration here
#%%
# initialize mediapipe
mpHands = mp.solutions.hands
hands = mpHands.Hands(max_num_hands=1, min_detection_confidence=0.7)
mpDraw = mp.solutions.drawing_utils

# Load the gesture recognizer model
model = load_model(r'mp_hand_gesture')

# Load class names
f = open(r'gesture.names', 'r')
classNames = f.read().split('\n')
f.close()
print(classNames)


# Initialize the webcam
cap = cv2.VideoCapture(0)
#%%
# initialize mediapipe
mpHands = mp.solutions.hands
hands = mpHands.Hands(max_num_hands=1, min_detection_confidence=0.7)
mpDraw = mp.solutions.drawing_utils

# Load the gesture recognizer model
model = load_model(r'mp_hand_gesture')

# Load class names
f = open(r'gesture.names', 'r')
classNames = f.read().split('\n')
f.close()
print(classNames)

# Initialize the webcam
cap = cv2.VideoCapture(0)

# Initialize volume variables
volume = 0  # Current volume level
volume_step = 10  # Volume change step size

with tf.device('/device:GPU:0'):
    while True:
        time.sleep(0.016)
        # Read each frame from the webcam
        ret, frame = cap.read()
        _, frame = cap.read()

        if not ret:
            # Handle the case where frame capture fails
            # Print an error message or break out of the loop
            print("Failed to capture frame from the webcam")
            break
        x, y, c = frame.shape

        # Flip the frame vertically
        frame = cv2.flip(frame, 1)
        framergb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

        # Get hand landmark prediction
        result = hands.process(framergb)

        # print(result)

        className = ''

        # post process the result
        if result.multi_hand_landmarks:
            landmarks = []
            for handslms in result.multi_hand_landmarks:
                for lm in handslms.landmark:
                    # print(id, lm)
                    lmx = int(lm.x * x)
                    lmy = int(lm.y * y)

                    landmarks.append([lmx, lmy])

                # Drawing landmarks on frames
                mpDraw.draw_landmarks(frame, handslms, mpHands.HAND_CONNECTIONS)

                # Predict gesture
                prediction = model.predict([landmarks])
                # print(prediction)
                classID = np.argmax(prediction)
                className = classNames[classID]
        if className == 'thumbs up':
            volume += volume_step
            wk.Worker(f'amixer set Master {volume}%')
        if className == 'thumbs down':
            volume -= volume_step
            wk.Worker(f'amixer set Master {volume}%')

        # show the prediction on the frame
        cv2.putText(frame, f"{className}{volume})", (10, 50), cv2.FONT_HERSHEY_SIMPLEX,
                1, (0, 0, 255), 2, cv2.LINE_AA)

        # Show the final output
        cv2.imshow("Output", frame) 

        if cv2.waitKey(1) == ord('q'):
            break

    # release the webcam and destroy all active windows
    cap.release()

    cv2.destroyAllWindows()
    # %%
