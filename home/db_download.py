from django.shortcuts import render
from django.template.loader import get_template
from django.template import Context
from django.http import HttpResponse
from django import template
import MySQLdb

def log_data(request):
    db = MySQLdb.connect(user='root', db='sid', passwd='', host='localhost')
    cursor = db.cursor()
    cursor.execute('SELECT * FROM pyd_logs')
    logs=cursor.fetchall()





    t = template.Template(' {{ logs }}')
    c = template.Context({'logs': logs})

#    print c.render()
    db.close()
    #return render(request, 'book_list.html', {'names': names})
    return render(request,logs)
