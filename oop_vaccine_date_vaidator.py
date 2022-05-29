import tkinter as tk
import cv2
import pytesseract
import re
from datetime import datetime, timedelta
from PIL import Image,ImageTk
import time


class Page(tk.Frame):
    pytesseract.pytesseract.tesseract_cmd = r"C:\Users\wasda\Desktop\CODES\Tesseract-OCR\tesseract.exe"
    tdy = datetime.today()
    allowed = tdy - timedelta(days=14)
    img2str_config = "--psm 1"
    cap = cv2.VideoCapture(0)
    flag=None
    def __init__(self, *args, **kwargs):
        tk.Frame.__init__(self, *args, **kwargs)

    def show(self):
        self.lift()


class VaccineValidator(Page):
    def __init__(self, *args, **kwargs):
        Page.__init__(self, *args, **kwargs)

        self.img1 = None
        self.count = 0
        Page.flag=None

        frame_left = tk.Frame(self)
        frame_left.place(relx=0,rely=0,relwidth=0.8,relheight=1)
        self.img_label = tk.Label(frame_left,bg="white")
        self.img_label.place(relx=0,rely=0,relwidth=1,relheight=1)

        frame_right = tk.Frame(self,bg="white")
        frame_right.place(relx=0.8,rely=0,relwidth=0.2,relheight=1)
        self.canvas = tk.Canvas(frame_right, bd=0, highlightthickness=0, bg="white")#"#0a1529"
        self.canvas.create_oval(55,20,155,120,fill='gray',outline='gray')
        self.canvas.place(relx=0,rely=0,relwidth=1,relheight=0.2)

        validate_dates_button = tk.Button(frame_right,text="Validate Dates",command= lambda: self.validate_dates(self.img1))
        validate_dates_button.place(relx=0,rely=0.2,relwidth=1,relheight=0.1)

        self.dates_label = tk.Label(frame_right,text="",font="Helvetica 35 bold")
        self.dates_label.place(relx=0,rely=0.3,relwidth=1,relheight=0.1)

        self.people_count = tk.Label(frame_right,text="",font="Helvetica 35 bold")
        self.people_count.place(relx=0,rely=0.4,relwidth=1,relheight=0.1)

    def show_images(self):
        Page.flag = True
        ret, img = Page.cap.read()
        #img = cv2.rotate(img,cv2.ROTATE_90_CLOCKWISE)
        self.img1 = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        img_show = Image.fromarray(self.img1)
        imgtk = ImageTk.PhotoImage(image=img_show)
        self.img_label.imgtk = imgtk
        self.img_label.configure(image=imgtk)
        self.show()
        self.img_label.after(10, self.show_images)
        if Page.flag == False:
            time.sleep(1)
            return 0

    def validate_dates(self,img):
        self.img = img
        try:
            res_string = pytesseract.image_to_string(self.img, config=Page.img2str_config)
            regex = re.findall(r'\d\d ... \d\d\d\d', res_string)
            dates = [datetime.strptime(i, "%d %b %Y") for i in regex]
            print(dates)
            if dates[1] < Page.allowed :
                self.dates_label['text'] = "ALLOWED"
                self.dates_label['fg'] = "green"
                self.canvas.create_oval(55,20,155,120,fill='#39e600',outline='#39e600')
                self.count += 1
                self.people_count['text'] = f'{self.count}'
            else:
                self.dates_label['text'] = "NOT ALLOWED"
                self.dates_label['fg'] = "red"
                self.canvas.create_oval(55,20,155,120,fill='red',outline='red')
        except Exception as e:
            print(e)
            self.dates_label['text'] = "CHECK"
            self.dates_label['fg'] = "yellow"
            self.canvas.create_oval(55,20,155,120,fill='yellow',outline='yellow')


class MainView(tk.Frame):
    def __init__(self, *args, **kwargs):
        tk.Frame.__init__(self, *args, **kwargs)

        vv = VaccineValidator()

        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)

        vv.place(in_=container, relx=0, rely=0.05, relwidth=1, relheight=1)

        frame_top = tk.Frame(self,)
        frame_top.place(relx=0,rely=0,relwidth=1,relheight=0.05)
        vv.show_images()
        

if __name__ == "__main__":
    root = tk.Tk()
    root.title("Validator")
    main = MainView(root)
    main.pack(side="top", fill="both", expand=True)
    root.wm_geometry("1920x1080")
    root.mainloop()
