import cv2
import socket
import pickle

def receive_video():
    # Create a socket object
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Define the IP address and port number to bind the socket
    receiver_ip = '192.168.43.75'  # IP address of Device B
    receiver_port = 12345

    # Bind the socket to the IP address and port number
    s.bind((receiver_ip, receiver_port))

    # Listen for incoming connections
    s.listen(1)

    # Accept a connection from the sender
    conn, addr = s.accept()

    # Create an empty frame to store the received frame
    frame = b''

    while True:
        # Receive the length of the serialized frame as 4 bytes
        frame_size_bytes = conn.recv(4)

        # Break the loop if no more data is received
        if not frame_size_bytes:
            break

        # Convert the frame size bytes to an integer
        frame_size = int.from_bytes(frame_size_bytes, byteorder='big')

        while len(frame) < frame_size:
            # Receive the serialized frame data
            data = conn.recv(frame_size - len(frame))

            # Break the loop if no more data is received
            if not data:
                break

            # Append the received data to the frame
            frame += data

        # Try to reconstruct the frame
        try:
            # Deserialize the frame using pickle
            frame_data = pickle.loads(frame)

            # Display the received frame
            cv2.imshow("Video", frame_data)

        except pickle.UnpicklingError:
            continue

        # Clear the frame for the next iteration
        frame = b''

        # Break the loop if 'q' is pressed
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # Close the connection and destroy the window
    conn.close()
    cv2.destroyAllWindows()

# Call the function to receive the video
receive_video()
