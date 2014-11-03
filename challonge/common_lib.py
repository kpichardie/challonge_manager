#!/usr/bin/env python
# -*- coding: utf-8 -*- 

class common_lib():

    def __init__(self):
        self = self

    def _url_construct(self, modele, url_options):
        url = "https://api.challonge.com/v1/"
        full_url = "%s%s.xml?%s" % (url, modele, url_options) 
        return full_url;

