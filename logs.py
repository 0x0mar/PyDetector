import Tkinter
import base64
import thread
from Tkconstants import *
from Tkinter import *
from PIL import Image, ImageTk
import parse_packet
import capture
import time
alpha=10
global mlb
flag=0
global tk
c=1
#global v,label

#def s():
#    global v,label
#    v.set(100)
def counter_label_tot_pkt(label):
        #counter = 0
        def count():
            global total_packets
            #global counter
            #counter += 1
            label.config(text=str(capture.total_packets))
            label.after(1000, count)
        count()
def counter_label_pro_pkt(label):
        #counter = 0
        def count():
            global processed_packets
            #global counter
            #counter += 1
            label.config(text=str(parse_packet.processed_packets))
            label.after(1000, count)
        count()

def insert(type,length,remarks):
    global c


    print "in logs.insert"
    global mlb


    mlb.insert(END,('%d'%c,'%s'%(time.strftime("%d/%m/%Y")),'%s'%(time.strftime("%H:%M:%S")),'%s' %parse_packet.s_addr,'%s'%parse_packet.s_mac,'%s' %parse_packet.d_addr,'%s'%parse_packet.d_mac,'%s' %type,'%d'%length,'%s'%remarks))

    mlb.pack(expand=YES,fill=BOTH)
    c=c+1
    #s
    #print "after s()"
    #v.set("sdsdf")

    #mlb.pack(expand=YES,fill=BOTH)
    #frame = Tkinter.Frame(tk, relief=RAISED,width=1, height=11, colormap="new")
    #frame.pack(fill=BOTH,expand=1)
    #label = Tkinter.Label(tk, textvariable=v)


    #button = Tkinter.Button(frame,text="Exit",command=PyDetector.destroy)
    #button.pack(side=BOTTOM)
    #tk.mainloop( )
    #tk.update_idletasks()
    #label.after(1,s)
    tk.update()




def main(self):
    print "in logs.main-----------"


    global flag,v,label

    global tk
    flag=99
    #int_var=StringVar()
    tk = Tk( )
    #v=IntVar()
    tk.wm_title("Logs")

    #int_var.set('sdsdf')
    #image = Image.open("/root/Desktop/kali.png")
    #photo = ImageTk.PhotoImage(image)
    #str_var.set("Total No of Packet ")
    #Label(tk,textvariable=int_var).pack()
    #Label.config(str(capture.total_packets))
    #Label.pack()
    #label = Tkinter.Label(tk, textvariable=v)
    #Button(tk,command=s).pack()
    #label.pack()

    global mlb

    mlb = MultiListbox(tk, (("S.No",1),('Date',1),('Time',1),('Source IP Address', 12),('Source Mac',10), ('Destination IP Address', 10),('Destination Mac',10),('Type', 10),('Length',10),('Remarks',10)))
    #for i in range(1000):
    #   mlb.insert(END,('Alert generated for: %d' % i, 'TCP','10/10/%04d' % (1900+i)))
    #while(True):
    Tkinter.Label(tk,text="Total Packets :").pack()
    label_tot = Tkinter.Label(tk, fg="dark green")
    label_tot.pack()
    counter_label_tot_pkt(label_tot)


    Tkinter.Label(tk,text="Processed Packet :").pack()
    label_pro=Tkinter.Label(tk,fg="dark green")
    label_pro.pack()

    counter_label_pro_pkt(label_pro)
    mlb.pack(expand=YES,fill=BOTH)
    #frame = Tkinter.Frame(tk, relief=RAISED,width=10, height=11, colormap="new")
    #frame.pack(fill=BOTH,expand=1)
    #label = Tkinter.Label(frame, text="ds")
    #label.pack(fill=X, expand=1)
    #button = Tkinter.Button(frame,text="Exit",command=PyDetector.destroy)
    #button.pack(side=BOTTOM)

    #mlb.after(self,1000,self.updateGUI)

    w=5000
    h=3000
    ws = tk.winfo_screenwidth()
    hs = tk.winfo_screenheight()
    #calculate position x, y
    x = (ws/2) - (w/2)
    y = (hs/2) - (h/2)
    tk.geometry('%dx%d+%d+%d' % (w, h, x, y))
    #tk.after(1,s)
    #label.after(1,s)
    tk.mainloop( )


class MultiListbox(Frame):
    def __init__(self, master, lists):
        Frame.__init__(self, master)
        self.lists = []
        for l,w in lists:
            frame = Frame(self); frame.pack(side=LEFT,expand=YES, fill=BOTH)
            #frame.pack(side=TOP,expand=YES, fill=BOTH)
            Label(frame, text=l, borderwidth=7,relief=RAISED).pack(fill=X)
            lb = Listbox(frame, width=w, borderwidth=1,selectborderwidth=1,cursor='spider',selectbackground='cyan',selectforeground='blue',relief=FLAT, height=25, exportselection=FALSE)
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
