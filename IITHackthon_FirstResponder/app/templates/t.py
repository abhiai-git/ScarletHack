import requests,json
r = requests.post("https://sms.telnyx.com/send",
		data=json.dumps({
			"from": "+17733022716",
			"to": "+13126238253",
			"body": "Hi Sachin and Alan,  Join Me @AICollab!!!! at Call : Surgery1 at 1 pm Sunday 24th September 2017 Cheer AI Collab, RoomName: demo"
			}),
		headers={
			"x-profile-secret": "jSqkQ280CinfZkBBMQj3Do9K",
			"content-type": 'application/json'
		})