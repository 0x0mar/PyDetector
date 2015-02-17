import easygui
import tkMessageBox
import iptc
import parse_packet
global chain
set_ips=set()
def main():
        #global parse_packet.block
        global chain,set_ips
        print "block packet",parse_packet.set_block
        #tup=()
        print "length of block",len(parse_packet.set_block)

        #for j in range(len(parse_packet.set_block)):
        for tup in parse_packet.set_block:
            #tup=parse_packet.set_block.pop()
            if tup[1]=="tcp":
                print "TUPLE VALUE",tup[0]
                rule =iptc.Rule()
                rule.in_interfaces = "eth0"
                rule.src = tup[0]
                rule.protocol = "tcp"
                match = rule.create_match("tcp")
                #match.dport = str(tup[1])
                rule.target=iptc.Target(rule,"DROP")
                print rule


                chain = iptc.Chain(iptc.Table(iptc.Table.FILTER),"INPUT")

                #iptc.Chain.insert_rule(,rule,position=1)
                chain.insert_rule(rule)
                set_ips.add(("eth0","tcp","INPUT chain","DROP","%s"%tup[0]))
                print "set_ips",set_ips
            if tup[1]=="icmp":
                print "TUPLE VALUE",tup[0]
                rule =iptc.Rule()
                rule.in_interfaces = "eth0"
                rule.src = tup[0]
                rule.protocol = "icmp"
                match = rule.create_match("icmp")
                #match.dport = str(tup[1])
                rule.target=iptc.Target(rule,"DROP")
                print "rule",rule


                chain = iptc.Chain(iptc.Table(iptc.Table.FILTER),"INPUT")

                print "chain ",chain
                #iptc.Chain.insert_rule(,rule,position=1)
                chain.insert_rule(rule)
                set_ips.add(("eth0","icmp","INPUT chain", "DROP", "%s"%tup[0]))
                print "set_ips",set_ips
                print "chain rule",chain.rules
                print "deleting ", len(chain.rules)
                print"chain name", chain.name
def flush(proto,s_addr):
    print "proto ",proto
    print "s_addr",s_addr
    if proto=="icmp":
        print "aaaaaaaa"
        rule =iptc.Rule()
        rule.in_interfaces = "eth0"
        rule.src = s_addr
        rule.protocol = "icmp"
        match = rule.create_match("icmp")
        print "match",match
        #match.dport = str(tup[1])
        rule.target=iptc.Target(rule,"DROP")
        #print rule
        #print "rule.src",rule.src

        chain = iptc.Chain(iptc.Table(iptc.Table.FILTER),"INPUT")

        #iptc.Chain.insert_rule(,rule,position=1)
        #chain.insert_rule(rule)
        #if rule.src=="192.168.73.56/255.255.255.255" :
        chain.delete_rule(rule)

        #chain.flush()
        message()
    if proto=="tcp":
        print "aaaaaaaa"
        rule =iptc.Rule()
        rule.in_interfaces = "eth0"
        rule.src = s_addr
        rule.protocol = "tcp"
        match = rule.create_match("tcp")
        print "match",match
        #match.dport = str(tup[1])
        rule.target=iptc.Target(rule,"DROP")
        #print rule
        #print "rule.src",rule.src

        chain = iptc.Chain(iptc.Table(iptc.Table.FILTER),"INPUT")

        #iptc.Chain.insert_rule(,rule,position=1)
        #chain.insert_rule(rule)
        #if rule.src=="192.168.73.56/255.255.255.255" :
        chain.delete_rule(rule)

        #chain.flush()
        message()

def message():

    easygui.msgbox("IP Rule Deleted Successfully!!", title="")



#if __name__ == "__main__":
#   main()