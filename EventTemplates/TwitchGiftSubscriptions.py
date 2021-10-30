#!/usr/bin/env python2
# -*- coding: utf-8 -*-

from .CreateEventData import CreateEventData
import logging
logger = logging.getLogger(__name__)

def TwitchGiftSubscriptions(user_id, user_name, display_name, sub_plan, amount, sub_type=None, total=None, message=None, is_test=False, is_repeat=False):
	data = locals().copy()
	events = list()
	v1 = [ "user_name", "display_name", "user_id", "sub_type", "sub_plan", "amount", "total", "message", "is_test", "is_repeat" ]
	try:
		events.append({ "event": "TWITCH_GIFTSUB_V1", "data": CreateEventData(v1, data, LiteralEval=True), "version": "1.0" })
	except KeyError as e:
		logger.error(e)
	return events
