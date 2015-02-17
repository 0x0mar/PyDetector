import Tkinter
import base64
import thread
from Tkconstants import *
from Tkinter import *
from PIL import Image, ImageTk
import capture
import parse_packet
import time
import ips
alpha=10
global mla
flag=0
global ta
global frame
s_no=1

def iptables():

    ipt=Tk()
    ipt.wm_title("IPTABLES")
    #frame = Tkinter.Frame(ipt, relief=RAISED,width=10, height=11,colormap="new")
    ##frame.pack(fill=BOTH,expand=1)
    for i in ips.set_ips:
        rd=Tkinter.Radiobutton(ipt, text="%s : %s : %s : %s : %s"%(i[0], i[1], i[2], i[3], i[4]), width=150, indicatoron=0, activeforeground="blue", padx=20,  pady=5, command=lambda: ips.flush(i[1], i[4]))
        rd.pack()

    #rd=Tkinter.Radiobutton(frame,text="ss",width=20,command=ips.flush)
    #rd.pack()
    #rd=Tkinter.Radiobutton(frame,text="ss",width=20,command=ips.flush)
    #rd.pack()
    #RADIOBUTTON(ipt,text="ips").pack()

    w=5000
    h=3000
    ws = ipt.winfo_screenwidth()
    hs = ipt.winfo_screenheight()
    #calculate position x, y
    x = (ws/2) - (w/2)
    y = (hs/2) - (h/2)
    ipt.geometry('%dx%d+%d+%d' % (w, h, x, y))
    ipt.mainloop()


def insert(s_addr,s_mac,message,attack,severity):
    print "in alert.insert"
    global mla,s_no

    #print parse_packet.s_addr
    mla.insert(END,('%d' % s_no , '%s'%(time.strftime("%d/%m/%Y")),'%s'% (time.strftime("%H:%M:%S")),'%s' %message,'%s'% attack,'%s' %s_addr,'%s'%s_mac,'%s' %severity))
    mla.pack(expand=YES,fill=BOTH)
    s_no=s_no+1
    print parse_packet.s_addr
    #mlb.pack(expand=YES,fill=BOTH)
    #frame = Tkinter.Frame(tk, relief=RAISED,width=1786, height=11, colormap="new")
    #frame.pack(fill=BOTH,expand=1)
    #label = Tkinter.Label(frame, text="")
    #label.pack(fill=X, expand=1)
    #button = Tkinter.Button(frame,text="Exit",command=PyDetector.destroy)
    #button.pack(side=BOTTOM)
    #tk.mainloop( )
    ta.update()

'''
def start_fix_thread(self):
    thread.start_new_thread(ips.main(self,))

def start_flush_thread(self):
    thread.start_new_thread(iptables(self,))
'''
def main(self):
    print "in alert.main-----------"


    global flag
    global ta
    global mla
    flag=99

    ta = Tk( )
    ta.wm_title("Alerts")
    #image = Image.open("/root/Desktop/kali.png")
    #photo = ImageTk.PhotoImage(image)
    #Label(ta,text='',photo=image).pack( )
    #ips_o=ips.ips()

    Button(ta,text="FIX",width=20,fg='black',bg='green',command=ips.main).pack(side=TOP)
    Button(ta,text="FLUSH",width=20,fg='black',bg='green',command=iptables).pack(side=TOP)


    mla = MultiListbox(ta, (('S.No.',1),('Date',3),('Time',3),('Message',20),('Attack', 10),('Source address',10),('Source Mac',10),('Severity', 3)))

    #for i in range(1000):
    #   mlb.insert(END,('Alert generated for: %d' % i, 'TCP','10/10/%04d' % (1900+i)))
    #while(True):


    mla.pack(expand=YES,fill=BOTH)
    #frame = Tkinter.Frame(tk, relief=RAISED,width=1786, height=11, colormap="new")
    #frame.pack(fill=BOTH,expand=1)
    #label = Tkinter.Label(frame, text="")
    #label.pack(fill=X, expand=1)


    #mlb.after(self,1000,self.updateGUI)
    w=5000
    h=3000
    ws = ta.winfo_screenwidth()
    hs = ta.winfo_screenheight()
    #calculate position x, y
    x = (ws/2) - (w/2)
    y = (hs/2) - (h/2)
    ta.geometry('%dx%d+%d+%d' % (w, h, x, y))

    ta.mainloop( )


class MultiListbox(Frame):
    def __init__(self, master, lists):
        Frame.__init__(self, master)
        self.lists = []
        for l,w in lists:
            frame = Frame(self); frame.pack(side=LEFT,expand=YES, fill=BOTH)
            #frame.pack(side=,expand=YES, fill=BOTH)
            Label(frame, text=l, borderwidth=7,relief=RAISED).pack(fill=X)
            lb = Listbox(frame, width=w, borderwidth=1,selectborderwidth=1,selectbackground='cyan',selectforeground='red',cursor='pirate',relief=RAISED, exportselection=FALSE)
            lb.pack(expand=YES, fill=BOTH)
            self.lists.append(lb)
            lb.bind('<B1-Motion>', lambda e, s=self:
            s._select(e.y))
            lb.bind('<Button-1>', lambda e, s=self:
            s._select(e.y))
            lb.bind('<Leave>', lambda e: 'break')
            lb.bind('<B2-Motion>', lambda e, s=self:
            s._b2motion(e.x, e.y))
            lb.bind('<Button-2>', lambda e, s=self:
            s._button2(e.x, e.y))
        frame = Frame(self); frame.pack(side=LEFT, fill=Y)
        Label(frame, borderwidth=1,relief=RAISED).pack(fill=X)
        sb = Scrollbar(frame, orient=VERTICAL,command=self._scroll)
        sb.pack(expand=YES, fill=Y)
        self.lists[0]['yscrollcommand']=sb.set
    def _select(self, y):
        row = self.lists[0].nearest(y)
        self.selection_clear(0, END)
        self.selection_set(row)
        return 'break'
    def _button2(self, x, y):
        for l in self.lists: l.scan_mark(x, y)
        return 'break'
    def _b2motion(self, x, y):
        for l in self.lists: l.scan_dragto(x, y)
        return 'break'
    def _scroll(self, *args):
        for l in self.lists:
            apply(l.yview, args)
    def curselection(self):
        return self.lists[0].curselection()
    def delete(self, first, last=None):
        for l in self.lists:
            l.delete(first, last)
        def get(self, first, last=None):
            result = []
            for l in self.lists:
                result.append(l.get(first,last))
            if last: return apply(map, [None] + result)
            return result
    def index(self, index):
        self.lists[0].index(index)
    def insert(self, index, *elements):
        for e in elements:
            i = 0
            for l in self.lists:
                l.insert(index, e[i])
                i = i + 1
    def size(self):
        return self.lists[0].size()
    def see(self, index):
        for l in self.lists:
            l.see(index)
    def selection_anchor(self, index):
        for l in self.lists:
            l.selection_anchor(index)
    def selection_clear(self, first, last=None):
        for l in self.lists:
            l.selection_clear(first, last)
    def selection_includes(self, index):
        return self.lists[0].selection_includes(index)
    def selection_set(self, first, last=None):
        for l in self.lists:
            l.selection_set(first, last)
if __name__=='__main__':
    main()
