import iptc
import parse_packet
import MySQLdb

def main():
        #global parse_packet.block
        db = MySQLdb.connect("localhost","root","","sid")
        cursor=db.cursor()
        cursor.execute("select * from old_value where id='1'")
        old=cursor.fetchall()
        print "old",old
        print "block packet",parse_packet.set_block
        tup=()
        print "length of block",len(parse_packet.set_block)
        new=len(parse_packet.set_block)
        old1=int(old[0][1])
        set_block1=list(parse_packet.set_block)[old1:]
        print "set_block1",set_block1
        for j in range(len(set_block1)):
            tup=set_block1[j]
            print "TUPLE VALUE",tup[0]
            rule =iptc.Rule()
            rule.in_interfaces = "eth0"
            rule.src = tup[0]
            rule.protocol = "tcp"
            match = rule.create_match("tcp")
            match.dport = str(tup[1])
            rule.target=iptc.Target(rule,"DROP")
            print rule


            chain = iptc.Chain(iptc.Table(iptc.Table.FILTER),"INPUT")

            #iptc.Chain.insert_rule(,rule,position=1)
            chain.insert_rule(rule)
            #parse_packet.set_block.clear()
        new=str(new)
        cursor.execute("update old_value set size=%s where id='1'"%new)

#if __name__ == "__main__":
#   main()