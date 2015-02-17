#__author__ = 'root'
import Tkinter
import main_window


class login:
    def valid(entuser):
        a=entuser.get()
        print a
        if(a=="aa"):
            print a
            main_window.main()

    def main(self):
        print "aaaaaaaaaaaaaaaaaaaaaa"
        w=Tkinter.Tk()
        w.title("PyDetector Login")

        #w.w m_iconbitmap('')
        w.configure(background="#a1bdcd")
        #lblint=Tkinter.Label(w,text="Please login to continue")
        #lblint.pack()

        userlbl=Tkinter.Label(w,text="Username:",width=1230,height=5,background="#a1bdcd")
        entuser=Tkinter.Entry(w,width=30)
        userlbl.pack()
        entuser.pack()
        #a=entuser.get()



        passlbl=Tkinter.Label(w,text="Password:",width=1230,height=5,background="#a1bdcd")
        entpass=Tkinter.Entry(w,width=30)
        passlbl.pack()
        entpass.pack()

        btn=Tkinter.Button(w,text="Login",width=10,command=self.valid(entuser))

        btn.pack()

        w.mainloop()

if __name__=='__main__':
    login.main