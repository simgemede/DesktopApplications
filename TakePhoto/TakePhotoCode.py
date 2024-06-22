import tkinter as tk
import cv2
import uuid

def takePhoto():
    ret, frame = video_capture.read()
    if ret:
        fileName = str(uuid.uuid4()) + ".png"
        cv2.imwrite(fileName, frame)
        print(f"The photo was saved: {fileName}")

def exitApp():
    video_capture.release()
    window.quit()

window = tk.Tk()
window.title("Take Photo")
window.geometry("400x300")
window.resizable(False, False)

video_source = 0
video_capture = cv2.VideoCapture(video_source)

frame = tk.Frame(window)
frame.place(relx = 0.5, rely = 0.5, anchor = tk.CENTER)

buton_TakePhoto = tk.Button(frame, text="Take Photo", width=20, command=takePhoto)
buton_TakePhoto.pack(padx = 20, pady = 10)

buton_Exit = tk.Button(frame, text="Exit", width=20, command=exitApp)
buton_Exit.pack(padx = 20, pady = 10)

window.mainloop()