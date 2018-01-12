# Secretary Bot 

#### First: make your slack bot and app. here are some nice instructions:
<https://github.com/slackapi/python-slack-events-api>

<https://github.com/slackapi/python-slack-events-api/tree/master/example>

## Do the Dev
1. start ngrok
2. add https url to slack app
..- Even Subscriptions > Request Url
..- Manage Distribution > OAuth Redirect URL
3. put tokens in your .env
..- App Credentials > verification token = SLACK_VERIFICATION_TOKEN
..- OAuth & Permissions > Bot User Auth Token = SLACK_BOT_TOKEN
4. start bot script
5. prophet

Goal: connect to a goog doc for a constantly up-to-date google doc version of
the notes you are taking in your slack channel
