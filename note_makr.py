from slackeventsapi import SlackEventAdapter
from slackclient import SlackClient
import json
import os

# Our app's Slack Event Adapter for receiving actions via the Events API
SLACK_VERIFICATION_TOKEN = os.environ["SLACK_VERIFICATION_TOKEN"]
slack_events_adapter = SlackEventAdapter(SLACK_VERIFICATION_TOKEN, "/slack/events")

# Create a SlackClient for your bot to use for Web API requests
SLACK_BOT_TOKEN = os.environ["SLACK_BOT_TOKEN"]
CLIENT = SlackClient(SLACK_BOT_TOKEN)


@slack_events_adapter.on("message")
def take_notes(event_data):
    event = event_data["event"]
    if event.get('subtype') is None:
        message = event.get('text')
        user = event["user"]
        channel = event["channel"]
        timestamp = event.get('ts')
        file_name = "{}_{}notes.txt".format(user, channel)
        content = "[{} - {}]\n".format(timestamp, message)
        print(file_name)
        print(content)
        with open(file_name, 'a+') as file:
            file.write(content)
        reply = "It has been writen :memo:"
        CLIENT.api_call("chat.postMessage", channel=channel, text=reply)


# Once we have our event listeners configured, we can start the
# Flask server with the default `/events` endpoint on port 3000
slack_events_adapter.start(port=3000)

