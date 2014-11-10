#!/usr/bin/env python
# -*- coding: utf-8 -*- 

from challonge.common import * 

class Tournament(Common):

    def index(self, **kwargs):
        
        url_options = '&'.join(kwargs)

        self._url_construct(url_options)
        return url

    def __init__(self):
        self._model = "tournament"
        self._api_key = self

    def create(self, **kwargs):
        return self


