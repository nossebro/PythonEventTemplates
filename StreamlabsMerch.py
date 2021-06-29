#!/usr/bin/env python2
# -*- coding: utf-8 -*-

from .CreateEventData import CreateEventData
import logging
logger = logging.getLogger(__name__)

def StreamlabsMerch(user_name, product, display_name=None, image=None, condition=None, is_test=False, is_repeat=False):
	data = locals().copy()
	events = list()
	v1 = [ "user_name", "display_name", "user_id", "product", "image", "condition", "is_test", "is_repeat" ]
	try:
		events.append({ "event": "STREAMLABS_MERCH_V1", "data": CreateEventData(v1, data, LiteralEval=True), "version": "0.0-alpha" })
	except KeyError as e:
		logger.error(e)
	return events
