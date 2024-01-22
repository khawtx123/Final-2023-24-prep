import cv2
import os
import numpy as np
import tkinter as tk
from tkinter import filedialog
from tkinter import Canvas
import subprocess

# Global variables
ran = False
drawing = False
resizing = False
rectangles = []
current_rect = None
roi_x, roi_y, roi_width, roi_height = -1, -1, -1, -1
valid_png_directories = set()

drawingCircle = False
center = (-1, -1)
radius = -1

roi_width = ""
roi_height = ""

root = tk.Tk()
root.title("ROI Preview")
canvas = Canvas(root, bg="white", width=400, height=400)
canvas.pack()

def chooseFile():
    # Create a Tkinter root window (you can hide it if you want)
    root = tk.Tk()
    root.withdraw()

    # Open a file dialog for selecting a file
    file_path = filedialog.askopenfilename(title="Select a file")

    if file_path:
        print("Selected file:", file_path)
    else:
        print("No file selected")

    # You can also use asksaveasfilename for saving files
    # file_path = filedialog.asksaveasfilename(title="Save a file")

    # Don't forget to close the Tkinter main loop if you're not using it
    root.quit()
    return file_path

nice_photo = chooseFile()
image = tk.PhotoImage(file=nice_photo)  # Replace with your image file (supports GIF)
# Insert the image into the canvas
image_id = canvas.create_image(200, 200, image=image)

def chooseDir():
    # Create a Tkinter root window (you can hide it if you want)
    root = tk.Tk()
    root.withdraw()

    # Open a file dialog for selecting a file
    file_path = filedialog.askdirectory(title= "select Directory")

    if file_path:
        print("Selected file:", file_path)
    else:
        print("No file selected")

    # You can also use asksaveasfilename for saving files
    # file_path = filedialog.asksaveasfilename(title="Save a file")

    # Don't forget to close the Tkinter main loop if you're not using it
    root.quit()
    return file_path


def saveFile():
    # Create a Tkinter root window (you can hide it if you want)
    root = tk.Tk()
    root.withdraw()

    # Open a file dialog for selecting a file
    file_path = filedialog.asksaveasfilename(title="Save a file")

    if file_path:
        print("Selected file:", file_path)
    else:
        print("No file selected")

    # You can also use asksaveasfilename for saving files
    # file_path = filedialog.asksaveasfilename(title="Save a file")

    # Don't forget to close the Tkinter main loop if you're not using it
    root.quit()
    return file_path


def draw_circle(event, x, y, flags, param):
    global drawing, center, radius

    if event == cv2.EVENT_LBUTTONDOWN:
        drawing = True
        center = (x, y)

    elif event == cv2.EVENT_MOUSEMOVE:
        if drawing:
            radius = int(np.sqrt((x - center[0])**2 + (y - center[1])**2))

    elif event == cv2.EVENT_LBUTTONUP:
        drawing = False


def draw_rectangle(event, x, y, flags, param):
    global drawing, resizing, current_rect, roi_x, roi_y, roi_width, roi_height

    if event == cv2.EVENT_LBUTTONDOWN:
        drawing = True
        resizing = False
        for rect in rectangles:
            if rect[0] < x < rect[0] + rect[2] and rect[1] < y < rect[1] + rect[3]:
                resizing = True
                current_rect = rect
                break

        if not resizing:
            current_rect = [x, y, 0, 0]

    elif event == cv2.EVENT_MOUSEMOVE:
        if drawing:
            current_rect[2] = x - current_rect[0]
            current_rect[3] = y - current_rect[1]

    elif event == cv2.EVENT_LBUTTONUP:
        drawing = False
        if current_rect[2] < 0:
            current_rect[0] += current_rect[2]
            current_rect[2] = abs(current_rect[2])
        if current_rect[3] < 0:
            current_rect[1] += current_rect[3]
            current_rect[3] = abs(current_rect[3])
        rectangles.append(current_rect)
        current_rect = None


def draw_Rect_ROI():
    image_path = chooseFile()
    output_path = "C:\\Users\\thong-xiang.khaw\\Documents\\a1\\solderJoint\\cropped.jpg"

    global rectangles, current_rect, roi_x, roi_y, roi_width, roi_height, valid_png_directories

    image = cv2.imread(image_path)
    clone = image.copy()
    cv2.namedWindow("Draw and Resize Rectangles")
    cv2.setMouseCallback("Draw and Resize Rectangles", draw_rectangle)

    while True:
        temp = clone.copy()

        for rect in rectangles:
            cv2.rectangle(temp, (rect[0], rect[1]), (rect[0] + rect[2], rect[1] + rect[3]), (0, 255, 0), 2)

        if current_rect is not None:
            cv2.rectangle(temp, (current_rect[0], current_rect[1]), (current_rect[0] + current_rect[2], current_rect[1] + current_rect[3]), (0, 0, 255), 2)
            roi_x, roi_y, roi_width, roi_height = current_rect[0], current_rect[1], current_rect[2], current_rect[3]

        cv2.imshow("Draw and Resize Rectangles", temp)
        key = cv2.waitKey(1) & 0xFF

        if key == 27:  # 'Esc' key to exit
            break
        elif key == ord("c"):  # 'c' key to clear rectangles
            rectangles = []

        elif key == ord("s"):  # 's' key to save the drawn ROI
            if roi_width > 0 and roi_height > 0:
                roi = image[roi_y:roi_y + roi_height, roi_x:roi_x + roi_width]
                output_path = saveFile()

                height, width, _ = image.shape
                mask = np.full((height, width, 3), 255, dtype=np.uint8)

                # Draw a white rectangle on the mask at the same position as the drawn rectangle
                cv2.rectangle(mask, (roi_x, roi_y), (roi_x + roi_width, roi_y + roi_height), (0, 0, 0), thickness=cv2.FILLED)

                # Extract the region defined by the drawn rectangle from the original image using the mask
                extracted_roi = cv2.bitwise_and(image, mask)

                # Save the masked region as a separate image
                cv2.imwrite(output_path, mask)
                cv2.imshow("mask", mask)
                cv2.waitKey(0)
                print("Masked ROI saved as 'extracted_roi.png'")

            break

    cv2.destroyAllWindows()

    # You can access the ROI coordinates and size here (roi_x, roi_y, roi_width, roi_height)

    print(f"ROI Coordinates: x={roi_x}, y={roi_y}, Width={roi_width}, Height={roi_height}")


def draw_circ_ROI():
    global drawingCircle, center, radius
    image_path = chooseFile()
    output_path = "C:\\Users\\thong-xiang.khaw\\Documents\\a1\\solderJoint\\cropped.jpg"
    image = cv2.imread(image_path)
    cv2.namedWindow("Draw and Save ROI")
    cv2.setMouseCallback("Draw and Save ROI", draw_circle)
    while True:
        temp = image.copy()

        if radius > 0:
            cv2.circle(temp, center, radius, (0, 0, 255), 2)

        cv2.imshow("Draw and Save ROI", temp)
        key = cv2.waitKey(1) & 0xFF

        if key == 27:  # 'Esc' key to exit
            break
        elif key == ord("c"):  # 'c' key to clear the circle
            center = (-1, -1)
            radius = -1
        elif key == ord("s"):  # 's' key to save the drawn circular ROI
            if radius > 0:
                output_path = saveFile()

                # Create a mask for the circular ROI
                height, width, _ = image.shape
                mask = np.full((height, width, 3), 255, dtype=np.uint8)
                cv2.circle(mask, center, radius, (0, 0, 0), thickness=cv2.FILLED)

                # Extract the region defined by the circular ROI from the original image using the mask
                roi = cv2.bitwise_and(image, mask)

                # Save the masked region as a separate image
                cv2.imwrite(output_path, mask)
                cv2.imshow("mask", mask)
                cv2.waitKey(0)
                print(f"ROI saved as {output_path}")
                break

    cv2.destroyAllWindows()
    print(f"ROI Coordinates: x={roi_x}, y={roi_y}, Width={roi_width}, Height={roi_height}")


def moving_mask():
      # Function to process the user input
    def process_input():
        global roi_width, roi_height
        roi_width = entry1.get()
        roi_height = entry2.get()
        result = f"ROI size: {roi_width} px x {roi_height} px"
        print(result)
        roi_width = int(roi_width)
        roi_height = int(roi_height)

        image_path = chooseFile()
        larger_image = cv2.imread(image_path)
        height, width, _ = larger_image.shape
        # Define the dimensions and initial position of the subimage (ROI)
        roi_x, roi_y = 0, 0

        # Create a black mask with the same size as the larger image
        mask = np.zeros_like(larger_image)

        # Create a window
        cv2.namedWindow("Moving Mask")

        while True:
            # Create a copy of the larger image
            image_copy = larger_image.copy()
            traverse_speed = int(roi_width/10)
            # Draw a white rectangle on the mask at the current position of the subimage
            mask = np.zeros_like(larger_image)
            cv2.rectangle(mask, (roi_x, roi_y), (roi_x + roi_width, roi_y + roi_height), (255, 255, 255), thickness=cv2.FILLED)

            # Extract the subimage from the larger image using the mask
            subimage = cv2.bitwise_and(image_copy, mask)

            # Display the subimage with the moving mask
            cv2.imshow("Moving Mask", subimage)
            roi = image_copy[roi_y:roi_y + roi_height, roi_x:roi_x + roi_width]

            # Create a new window with the size of the extracted image
            cv2.namedWindow("Extracted Image", cv2.WINDOW_NORMAL)
            cv2.resizeWindow("Extracted Image", roi_width, roi_height)

            # Display the extracted image in the new window
            cv2.imshow("Extracted Image", roi)

            key = cv2.waitKey(1) & 0xFF

            if key == 27:  # 'Esc' key to exit
                break

            # Update the position of the subimage (move it)
            if key == ord("d"):
                roi_x += traverse_speed

            elif key == ord("a"):
                roi_x -= traverse_speed

            elif key == ord("s"):
                roi_y += traverse_speed

            elif key == ord("w"):
                roi_y -= traverse_speed

        print(f"ROI Coordinates: x={roi_x}, y={roi_y}, Width={roi_width}, Height={roi_height}")
        directory = os.path.dirname(image_path)

        save_directory = chooseDir()
        # List all files in the directory
        all_files = os.listdir(directory)

        # Filter for JPG files
        jpg_files = [file for file in all_files if file.endswith(".jpg")]

        i = 0
        # Print the list of JPG files
        for jpg_file in jpg_files:
            jpg_file_path = os.path.join(directory, jpg_file)
            image = cv2.imread(jpg_file_path)
            image_copy = image.copy()
            roi = image_copy[roi_y:roi_y + roi_height, roi_x:roi_x + roi_width]
            if i<10:
                filepath = save_directory + "/extracted_roi" + "0" + str(i) + ".jpg"
            else:
                filepath = save_directory + "/extracted_roi" + str(i) + ".jpg"
            print(filepath)
            cv2.imwrite(filepath, roi)
            cv2.imshow("extracted roi", roi)
            cv2.waitKey(0)
            i += 1
        cv2.destroyAllWindows()

    new_window = tk.Toplevel(root)
    new_window.title("ROI Width and Height")
    canvas = tk.Canvas(new_window, width=200, height=100)
    canvas.pack()

    # Create an entry widget for user input
    entry1 = tk.Entry(new_window)
    entry2 = tk.Entry(new_window)

    entry1.pack()
    entry2.pack()

    # Create a button to process the input
    submit_button = tk.Button(new_window, text="Submit", command=process_input)

    submit_button.pack()

    center_x = canvas.winfo_reqwidth() // 2
    center_y = canvas.winfo_reqheight() // 2

    user_prompt = "Enter ROI width and height \n suggested value: 1000 x 1000"
    canvas.create_text(center_x, center_y, text=user_prompt)


def find_circles():
    image_path = chooseFile()
    image = cv2.imread(image_path)
    brightness = 50

    # Create a matrix of zeros with the same dimensions as the image
    # This will be used to increase the brightness
    increased_brightness = np.zeros(image.shape, dtype=np.uint8)

    # Add the specified brightness to each channel (BGR)
    increased_brightness = cv2.add(image, (brightness, brightness, brightness, 0))

    cv2.destroyAllWindows()

    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Apply Gaussian blur to reduce noise
    gray = cv2.GaussianBlur(gray, (9, 9), 2)

    # Detect circles using Hough Circle Transform
    circles = cv2.HoughCircles(
        gray,            # Input grayscale image
        cv2.HOUGH_GRADIENT,  # Detection method (Hough Gradient)
        dp=1,             # Inverse ratio of the accumulator resolution
        minDist=100,       # Minimum distance between the centers of the detected circles
        param1=50,        # Upper threshold for edge detection
        param2=30,        # Threshold for center detection
        minRadius=10,      # Minimum radius to be detected
        maxRadius=10000       # Maximum radius to be detected
    )

    # If circles are found, draw them on the image
    if circles is not None:
        height, width, _ = image.shape
        mask = np.full((height, width, 3), 0, dtype=np.uint8)
        circles = np.uint16(np.around(circles))
        for circle in circles[0, :]:
            center = (circle[0], circle[1])
            radius = circle[2]
            cv2.circle(image, center, radius, (0, 255, 0), 5)  # Draw the circle
            cv2.circle(mask, center, radius, (255, 255, 255), -1)

        # Display the result
        cv2.imshow('Circles Detected', image)
        cv2.imshow('Circles Mask', mask)

        output_file = saveFile()
        cv2.imwrite(output_file, mask)
        cv2.waitKey(0)
        cv2.destroyAllWindows()

def run_stereo():
    executable_path = chooseFile()
    try:
        subprocess.run([executable_path], check=True)
    except subprocess.CalledProcessError as e:
        print(f"Error: {e}")

def show_window():
    global ran, canvas

    if not ran:
        # Create a canvas for drawing the rectangle

        canvas_width = canvas.winfo_reqwidth()
        canvas_height = canvas.winfo_reqheight()
        center_x = canvas_width // 2
        center_y = canvas_height // 2

        button_frame = tk.Frame(canvas)

        # Place the frame in the center of the canvas
        button_frame.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

        # Create a button and add it to the window
        extract_button = tk.Button(button_frame, text="Extract ROI", command=moving_mask)
        rect_button = tk.Button(button_frame, text="Rectangle Mask", command=draw_Rect_ROI)
        circ_button = tk.Button(button_frame, text="Circular Mask", command=draw_circ_ROI)
        chrome_button = tk.Button(button_frame, text="Find chrome mask", command=find_circles)
        run_stereo_button = tk.Button(button_frame, text="Run Stereo", command=run_stereo)

        extract_button.pack(padx=10, pady=10)
        rect_button.pack(padx=10, pady=10)
        circ_button.pack(padx=10, pady=10)
        chrome_button.pack(padx=10, pady=10)
        run_stereo_button.pack(padx=10, pady=10)
        ran = True
        # Start the tkinter main loop
    root.mainloop()


if __name__ == "__main__":
    while(True):
        show_window()
    # Input image path

