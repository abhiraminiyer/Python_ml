import cv2

vid = cv2.VideoCapture(0) #port number
while True:
    ret, frame = vid.read()
    image = cv2.putText(frame, "welcome to ai mi class", (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (255,255,255), 5,
                        cv2.LINE_AA)
    # image,message,coordinate,font type,fontscale,color(bgr),thickness,keyword
    cv2.imshow("live video", image)  # first parameter is window name second is image
    if (cv2.waitKey(1) & 0xFF == ord('q')):
        print("i am here")
        break  # if pass then it will not terminate from the loop
vid.release()
cv2.destroyAllWindows()
