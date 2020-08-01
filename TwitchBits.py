from .CreateEventData import CreateEventData

def TwitchBits(data, Streamlabs = False):
	events = list()
	if "user_name" in data:
		data["name"] = data["user_name"]
	if "badge_entitlement" in data and data["badge_entitlement"] and "new_version" in data["badge_entitlement"] and "previous_version" in data["badge_entitlement"] and data["badge_entitlement"]["new_version"] > 0:
		data["is_new_badge_tier"] = True
		data["old_badge"] = data["badge_entitlement"]["previous_version"]
		data["new_badge"] = data["badge_entitlement"]["new_version"]
	if "bits_used" in data:
		data["bits"] = data["bits_used"]
	if "total_bits_used" in data:
		data["total_bits"] = data["total_bits_used"]
	if "chat_message" in data:
		data["message"] = data["chat_message"]
	sl = [ "name", "display_name", "bits", "total_bits", "message" ]
	v1 = [ "user_name", "display_name", "user_id", "bits", "total_bits", "is_anonymous", "is_new_badge_tier", "old_badge", "new_badge", "is_test", "is_repeat" ]
	if Streamlabs:
		events.append({ "event": "EVENT_CHEER", "data": CreateEventData(sl, data) })
	events.append({ "event": "TWITCH_BIT_V1", "data": CreateEventData(v1, data), "version": "1.0" })
	return events
