import cv2
import socket #low level interface for network communication
import pickle #serialise object to byte then back to object


def send_video():
    # Open a video capture object
    cap = cv2.VideoCapture(0)  # 0 for the default camera
    # Check if the camera is opened correctly
    if not cap.isOpened():
        print("Cannot open camera")
        return

    # Create a socket object
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #socket for low level netwrok interface
    #ipv4 ,#socket type

    # Define the IP address and port number of the receiver
    receiver_ip = '192.168.43.129'  # IP address of Device B
    receiver_port = 12345

    # Connect to the receiver
    s.connect((receiver_ip, receiver_port))

    while True:
        # Read frame-by-frame from the camera
        ret, frame = cap.read()

        # Serialize the frame using pickle
        data = pickle.dumps(frame)

        # Send the length of the serialized frame as 4 bytes
        frame_size = len(data)
        s.sendall(frame_size.to_bytes(4, byteorder='big'))

        # Send the serialized frame over the network
        s.sendall(data)

        # Break the loop if 'q' is pressed
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # Release the video capture object and close the socket
    cap.release()
    s.close()


# Call the function to send the video
send_video()
