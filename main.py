#---------------------------------------------------------------------------
#Encoding: utf-8							  							   |
#!/usr/bin/python3							  							   |
#Channel users parser						   							   |
#Attention: The script will only work if you ARE a channel administrator!   |
#---------------------------------------------------------------------------
#Connect the necessary libraries:			   							   |
#---------------------------------------------------------------------------
from telethon.sync import TelegramClient
from telethon.tl.functions.channels import GetFullChannelRequest

#Get api_id and api_hash on the website: https://my.telegram.org/
api_id = 000000
api_hash = 'hash'
name_channel = 'my_channel'

#If necessary, enter the phone number and code from the SMS message
with TelegramClient('my_session', api_id, api_hash) as client:
	full = client(GetFullChannelRequest(name_channel))
	bio = full.users
	file = open('usernames.txt', 'a')
	for item in bio:
		file.write('@' + item.username)