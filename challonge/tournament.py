#!/usr/bin/env python
# -*- coding: utf-8 -*- 

from common import *


class Tournament(Common):

    def __init__(self, username, api_key, name=None, tournament_type=None, url=None, subdomain=None, description=None,
                 open_signup=None, hold_third_place_match=None, pts_for_match_win=None, pts_for_match_tie=None,
                 pts_for_game_win=None, pts_for_game_tie=None, pts_for_bye=None, swiss_rounds=None, ranked_by=None,
                 rr_pts_for_match_win=None, rr_pts_for_match_tie=None, rr_pts_for_game_win=None,
                 rr_pts_for_game_tie=None, accept_attachments=None, hide_forum=None, show_rounds=None, private=None,
                 notify_users_when_matches_open=None, notify_users_when_the_tournament_ends=None):
        self.model = "tournament"
        self.username = username
        self.api_key = api_key
        self.name = name
        self.tournament_type = tournament_type
        self.url = url
        self.subdomain = subdomain
        self.description = description
        self.open_signup = open_signup
        self.hold_third_place_match = hold_third_place_match
        self.pts_for_match_win = pts_for_match_win
        self.pts_for_match_tie = pts_for_match_tie
        self.pts_for_game_win = pts_for_game_win,
        self.pts_for_game_tie = pts_for_game_tie
        self.pts_for_bye = pts_for_bye
        self.swiss_rounds = swiss_rounds
        self.ranked_by = ranked_by
        self.rr_pts_for_match_win = rr_pts_for_match_win
        self.rr_pts_for_match_tie = rr_pts_for_match_tie
        self.rr_pts_for_game_win = rr_pts_for_game_win
        self.rr_pts_for_game_tie = rr_pts_for_game_tie
        self.accept_attachments = accept_attachments
        self.hide_forum = hide_forum
        self.show_rounds = show_rounds
        self.private = private
        self.notify_users_when_matches_open = notify_users_when_matches_open
        self.notify_users_when_the_tournament_ends = notify_users_when_the_tournament_ends


    #def index(self, state=None, type=None, created_after=None, created_before=None, subdomain=None, **kwargs):
    #    if state:
    #        url_options = '&'.join(state)
    #    if type:
    #        url_options = '&'.join(type)
    #    if created_after:
    #        url_options = '&'.join(created_after)
    #    if created_before:
    #        url_options = '&'.join(created_before)
    #    if subdomain:
    #        url_options = '&'.join(subdomain)

    def index(self, **kwargs):
        url_options = '&'.join(kwargs)
        return self._url_construct(self.username, self.api_key, url_options)

    def create(self, **kwargs):
        #url_options = '&'.join(self.name, self.tournament_type, self.url, self.subdomain, self.description,
        #                       self.open_signup, self.hold_third_place_match, self.pts_for_match_win,
        #                       self.pts_for_match_tie, self.pts_for_game_win, self.pts_for_game_tie, self.pts_for_bye,
        #                       self.swiss_rounds, self.ranked_by, self.rr_pts_for_match_win, self.rr_pts_for_match_tie,
        #                       self.rr_pts_for_game_win, self.rr_pts_for_game_tie, self.accept_attachments,
        #                       self.hide_forum, self.show_rounds, self.private, self.notify_users_when_matches_open,
        #                       self.notify_users_when_the_tournament_ends)
        url_options = '&'.join(kwargs)
        return self._url_construct(self.username, self.api_key, url_options)

    def show(self, **kwargs):
        return self

    def show(self, **kwargs):
        return self

    def destroy(self, **kwargs):
        return self

    def process_check_ins(self, **kwargs):
        return self

    def abort_check_ins(self, **kwargs):
        return self

    def start(self, **kwargs):
        return self

    def finalize(self, **kwargs):
        return self

    def reset(self, **kwargs):
        return self

