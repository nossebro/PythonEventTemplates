#!/usr/bin/env python2
# -*- coding: utf-8 -*-

from .CreateEventData import CreateEventData
import logging
logger = logging.getLogger(__name__)

def StreamlabsDonation(user_name, amount, currency, message, user_id=None, display_name=None, formatted_amount=None, source=None, is_test=False, is_repeat=False):
	data = locals().copy()
	events = list()
	sl = [ "userId", "name", "display_name", "amount", "currency", "message" ]
	v1 = [ "user_id", "user_name", "display_name", "amount", "formatted_amount", "currency", "source", "message", "is_test", "is_repeat" ]
	try:
		events.append({ "event": "STREAMLABS_DONATION_V1", "data": CreateEventData(v1, data, LiteralEval=True), "version": "1.0" })
		data["name"] = data["userId"] = user_name
		if display_name:
			data["userId"] = display_name
		events.append({ "event": "EVENT_DONATION", "data": CreateEventData(sl, data) })
	except KeyError as e:
		logger.error(e)
	return events
