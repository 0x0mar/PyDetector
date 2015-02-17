import pcapy
from timeit import default_timer

#from threading import Timer
#from logs import *



start=0
duration_sync_flood=0


total_packets=0
global packets
packets=[]

no_syn_packets=0
no_syn_ack_packets=0
no_ack_packets=0

def main(self):

    #list all devices
    global start, total_packets
    start = default_timer()

    print "in capture main"

    devices = pcapy.findalldevs()
    print devices

    #ask user to enter device name to sniff
    print "Available devices are :"
    for d in devices :
        print d

#    dev = raw_input("Enter device name to sniff : ")

#    print "Sniffing device " + dev

    dev="eth0"
    '''
    open device
    # Arguments here are:
    #   device
    #   snaplen (maximum number of bytes to capture _per_packet_)
    #   promiscious mode (1 for true)
    #   timeout (in milliseconds)
    '''
    cap = pcapy.open_live(dev , 65536 , 1 , 0)

    #start sniffing packets




    while(True) :

        print "total packet = %d" %total_packets

        (header, p) = cap.next()
        packets.append(p)
        total_packets=total_packets+1
        if(total_packets>=0):
            #print packets[total_packets-1]
            pass
        #print ('%s: captured %d bytes, truncated to %d bytes' %(datetime.datetime.now(), header.getlen(), header.getcaplen()))
        #parse_packet(packet)


#Convert a string of 6 characters of ethernet address into a dash separated hex string

#function to parse a packet








if __name__ == "__main__":
  main()