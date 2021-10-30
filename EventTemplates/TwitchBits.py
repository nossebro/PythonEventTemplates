#!/usr/bin/env python2
# -*- coding: utf-8 -*-

from .CreateEventData import CreateEventData
import logging
logger = logging.getLogger(__name__)

def TwitchBits(user_id, user_name, display_name, bits, total_bits, message, is_anonymous, is_new_badge_tier=False, badge_tier=None, is_test=False, is_repeat=False):
	data = locals().copy()
	events = list()
	sl = [ "name", "display_name", "bits", "total_bits", "message" ]
	v1 = [ "user_name", "display_name", "user_id", "bits", "total_bits", "is_anonymous", "is_new_badge_tier", "badge_tier", "is_test", "is_repeat" ]
	try:
		events.append({ "event": "TWITCH_BIT_V1", "data": CreateEventData(v1, data, LiteralEval=True), "version": "1.0" })
		if "is_anonymous" in data and data["is_anonymous"]:
			data["display_name"] = "AnAnonymousCheerer"
			data["name"] = data["display_name"].lower()
		elif not "name" in data and "user_name" in data:
			data["name"] = data["user_name"]
		events.append({ "event": "EVENT_CHEER", "data": CreateEventData(sl, data) })
	except KeyError as e:
		logger.error(e)
	return events
