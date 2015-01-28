#!/usr/bin/env python
# -*- coding: utf-8 -*- 

class Common(object):

    def __init__(self):
        self._model = None 

    def _url_construct(self, username, api_key, url_options):
        url = "https://%s:%s@api.challonge.com/v1/" % (username, api_key)
        return "%s%s.xml?%s" % (url, self.model, url_options)
