#!/usr/bin/env python2
# -*- coding: utf-8 -*-

from .CreateEventData import CreateEventData
import logging
logger = logging.getLogger(__name__)

def TwitchRaid(user_id, user_name, display_name, raiders, is_test=False, is_repeat=False):
	data = locals().copy()
	events = list()
	sl = [ "name", "display_name", "raiders" ]
	v1 = [ "user_name", "display_name", "user_id", "raiders", "is_test", "is_repeat" ]
	try:
		events.append({ "event": "TWITCH_RAID_V1", "data": CreateEventData(v1, data, LiteralEval=True), "version": "1.0" })
		if "user_name" in data:
			data["name"] = data["user_name"]
		events.append({ "event": "EVENT_RAID", "data": CreateEventData(sl, data) })
	except KeyError as e:
		logger.error(e)
	return events
