import MySQLdb
import login
import parse_packet





'''
# Select qSQL with id=4.
#cursor.execute("show tables")

# Fetch a single row using fetchone() method.
results = cursor.fetchone()

#qSQL = results[0]

#cursor.execute(qSQL)

# Fetch all the rows in a list of lists.
#qSQLresults = cursor.fetchall()
#for row in qSQLresults:
 #   id = row[0]
  #  city = row[1]
'''
def pyd_db_alert(s_no , date , time , message , attack , src_ip , src_mac , severity):
#SQL query to INSERT a record into the table FACTRESTTBL.



    print "asdf"
    #cursor.execute('insert into pyd_alerts values("a","b","c","d","e","f","g","h")')

    parse_packet.cursor.execute('''INSERT into pyd_alerts ( s_no , date , time , message , attack , src_ip , src_mac , severity)
                      values (%s, %s ,%s ,%s ,%s ,%s ,%s ,%s)''',
                      (s_no , date , time , message , attack , src_ip , src_mac , severity))



    parse_packet.db.commit()

def pyd_db_logs(s_no , date , time , src_ip , src_mac , dst_ip , dst_mac , type , length , remarks):
    pass
    print "ssssssssssssssssssssss%s"%s_no

    parse_packet.cursor.execute('''INSERT into pyd_logs ( s_no , date , time , src_ip , src_mac , dst_ip , dst_mac , type , length , remarks)
                      values (%s, %s ,%s ,%s ,%s ,%s ,%s ,%s,%s,%s)''',
                      (s_no , date , time , src_ip , src_mac , dst_ip , dst_mac , type , length , remarks))

    parse_packet.db.commit()

def pyd_db_iptables(rule_no , interface , src_ip , src_port , target , chain):


    parse_packet.cursor.execute('''INSERT into pyd_alerts ( rule_no , interface , src_ip . src_port , target , chain)
                      values (%s, %s ,%s ,%s ,%s ,%s ,%s ,%s)''',
                      (rule_no , interface , src_ip . src_port , target , chain))

    parse_packet.db.commit()


    # Commit your changes in the database


# disconnect from server


def main():

    pyd_db_alert("a","b","c","d","e","f","g","h")

if "__name__"=="__main__":
    main()
