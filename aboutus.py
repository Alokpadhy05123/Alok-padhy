from tkinter import *
import cv2

from tkinter import *


class Frames(object):
    def newFrame(self):

        cap = cv2.VideoCapture(0)
        ret, frame = cap.read()
        while (True):
            cv2.imshow('img1', frame)
            if cv2.waitKey(1) & 0xFF == ord('y'):
                cv2.imwrite('outputimages/c1.png', frame)
                cv2.destroyAllWindows()
                break

        cap.release()

    def mainFrame(self, root):
        self.query = StringVar()  # passing parameter via query var

        root.title('EMOJIFY!!!')


        root.resizable(0, 0)

        label1 = Label(root, text="EMOJIFY", bg="#E74C3C", fg="white", font="Times").pack()
        label2 = Label(root, text="Under the guidance of Prof.Sudhir kumar Pattanaik", font="Times").pack()
        label3 = Label(root, text="Aanchal kumari pani . ....", font="Times").pack()
        label4 = Label(root, text="Alok padhy", font="Times").pack()
        label5 = Label(root, text=".................", font="Times").pack()
        label6 = Label(root, text=".............", font="Times").pack()


root = Tk()
app = Frames()
app.mainFrame(root)
root.mainloop()







class Frames(object):
    def newFrame(self):

        cap = cv2.VideoCapture(0)
        ret,frame = cap.read()

        while(True):
            cv2.imshow('img1',frame)
            if cv2.waitKey(1) & 0xFF == ord('y'):
                cv2.imwrite('outputimages/c1.png',frame)
                cv2.destroyAllWindows()
                break

        cap.release()


mainloop()





