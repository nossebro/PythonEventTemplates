from .CreateEventData import CreateEventData

def TwitchChannelPoints(data):
	events = list()
	data["user_name"] = data["user"]["login"]
	data["display_name"] = data["user"]["display_name"]
	data["user_id"] = data["user"]["id"]
	data["reward_id"] = data["reward"]["id"]
	data["cost"] = data["reward"]["cost"]
	data["title"] = data["reward"]["title"]
	data["prompt"] = data["reward"]["prompt"]
	v1 = [ "user_name", "display_name", "user_id", "reward_id", "cost", "title", "prompt", "is_test", "is_repeat" ]
	events.append({ "event": "TWITCH_REWARD_V1", "data": CreateEventData(v1, data), "version": "1.0" })
	return events
