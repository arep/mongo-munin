
import urllib2
import sys
import os  
import pymongo

def getServerStatus():
    host = "127.0.0.1"
    port = 27017
    c = pymongo.Connection(host, port)
    return c.admin.command('serverStatus', workingSet=True)
