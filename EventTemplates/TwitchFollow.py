#!/usr/bin/env python2
# -*- coding: utf-8 -*-

from .CreateEventData import CreateEventData
import logging
logger = logging.getLogger(__name__)

def TwitchFollow(user_id, user_name, display_name, is_test=False, is_repeat=False):
	data = locals().copy()
	events = list()
	sl = [ "name", "display_name" ]
	v1 = [ "user_name", "display_name", "user_id", "is_test", "is_repeat" ]
	try:
		events.append({ "event": "TWITCH_FOLLOW_V1", "data": CreateEventData(v1, data, LiteralEval=True), "version": "1.0" })
		if not "name" in data and "user_name" in data:
			data["name"] = data["user_name"]
		events.append({ "event": "EVENT_FOLLOW", "data": CreateEventData(sl, data) })
	except KeyError as e:
		logger.error(e)
	return events
