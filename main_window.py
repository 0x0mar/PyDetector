
import Tkinter
from Tkinter import *
import logs
import Tkinter
import thread
import parse_packet
import capture
import tkMessageBox
import alerts

class main_window:


    def invalid(self):
        tkMessageBox.showerror("", "Invalid Username or Password")
    def donothing(self):
       filewin = Toplevel()
       button = Button(filewin, text="Do nothing button")
       button.pack()

    def start_capture_thread(self):
    #   cap = thread(target=capture.main, name="capture_thread")
        thread.start_new_thread(capture.main,(self,))
        thread.start_new_thread(parse_packet.main,(self,))

    def start_logs_thread(self):
    #   log = thread(target=logs.main, name="logs_thread")
        thread.start_new_thread(logs.main,(self,))

    def start_alerts_thread(self):
        thread.start_new_thread(alerts.main(self,))



    def stop(self):
        pass

    def main(self):

        #cap=capture()

        #cap.main()
        #cap.main()

        root=Tk()

        #alt = Thread(target=capture.main, args=(i,))



        root.wm_title("PyDetector")
        menubar = Menu(root)
        adminmenu = Menu(menubar, tearoff=0)
        adminmenu.add_command(label="Configuration", command=self.donothing)
        #adminmenu.add_command(label="", command=donothing)
        #adminmenu.add_command(label="", command=donothing)
        #adminmenu.add_command(label="Save as...", command=donothing)
        #adminmenu.add_command(label="Close", command=donothing)

        adminmenu.add_separator()

        adminmenu.add_command(label="Exit", command=root.quit)
        menubar.add_cascade(label="Administration", menu=adminmenu)
        viewmenu = Menu(menubar, tearoff=0)
        #viewmenu.add_command(label="Undo", command=donothing)

        viewmenu.add_separator()

        viewmenu.add_command(label="Logs", command=self.start_logs_thread)
        viewmenu.add_command(label="Alerts", command=self.start_alerts_thread)
        #viewmenu.add_command(label="", command=donothing)
        #viewmenu.add_command(label="P", command=donothing)
        #viewmenu.add_command(label="D", command=donothing)
        #viewmenu.add_command(label="S", command=donothing)
        viewmenu.add_command(label="Exit", command=root.quit)
        menubar.add_cascade(label="View", menu=viewmenu)
        #menubar.add_cascade(label="Alerts", menu=viewmenu)
        helpmenu = Menu(menubar, tearoff=0)
        helpmenu.add_command(label="Help Index", command=self.donothing)
        helpmenu.add_command(label="About...", command=self.donothing)
        menubar.add_cascade(label="Help", menu=helpmenu)



        btn_start=Tkinter.Button(root,text="Capture",width=10,fg="black",command=self.start_capture_thread)
        btn_start.pack()


        btn_stop=Tkinter.Button(root,text="STOP",width=10,fg="red",command=self.stop)
        btn_stop.pack(pady=20,padx=20)
    #   btn_stop=Tkinter.Button(root,text="Login",width=10,command=stop)

        #root.config(menu=menubar)


        root.config(menu=menubar)
        w=5000
        h=3000
        ws = root.winfo_screenwidth()
        hs = root.winfo_screenheight()
        #calculate position x, y
        x = (ws/2) - (w/2)
        y = (hs/2) - (h/2)
        root.geometry('%dx%d+%d+%d' % (w, h, x, y))
        root.mainloop()






#if __name__=='__main__':
#    main_window.main()