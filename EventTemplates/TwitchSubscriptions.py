#!/usr/bin/env python2
# -*- coding: utf-8 -*-

from .CreateEventData import CreateEventData
import ast
import logging
logger = logging.getLogger(__name__)

def TwitchSubscriptions(user_id, user_name, display_name, sub_type, sub_plan, cumulative_months, is_gift, sub_plan_name=None, streak_months=None, message=None, recipient_user_id=None, recipient_user_name=None, recipient_display_name=None, multi_month_duration=None, is_test=False, is_repeat=False):
	data = locals().copy()
	events = list()
	sl = [ "name", "display_name", "tier", "is_resub", "months", "message", "is_gift", "is_mass_gift", "gift_target" ]
	v1 = [ "user_name", "display_name", "user_id", "sub_type", "sub_plan", "sub_plan_name", "cumulative_months", "streak_months", "message", "is_gift", "recipient_user_id", "recipient_user_name", "recipient_display_name", "multi_month_duration", "is_test", "is_repeat" ]
	try:
		events.append({ "event": "TWITCH_SUB_V1", "data": CreateEventData(v1, data, LiteralEval=True), "version": "1.0" })
		if str(sub_plan).lower() == "prime":
			data["tier"] = "1"
		else:
			data["tier"] = str(ast.literal_eval(data["sub_plan"]) / 1000)
		data["name"] = data["user_name"]
		data["months"] = data["cumulative_months"]
		if data["sub_type"] in [ "anonsubgift", "anonresubgift" ]:
			data["display_name"] = "Anonymous"
			data["name"] = data["display_name"].lower()
		if data["is_gift"] and "recipient_user_name" in data:
			data["gift_target"] = data["recipient_user_name"]
		events.append({ "event": "EVENT_SUB", "data": CreateEventData(sl, data) })
	except KeyError as e:
		logger.error(e)
	return events
