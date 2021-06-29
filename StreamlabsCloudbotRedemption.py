#!/usr/bin/env python2
# -*- coding: utf-8 -*-

from .CreateEventData import CreateEventData
import logging
logger = logging.getLogger(__name__)

def StreamlabsCloudbotRedemption(user_name, recipient_user_name, product, display_name=None, recipient_display_name=None, image=None, condition=None, is_test=False, is_repeat=True):
	data = locals().copy()
	events = list()
	v1 = [ "user_name", "display_name", "user_id", "recipient_user_name", "recipient_display_name", "product", "image", "message", "is_test", "is_repeat" ]
	try:
		events.append({ "event": "STREAMLABS_REDEEM_V1", "data": CreateEventData(v1, data, LiteralEval=True), "version": "0.0-alpha" })
	except KeyError as e:
		logger.error(e)
	return events
