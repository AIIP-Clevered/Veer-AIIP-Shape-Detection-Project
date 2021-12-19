import cv2
from tkinter import*
from tkinter import filedialog
from PIL import Image, ImageTk

def upload_file():
    global img
    global filename
    f_types = [('jpg Files', '*.jpg'),('png Files','*.png')]
    filename = filedialog.askopenfilename(filetypes=f_types)
    print(filename)
    img = ImageTk.PhotoImage(file=filename)
    b2 =Button(tk,image=img) # using Button
    b2.pack()




def openthewindow():
    img = cv2.imread(filename)
    imgGrey = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    _, thrash = cv2.threshold(imgGrey, 240, 255, cv2.THRESH_BINARY)
    contours, _ = cv2.findContours(thrash, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)

    for contour in contours:
        approx = cv2.approxPolyDP(contour, 0.01*cv2.arcLength(contour, True), True)
        cv2.drawContours(img, [approx], 0, (0, 0, 0), 5)
        x = approx.ravel() [0]
        y = approx.ravel() [1]
        if len(approx) == 3:
            cv2.putText(img, "Triangle", (x, y), cv2.FONT_HERSHEY_COMPLEX, 0.5, (0, 0, 0))
        elif len(approx) == 4:
            cv2.putText(img, "Rectangle", (x, y), cv2.FONT_HERSHEY_COMPLEX, 0.5, (0, 0, 0))
        elif len(approx) == 5:
            cv2.putText(img, "Pentagon", (x, y), cv2.FONT_HERSHEY_COMPLEX, 0.5, (0, 0, 0))
        elif len(approx) == 10:
            cv2.putText(img, "Decagon", (x, y), cv2.FONT_HERSHEY_COMPLEX, 0.5, (0, 0, 0))
        elif len(approx) == 6:
            cv2.putText(img, "Hexagon", (x, y), cv2.FONT_HERSHEY_COMPLEX, 0.5, (0, 0, 0))
        elif len(approx) == 8:
            cv2.putText(img, "Octagon", (x, y), cv2.FONT_HERSHEY_COMPLEX, 0.5, (0, 0, 0))
        else:
            cv2.putText(img, "Circle", (x, y), cv2.FONT_HERSHEY_COMPLEX, 0.5, (0, 0, 0))
    cv2.imshow("shapes", img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

tk = Tk()
Lbl=Label(text='AI SHAPE DETECTION',bd = 7,font=("comic sans",30,"bold",),bg='#0099cc',fg='white',relief='raised')
Lbl.pack()
btn=Button(tk,text='Upload Image' , command=upload_file,bd = 7,font=("comic sans",30,"bold",),bg='#0099cc',fg='white',relief='raised')
btn.pack()
btn=Button(tk,text='Press to detect' , command=openthewindow, bd = 7,font=("comic sans",30,"bold",),bg='#0099cc',fg='white',relief='raised')
btn.pack()
tk.mainloop()
