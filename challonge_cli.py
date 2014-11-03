#!/usr/bin/env python
# -*- coding: utf-8 -*- 

import pycurl
from StringIO import StringIO
import argparse
from challonge.tournament import *


#parser = argparse.ArgumentParser(description='Process some integers.')
#parser.add_argument('integers', metavar='N', type=int, nargs='+',
#                   help='an integer for the accumulator')
#parser.add_argument('--sum', dest='accumulate', action='store_const',
#                   const=sum, default=max,
#                   help='sum the integers (default: find the max)')
#
#args = parser.parse_args()
#print(args.accumulate(args.integers))



##curl part
#buffer = StringIO()
#c = pycurl.Curl()
#c.setopt(c.URL, 'https://$username:$password@api.challonge.com/v1/')
#c.setopt(c.WRITEDATA, buffer)
#c.perform()
#c.close()
#
#body = buffer.getvalue()
## Body is a string in some encoding.
## In Python 2, we can print it without knowing what the encoding is.
#print(body)

def main():
        t=tournament();
        url=t._index(test=2,test2=3);
        #option = t._index(test=2,test2=3);
        #url = t._url_construct(option);
        print (url);

def usage():

    print ' -------------------------------------------------------------------------'
    print ' '
    print ' '
    print ' '
    print ' '
    print ' '
    print ' Typical usage:'
    print ' '
    print ' '
    print ' '
    print ' '
    print ' -------------------------------------------------------------------------'
    sys.exit(' ')

#-------------------------------
if __name__ == "__main__":
    main()


#    def _create(*arg):
#        return "create";
#
#    def _show(*arg):
#        return "show";
#
#    def _update(*arg):
#        return "update";
#
#    def _destroy(*arg):
#        return "destroy";
#
#    def _process(*arg):
#        return "process";
#
#    def _abort(*arg):
#        return "abort";
#
#    def _start(*arg):
#        print arg;
#        return "start";
#
#    def _finalize(*arg):
#        return "finalize";
#
#    def _reset(*arg):
#        print "%s" list(arg);
#        return "reset";
    

#    Index
#        * api_key 
#        state
#        type
#        created_after
#        created_before
#        subdomain
#    Create
#        * api_key
#        tournament[name]
#
#    Show
#    Update
#    Destroy
#    Process
#    Abort
#    Start
#    Finalize
#    Reset
#Participants
#    Index
#    Create
#    Bulk
#    Show
#    Update
#    Check
#    Destroy
#    Randomize
#Matches
#    Index
#    Show
#    Update
#    
