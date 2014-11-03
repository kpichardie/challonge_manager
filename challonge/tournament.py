#!/usr/bin/env python
# -*- coding: utf-8 -*- 

class tournament():

    def _index(self, **kwargs):
        
        #for k,v in kwargs.items() : 
        #    options[] = print "%s=%s" % (k, v)

        #url_options = '&'.join(options);
        url_options = '&'.join(kwargs);

        #url = url_construct(url_options);
        print (url_options);
        url = self._url_construct(url_options)
        return url;
        #return url_options;

    def __init__(self):
        self._api_key = self

    def _create(self, **kwargs):
        return self;

    def _url_construct(self, url_options):
        url = "https://api.challonge.com/v1/tournaments.xml"
        full_url = "%s?%s" % (url, url_options) 
        return full_url;

