import Tkinter
import main_window
import MySQLdb
#import temp
global entuser
global entpass




def valid():
    a=entuser.get()
    b=entpass.get()

    #print a
    #print "sssssssssssssssss"
    if(a=="pydetector" and b=='admin'):
        print a
        print a
        m=main_window.main_window()
        m.main()
    else:
        d=main_window.main_window()
        d.invalid()



def main():

    global db

    w=Tkinter.Tk()
    w.title("PyDetector Login")

    #w.wm_iconbitmap('/root/Desktop/desk/images.jpeg')
    w.configure(background="#a1bdcd")
    #lblint=Tkinter.Label(w,text="Please login to continue")
    #lblint.pack()

    userlbl=Tkinter.Label(w,text="Username:",width=1230,height=5,background="#a1bdcd")
    global entuser
    entuser=Tkinter.Entry(w,width=30)
    userlbl.pack()
    entuser.pack()
    #a=entuser.get()
    print "aaaaaaaaaaaaaaaaaaaaaa"

    global entpass
    passlbl=Tkinter.Label(w,text="Password:",width=1230,height=5,background="#a1bdcd")
    entpass=Tkinter.Entry(w,width=30,show='*')
    passlbl.pack()
    entpass.pack()


    btn=Tkinter.Button(w,text="Login",width=10,command=valid)
    btn.pack()

    wn=5000
    h=3000
    ws = w.winfo_screenwidth()
    hs = w.winfo_screenheight()
    #calculate position x, y
    x = (ws/2) - (wn/2)
    y = (hs/2) - (h/2)
    w.geometry('%dx%d+%d+%d' % (wn, h, x, y))
    w.mainloop()

    db.close()

if __name__=='__main__':
    main()



