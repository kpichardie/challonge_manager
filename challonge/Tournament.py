#!/usr/bin/env python
# -*- coding: utf-8 -*- 

#from challonge.Common import * 

class Tournament():

    def index(self, **kwargs):
        
        url_options = '&'.join(kwargs);

        model = Common();
        modele = "tournament"
        url = model._url_construct(modele, url_options);
        return url;

    def __init__(self):
        self._api_key = self

    def create(self, **kwargs):
        return self;

class Common():

    def __init__(self):
        self = self

    def _url_construct(self, modele, url_options):
        url = "https://api.challonge.com/v1/"
        full_url = "%s%s.xml?%s" % (url, modele, url_options) 
        return full_url;

