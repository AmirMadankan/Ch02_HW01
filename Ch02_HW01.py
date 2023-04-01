import cv2
import numpy as np
import time

t0 = time.time()

cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    if ret:
        t1 = time.time() - t0
        t1_str = str(round(t1, 2))
        frame = cv2.flip(frame, 1)
        text = f"Amir Madankan {t1_str}"
        cv2.putText(frame, text, (100, 100), cv2.FONT_HERSHEY_SIMPLEX, 
                    1, (0, 0, 255), 1)
        frame_LD = 255 - frame
        frame_RD = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        n = frame_RD.shape[0]
        m = frame_RD.shape[1]
        frame_RD = frame_RD.reshape((n, m, 1))
        frame_RD = np.concatenate([frame_RD, frame_RD, frame_RD], 2)
        frame_RU = frame.copy()      
        frame_RU[:, :, 2] = 255
        frame_new1 = np.concatenate((frame, frame_RU), axis=1)
        frame_new2 = np.concatenate((frame_LD, frame_RD), axis=1)
        frame_new = np.concatenate((frame_new1, frame_new2), axis=0)
        cv2.imshow("webcam", frame_new)
        q = cv2.waitKey(1)
        if q == ord("q"):
            break

cv2.destroyAllWindows()
cap.release()