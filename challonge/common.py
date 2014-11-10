#!/usr/bin/env python
# -*- coding: utf-8 -*- 

class Common(object):

    def __init__(self):
        self._model = None 

    def _url_construct(self, url_options):
        url = "https://api.challonge.com/v1/"
        full_url = "%s%s.xml?%s" % (url, self._model, url_options) 
        return full_url

