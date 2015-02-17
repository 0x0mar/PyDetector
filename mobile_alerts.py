import urllib2
import unirest
import json

#phone = raw_input("Enter receiver's number: ")

#msg = raw_input("Enter the message to send: ")

#headers = { "X-Mashape-Authorization": "C3ZThvBHiXmsh1IZ5KMrKadUtKtDp1RRyxNjsn0PEgLLv8RDWW" }

#url = "https://160by2.p.mashape.com/index.php?msg="+msg+"&phone="+phone+"&pwd=your < password>&uid=<your user id>"
#url2= "https://messagebird-sms-gateway.p.mashape.com/hlr"
#url3= "https://messagebird-sms-gateway.p.mashape.com/sms?password=iPhone&username=siddhuthekiller"
#req = urllib2.Request(url3, '', headers)

#response = json.loads(urllib2.urlopen(req).read())

# These code snippets use an open-source library. http://unirest.io/python
response = unirest.get("https://dhruvj-160by21.p.mashape.com/?gateway=Type+160by2&mymsg=undefined&no=8093775331&num=8093775331&pass=iPhone&submit=Type+Send&to=8093775331",
  headers={"X-Mashape-Key": "C3ZThvBHiXmsh1IZ5KMrKadUtKtDp1RRyxNjsn0PEgLLv8RDWW"}
)


print response.code
'''




if response['response'] != "done\n":

    print "Error"

else:

    print "Message sent successfully"
'''