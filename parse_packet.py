
import socket
from struct import *
import datetime
import pcapy
import sys
import time
from timeit import default_timer
import logs
from threading import Timer
import capture
import alerts
import ips
import db_load
import MySQLdb

global protocol
global s_addr
global d_addr
global s_mac
global d_mac
global set_block

global db
global cursor

processed_packets=0


set_block= set()
set_icmp_s_addr=set()
set_port_nos=set()
set_ping_of_death_s_addr=set()
set_smurf_s_addr=set()
set_ddos=set()

s_no_alerts=0
s_no_logs=0


start_sync_flood_timer = default_timer()
start_ddos_timer=default_timer()

duration_sync_flood=0
duration_ddos=0

nmap_s_addr=""
nmap_s_mac=""


def main(self):
    print "parse main"
    global processed_packets

    global db,cursor

    # Open database connection
    db = MySQLdb.connect("localhost","root","","sid" )

# prepare a cursor object using cursor() method
    cursor = db.cursor()

    print "conn estd"




    while(True):
         #   pass
        if(capture.total_packets==processed_packets):
            print "in sleep"
            time.sleep(2)
        print "parse while"
        if(capture.total_packets>processed_packets):
            print "capture.total packet = %d" %capture.total_packets
            print "processd packet = %d" %processed_packets
            #print "dddd",capture.packets[0]
            #print "length of packt",len(capture.packets)
            parse_packet(capture.packets[processed_packets])

            #capture.packets=capture.packets[processed_packets:]
            processed_packets=processed_packets+1
            print "processd packets = %d"%processed_packets


def parse_packet(packet):

    #print packet
    #parse ethernet header



    print "set_port_nos=%s" %set_port_nos

    global iph_length,s_mac,d_mac,set_block,nmap_s_addr,set_smurf_s_addr
    global temp, start_sync_flood_timer,start_ddos_timer,s_no_alerts,nmap_s_mac,s_no_logs
    eth_length = 14

    eth_header = packet[:eth_length]
    eth = unpack('!6s6sH' , eth_header)
    eth_protocol = socket.ntohs(eth[2])

    s_mac=eth_addr(packet[6:12])
    d_mac=eth_addr(packet[0:6])
    print 'Destination MAC : ' + d_mac + ' Source MAC : ' + s_mac + ' Protocol : ' + str(eth_protocol)

    """
    duration_sync_flood = default_timer() - start_sync_flood_timer

    print "default_timer()=%s"%default_timer()

    print "start_sync_flood_timer=%s"%start_sync_flood_timer


    print "duration_sync_flood=%s" %duration_sync_flood

    """


    #Parse IP packets, IP Protocol number = 8
    if eth_protocol == 8 :
        print "sadfd"
        #Parse IP header
        #take first 20 characters for the ip header
        ip_header = packet[eth_length:20+eth_length]

        #now unpack them :)
        iph = unpack('!BBHHHBBH4s4s' , ip_header)

        version_ihl = iph[0]
        version = version_ihl >> 4
        ihl = version_ihl & 0xF

        iph_length = ihl * 4
        print "length====",iph_length

        ttl = iph[5]

        global protocol
        global s_addr
        global d_addr, no_syn_ack_packets, no_ack_packets
        global flag, no_syn_packets
        protocol = iph[6]
        s_addr = socket.inet_ntoa(iph[8]);
        d_addr = socket.inet_ntoa(iph[9]);





        print 'Version : ' + str(version) + ' IP Header Length : ' + str(ihl) + ' TTL : ' + str(ttl) + ' Protocol : ' + str(protocol) + ' Source Address : ' + str(s_addr) + ' Destination Address : ' + str(d_addr)

        duration_sync_flood = default_timer() - start_sync_flood_timer

        print "default_timer()=%s"%default_timer()

        print "start_sync_flood_timer=%s"%start_sync_flood_timer


        print "duration_sync_flood=%s" %duration_sync_flood


        print "set_port_nos=%s" %set_port_nos

        print "len(set_port_nos)%d"%len(set_port_nos)

        if(duration_sync_flood>10):
            start_sync_flood_timer=default_timer()



            print "capture.no_ack_packets=%s " %capture.no_ack_packets
            print "capture.no_syn_packets=%s" %capture.no_syn_packets
                #print "len(set_port_nos)%d"%len(set_port_nos)
                #print "len(set_port_nos)=%s"%len(set_port_nos)
            if(len(set_port_nos)>100):
                alerts.insert(nmap_s_addr,nmap_s_mac,"Port Scanning", "NMAP","Medium")
                s_no_alerts=s_no_alerts+1

                db_load.pyd_db_alert(s_no_alerts,'%s'%(time.strftime("%d/%m/%Y")),'%s'%(time.strftime("%H:%M:%S")),"Port Scanning","NMAP",nmap_s_addr,nmap_s_mac,"Medium")
                print "nmap sourceaddre=%s"%nmap_s_addr

                set_block.add((nmap_s_addr,"tcp"))
                set_port_nos.clear()
                print "nmap block ips",set_block
            if(capture.no_ack_packets<(capture.no_syn_packets*0.75) and len(set_port_nos)==1 and capture.no_syn_packets>300 ):
                alerts.insert(s_addr,s_mac,"Flooding of sync packet", "TCP Sync Flood","Medium")
                s_no_alerts=s_no_alerts+1
                db_load.pyd_db_alert(s_no_alerts,'%s'%(time.strftime("%d/%m/%Y")),'%s'%(time.strftime("%H:%M:%S")),"Flooding of sync packet","TCP Sync Flood",s_addr,s_mac,"Medium")

                set_port_nos.clear()
                set_block.add((s_addr,"tcp"))
            #   set_block.append((s_addr,source_port))




        #TCP protocol
        if protocol == 6 :

            print "=================================TCP===================="

            t = iph_length + eth_length
            tcp_header = packet[t:t+20]

            #now unpack them :)
            tcph = unpack('!HHLLBBHHH' , tcp_header)

            source_port = tcph[0]
            dest_port = tcph[1]
            sequence = tcph[2]
            acknowledgement = tcph[3]
            doff_reserved = tcph[4]
            print "=========================offset===================="
            print doff_reserved.__sizeof__
            tcph_length = doff_reserved >> 4

            print "=========================tcph[5]==============="

            #print bin(tcph[5])
            #print tcph[5]
            print "=====================tcp_syn value=============="




            """
            if(duration>=10):
                start = default_timer()
                if(no_syn_packets>100):
                    print "syn flood"

            tcp_syn=tcph[5] & 2
            if(tcp_syn==2):

                print "sync packet detected "
                no_syn_packets=no_syn_packets+1

            print "no of syn pack=%d"%no_syn_packets
            duration = default_timer() - start

            print "duration=%d"%duration


            """
            tcp_syn=tcph[5] & 2
            tcp_syn_ack=tcph[5] & 18
            tcp_ack=tcph[5] & 16

            if(tcp_syn==2):
                capture.no_syn_packets=capture.no_syn_packets+1
                print "sync packet detected "
                print "dest_port=%s" %dest_port
                set_port_nos.add(dest_port)
                nmap_s_addr=s_addr
                nmap_s_mac=s_mac
                print "qqqqqqqqqqqqqqqqqs_addr=%s"%s_addr


            if(tcp_syn==18):
                print "sync n ack packet detected "
                capture.no_syn_ack_packets=capture.no_syn_ack_packets+1

            if(tcp_syn==16):
                print "ack packet detected "
                capture.no_ack_packets=capture.no_ack_packets+1

            print "no of syn pack=%d"%capture.no_syn_packets










                    #block=(s_addr,source_port)






            if(dest_port==21):
                if(logs.flag==99):
                    logs.insert("FTP",len(packet),"")
                    s_no_logs=s_no_logs+1
                    db_load.pyd_db_logs(str(s_no_logs),'%s'%(time.strftime("%d/%m/%Y")),'%s'%(time.strftime("%H:%M:%S")),s_addr,s_mac,d_addr,d_mac,"FTP",str(len(packet)),"")
                    #set_block.add((s_addr,source_port))
                    #print "display block",set_block



            if(dest_port==25 ):
                if(logs.flag==99):
                    logs.insert("SMTP",len(packet),"")
                    s_no_logs=s_no_logs+1
                    db_load.pyd_db_logs(str(s_no_logs),'%s'%(time.strftime("%d/%m/%Y")),'%s'%(time.strftime("%H:%M:%S")),s_addr,s_mac,d_addr,d_mac,"SMTP",str(len(packet)),"")


            if(dest_port==53 ):
                if(logs.flag==99):
                    logs.insert("DNS",len(packet),"")
                    s_no_logs=s_no_logs+1
                    db_load.pyd_db_logs(str(s_no_logs),'%s'%(time.strftime("%d/%m/%Y")),'%s'%(time.strftime("%H:%M:%S")),s_addr,s_mac,d_addr,d_mac,"DNS",str(len(packet)),"")



            if(dest_port==443 ):
                if(logs.flag==99):
                    logs.insert("HTTPS",len(packet),"")
                    s_no_logs=s_no_logs+1
                    db_load.pyd_db_logs(str(s_no_logs),'%s'%(time.strftime("%d/%m/%Y")),'%s'%(time.strftime("%H:%M:%S")),s_addr,s_mac,d_addr,d_mac,"HTTPS",str(len(packet)),"")


            if(dest_port==22 ):
                if(logs.flag==99):
                    logs.insert("SSH",len(packet),"")
                    s_no_logs=s_no_logs+1
                    db_load.pyd_db_logs(str(s_no_logs),'%s'%(time.strftime("%d/%m/%Y")),'%s'%(time.strftime("%H:%M:%S")),s_addr,s_mac,d_addr,d_mac,"SSH",str(len(packet)),"")


            if(dest_port==23 ):
                if(logs.flag==99):
                    logs.insert("TELNET",len(packet),"")
                    s_no_logs=s_no_logs+1
                    db_load.pyd_db_logs(str(s_no_logs),'%s'%(time.strftime("%d/%m/%Y")),'%s'%(time.strftime("%H:%M:%S")),s_addr,s_mac,d_addr,d_mac,"TELNET",str(len(packet)),"")






            print "set block",set_block
            print 'Source Port : ' + str(source_port) + ' Dest Port : ' + str(dest_port) + ' Sequence Number : ' + str(sequence) + ' Acknowledgement : ' + str(acknowledgement) + ' TCP header length : ' + str(tcph_length)


            h_size = eth_length + iph_length + tcph_length * 4


            data_size = len(packet) - h_size

            #get data from the packet
            data = packet[h_size:]

            print 'Data : ' + data

        #ICMP Packets
        elif protocol == 1 :

            print "==========================ICMP==========================="

            #set_icmp_s_addr.add(s_addr)

            #print "set_icmp_s_addr=%s"%set_icmp_s_addr





            u = iph_length + eth_length
            icmph_length = 4
            icmp_header = packet[u:u+4]

            #now unpack them :)
            icmph = unpack('!BBH' , icmp_header)

            icmp_type = icmph[0]
            code = icmph[1]
            checksum = icmph[2]

            print 'Type : ' + str(icmp_type) + ' Code : ' + str(code) + ' Checksum : ' + str(checksum)


            h_size = eth_length + iph_length + icmph_length

            print "SIZE OF PACKET",len(packet)

            data_size = len(packet) - h_size

            #get data from the packet
            data = packet[h_size:]
            print "icmp data= %s"%data
            #print "data[52]",data[52]
            if icmp_type==8:
                set_icmp_s_addr.add((s_addr,s_mac))
            if logs.flag==99:
                if icmp_type==8:
                    print "icmp req"
                    if(data.find('abcdefghijklmnopqrtuvw') and len(packet)==74):
                        logs.insert("ICMP Request",len(packet),"Windows Ping")
                        s_no_logs=s_no_logs+1
                        #db_load.pyd_db_logs(str(s_no_logs),'%s'%(time.strftime("%d/%m/%Y")),'%s'%(time.strftime("%H:%M:%S")),s_addr,s_mac,d_addr,d_mac,"ICMP Request",str(len(packet)),"Windows Ping")
                        db_load.pyd_db_logs("","","","","","","","","","")
                    elif (data.find('01234567') and len(packet)==98):
                        logs.insert("ICMP Request",len(packet),"Linux Ping")
                        s_no_logs=s_no_logs+1
                        db_load.pyd_db_logs(str(s_no_logs),'%s'%(time.strftime("%d/%m/%Y")),'%s'%(time.strftime("%H:%M:%S")),s_addr,s_mac,d_addr,d_mac,"ICMP Request",str(len(packet)),"Linux Ping")


                if(icmp_type==0 ):
                    print "icmp rep"
                    if(data.find('abcdefghijklmnopqrtuvw') and len(packet)==74):
                        logs.insert("ICMP Reply",len(packet),"Windows Ping")
                        s_no_logs=s_no_logs+1
                        db_load.pyd_db_logs(str(s_no_logs),'%s'%(time.strftime("%d/%m/%Y")),'%s'%(time.strftime("%H:%M:%S")),s_addr,s_mac,d_addr,d_mac,"ICMP Reply",str(len(packet)),"Windows Ping")
                    elif (data.find('01234567') and len(packet)==98):
                        logs.insert("ICMP Reply",len(packet),"Linux Ping")
                        s_no_logs=s_no_logs+1
                        db_load.pyd_db_logs(str(s_no_logs),'%s'%(time.strftime("%d/%m/%Y")),'%s'%(time.strftime("%H:%M:%S")),s_addr,s_mac,d_addr,d_mac,"ICMP Reply",str(len(packet)),"Linux Ping")

            if(alerts.flag==99):
                if(d_addr.find('255')!=-1):
                    print d_addr.find('255')
                    if(s_addr not in set_smurf_s_addr):
                        alerts.insert(s_addr,s_mac,"Smurf attack","Smurf attack","Medium")
                        s_no_alerts=s_no_alerts+1
                        db_load.pyd_db_alert(s_no_alerts,'%s'%(time.strftime("%d/%m/%Y")),'%s'%(time.strftime("%H:%M:%S")),"","Smurf attack",s_addr,s_mac,"Medium")
                        set_smurf_s_addr.add(s_addr)
                        for s_smurf in set_smurf_s_addr:
                            set_block.add((s_smurf,"icmp"))


                if(len(packet)!=74 and len(packet)!=98 and icmp_type==8):


                    if(s_addr not in set_ping_of_death_s_addr):
                        alerts.insert(s_addr,s_mac,"ICMP Tampered Packet","Ping of Death","Medium")
                        s_no_alerts=s_no_alerts+1
                        db_load.pyd_db_alert(s_no_alerts,'%s'%(time.strftime("%d/%m/%Y")),'%s'%(time.strftime("%H:%M:%S")),"ICMP Tampered Packet","Ping of Death",s_addr,s_mac,"Medium")

                    set_ping_of_death_s_addr.add(s_addr)

                    for s_ping in set_ping_of_death_s_addr:
                        set_block.add((s_ping,"icmp"))

                duration_ddos = default_timer() - start_ddos_timer

                print "duration_ddos=%s"%duration_ddos

                print "default_timer=%s"%default_timer()

                if(duration_ddos>5):
                    start_ddos_timer=default_timer()
                    print "set_icmp_s_addr=%s"%set_icmp_s_addr
                    if(len(set_icmp_s_addr)>=4 ):
                        for s in set_icmp_s_addr:
                            alerts.insert(s[0],s[1],"Possible DDos","DDos","Severe")
                            s_no_alerts=s_no_alerts+1
                            db_load.pyd_db_alert(s_no_alerts,'%s'%(time.strftime("%d/%m/%Y")),'%s'%(time.strftime("%H:%M:%S")),"Ping from different IPs","DDos",s_addr,s_mac,"Severe")


                            set_block.add((s,"icmp"))
                        #set_icmp_s_addr.clear()



            print 'Data : ' + data

        #UDP packets
        elif protocol == 17 :
            u = iph_length + eth_length
            udph_length = 8
            udp_header = packet[u:u+8]

            #now unpack them :)
            udph = unpack('!HHHH' , udp_header)

            source_port = udph[0]
            dest_port = udph[1]
            length = udph[2]
            checksum = udph[3]

            print 'Source Port : ' + str(source_port) + ' Dest Port : ' + str(dest_port) + ' Length : ' + str(length) + ' Checksum : ' + str(checksum)

            h_size = eth_length + iph_length + udph_length
            data_size = len(packet) - h_size

            #get data from the packet
            data = packet[h_size:]

            print 'Data : ' + data

    #some other IP packet like IGMP

        else:
            print 'Protocol other than TCP/UDP/ICMP'

            print

    else:
         print "========================================================other than ip"



def eth_addr (a) :
    b = "%.2x:%.2x:%.2x:%.2x:%.2x:%.2x" % (ord(a[0]) , ord(a[1]) , ord(a[2]), ord(a[3]), ord(a[4]) , ord(a[5]))
    return b
