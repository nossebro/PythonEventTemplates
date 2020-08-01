from .CreateEventData import CreateEventData

def TwitchSubscriptions(data, Streamlabs = False):
	events = list()
	tier = str()
	try:
		tier = str(int(data["sub_plan"]) / 1000)
	except:
		tier = data["sub_plan"]
	data["tier"] = tier
	if "user_name" in data:
		data["name"] = data["user_name"]
	if not "months" in data:
		data["months"] = data["cumulative_months"]
	if "recipient_user_name" in data:
		data["gift_target"] = data["recipient_user_name"]
	if "sub_message" in data and "message" in data["sub_message"]:
		data["message"] = data["sub_message"]["message"]
	if "context" in data:
		data["sub_type"] = data["context"]
	sl = [ "name", "display_name", "tier", "is_resub", "months", "message", "is_gift", "is_mass_gift", "gift_target" ]
	v1 = [ "user_name", "display_name", "user_id", "sub_type", "sub_plan", "sub_plan_name", "cumulative_months", "streak_months", "message", "is_gift", "recipient_id", "recipient_user_name", "recipient_display_name", "multi_month_duration" ]
	if Streamlabs:
		events.append({ "event": "EVENT_SUB", "data": CreateEventData(sl, data) })
	events.append({ "event": "TWITCH_SUB_V1", "data": CreateEventData(v1, data), "version": "1.0" })
	return events
