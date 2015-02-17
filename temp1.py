import iptc
print "aaaaaaaa"
rule =iptc.Rule()
rule.in_interfaces = "eth0"
rule.src = "192.168.73.56"
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

#et_ips.add(("Interface eth0","protocol tcp","INPUT chain","DROP","source ip :%s"%tup[0]))
#print "set_ips",set_ips
