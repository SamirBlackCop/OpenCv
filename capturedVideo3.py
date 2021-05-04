import cv2
#cap = cv2.VideoCapture(0) it will record the video from webcam
cap = cv2.VideoCapture(r"E:\video\4_5868212613933963640.mkv");

print(cap.get(cv2.CAP_PROP_FRAME_WIDTH))  # this will provide the info about width and height
print(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

#while(True):
while cap.isOpened():
    ret, frame = cap.read()  # cap.read() will provide true and frame simultaneously

    """gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    cv2.imshow(("Movie with grays", gray))"""
    # it wll play the video the in grayscale



    """font = cv2.FONT_ITALIC
    text="Widh: " + str(cap.get(3)) + ' height: '+ str(cap.get(4))                          # cap.get(3) == cap.get(cv2.CAP_PROP_FRAME_WIDTH)
    frame = cv2.putText(frame, text, (10, 50), font, 1, (0,255, 255), 2, cv2.LINE_AA)"""    # cap.get(3) == cap.get(cv2.CAP_PROP_FRAME_HEIGHT)
    # it will print text on video and



    cv2.imshow('frame', frame)

    if cv2.waitKey(1) == ord('q'):  # exit from the video if q is pressed
        break

cap.release()
cv2.destroyAllWindows()