# import cv2
# import numpy as np
#
# cap = cv2.VideoCapture(0)
# while True:
#     rt, frame = cap.read()
#     if rt:
#         res1 = np.fliplr(frame)
#         if res1.shape[:][1]%2 != 0:
#             res1 = res1[:,:-1]
#         height, width = res1.shape[:2]
#         width2 = width//2
#         res2=res1[:,:width2]
#         res1[:,width2:] = np.fliplr(res2)
#         cv2.imshow('res2', res1)
#         cv2.waitKey(1)


import tkinter
import cv2
import PIL.Image, PIL.ImageTk
import time

class App:
    def __init__(self, window, window_title, video_source=0):
        self.window = window
        self.window.title(window_title)
        self.video_source = 0

        # open video source (by default this will try to open the computer webcam)
        self.vid = MyVideoCapture(self.video_source)

        # Create a canvas that can fit the above video source size
        self.canvas = tkinter.Canvas(window, width = self.vid.width, height = self.vid.height)
        self.canvas.pack()

        # 화면 캡쳐 버튼
        # # Button that lets the user take a snapshot
        # self.btn_snapshot=tkinter.Button(window, text="Snapshot", width=50, command=self.snapshot)
        # self.btn_snapshot.pack(anchor=tkinter.CENTER, expand=True)

        # After it is called once, the update method will be automatically called every delay milliseconds

        self.delay = 15
        self.update()

        self.window.mainloop()

    # 화면 캡쳐 기능
    # def snapshot(self):
    #     # Get a frame from the video source
    #     ret, frame = self.vid.get_frame()
    #
    #     if ret:
    #         cv2.imwrite("frame-" + time.strftime("%d-%m-%Y-%H-%M-%S") + ".jpg", cv2.cvtColor(frame, cv2.COLOR_RGB2BGR))

    def update(self):
        # Get a frame from the video source
        ret, frame = self.vid.get_frame()

        if ret:
            self.photo = PIL.ImageTk.PhotoImage(image = PIL.Image.fromarray(frame))
            self.canvas.create_image(0, 0, image = self.photo, anchor = tkinter.NW)
            self.window.after(self.delay, self.update)


class MyVideoCapture:
    def __init__(self, video_source=0):
        # Open the video source
        self.vid = cv2.VideoCapture(video_source)
        if not self.vid.isOpened():
            raise ValueError("Unable to open video source", video_source)

        # Get video source width and height
        self.width = self.vid.get(cv2.CAP_PROP_FRAME_WIDTH)
        self.height = self.vid.get(cv2.CAP_PROP_FRAME_HEIGHT)

    def get_frame(self):
        if self.vid.isOpened():
            ret, frame = self.vid.read()
            if ret:
                # Return a boolean success flag and the current frame converted to BGR
                return (ret, cv2.cvtColor(frame, cv2.COLOR_BGR2RGB))
            else:
                return (ret, None)
        else:
            # return (ret, None)
            pass


# Create a window and pass it to the Application object
App(tkinter.Tk(), "Tkinter and OpenCV")