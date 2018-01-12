from slackeventsapi import SlackEventAdapter
from slackclient import SlackClient
import os

# Our app's Slack Event Adapter for receiving actions via the Events API
SLACK_VERIFICATION_TOKEN = os.environ["SLACK_VERIFICATION_TOKEN"]
slack_events_adapter = SlackEventAdapter(SLACK_VERIFICATION_TOKEN, "/slack/events")

# Create a SlackClient for your bot to use for Web API requests
SLACK_BOT_TOKEN = os.environ["SLACK_BOT_TOKEN"]
CLIENT = SlackClient(SLACK_BOT_TOKEN)


# Example responder to greetings
@slack_events_adapter.on("message")
def handle_message(event_data):
    message = event_data["event"]
    message_text = message.get('text')
    print(message_text)
    if message.get('subtype') is None and "take notes" in message_text:
        channel = message["channel"]
        print(channel)
        reply = "Ok, <@{}>! I will begin taking notes. :memo:".format(message["user"])
        # print(reply)
        CLIENT.api_call("chat.postMessage", channel=channel, text=reply)


# Example reaction emoji echo
@slack_events_adapter.on("reaction_added")
def reaction_added(event_data):
    event = event_data["event"]
    emoji = event["reaction"]
    print(emoji)
    channel = event["item"]["channel"]
    text = ":{}:".format(emoji)
    print(text)
    CLIENT.api_call("chat.postMessage", channel=channel, text=text)


# Once we have our event listeners configured, we can start the
# Flask server with the default `/events` endpoint on port 3000
slack_events_adapter.start(port=3000)

