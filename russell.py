#!/usr/bin/python3
###
# Copyright (c) 2020, Russell B.
# All rights reserved.
#
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions are met:
#
#   * Redistributions of source code must retain the above copyright notice,
#     this list of conditions, and the following disclaimer.
#   * Redistributions in binary form must reproduce the above copyright notice,
#     this list of conditions, and the following disclaimer in the
#     documentation and/or other materials provided with the distribution.
#   * Neither the name of the author of this software nor the name of
#     contributors to this software may be used to endorse or promote products
#     derived from this software without specific prior written consent.
#
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS"
# AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
# IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE
# ARE DISCLAIMED.  IN NO EVENT SHALL THE COPYRIGHT OWNER OR CONTRIBUTORS BE
# LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR
# CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF
# SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS
# INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN
# CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE)
# ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE
# POSSIBILITY OF SUCH DAMAGE.
###

#### Imports ###
import hexchat
try:
	from datetime import datetime
	import hashlib
	import json
	import os
	import platform
	import re
	import requests
	import random
	import socket
	import string
	import struct
	import time
	import twitter
except ImportError as e:
	print("\002** WARNING:\002 One or more of the required python modules could not be found for this plugin. Please ensure you have installed the required modules.")
	print(f"\002**\002 The error message returned was: {e}")

### Initialise Information ####
__module_name__ = "Russell's Awsome Plugin"
__module_version__ = "1.0"
__module_description__ = "Russell's Awsome Plugin for Hexchat (2021 Edition)"

hexchat.command(f"echo \002**\002 {__module_name__} v{__module_version__} Loaded")

#### Configuration ####

close_on_disconnect = False
custom_ctcps = True
join_on_invite = True
require_sasl = True
wallops_seperate = False
whois_on_private = True

# Custom CTCP Replies - OS/TIME/DATE/VERSION are already customised in hook_ctcp
custom_ctcp_replies = {
			'FINGER': "I don't want fingering!"
}

# Networks for which SASL is required and will not connect if SASL fails
require_sasl_networks = (
			'Freenode'
)

# Twitter Configuration for /tweet - Obtain keys from https://developer.twitter.com/
twitter = {
			'consumer_key': '',
			'consumer_secret': '',
			'access_token': '',
			'access_secret': ''
}

# LastFM configuration for /np - Obtain keys from https://www.last.fm/api
lastfm = {
			'api_url': 'http://ws.audioscrobbler.com/2.0/',
			'api_key': '',
			'username': ''
}

# Wallops Window Name
wallops_window = "(wallops)"

# Drunk Data Filename
drunk_config = "drunk.conf"
drunk_custom_date = "01/01/2021"

#### End of Configuration ####


#### Command Help Strings ####
help = {
			'banhammer': "\002/bh [nickname]\002 -- Hit a given nickname with a ban hammer",
			'bass': "\002/bass\002 -- Displays the words 'turn up the music' with a large ascii",
			'binary': "\002/binary [number]\002 -- Convert a number into binary",
			'brag': "\002/brag\002 -- Show the current channel how many networks/channels your on and how many people you have power over",
			'chatprotect': "\002/chatprotect\002 -- Displays a chat protect message in the current channel",
			'dec2ip': "\002/dec2ip\002 -- Convert/Translate a decimal IP into a normal IPv4 address",
			'dieman': "\002/dieman\002 --Displays an ascii comic of a man being shot",
			'drink': "\002/drink\002 -- Have a drink and update the data for the drunk command",
			'drunk': "\002/drunk\002 -- Shows how many times you got drunk and when it last was",
			'flip': "\002/flip [text]\002 -- Flips the text you write upside down and writes it in the current channel",
			'hashed': "\002/hashed [string]\002 -- Generate an hash using a algorith and word/string",
			'hex': "\002/hex [number]\002 -- Convert a number into a hexadecimal",
			'hex2ip': "\002/hex2ip [hexadecimal ip]\002 -- Convert/Translate a hexadecimal IP into a normal IPv4 address",
			'ip2dec': '\002/ip2dec [IPv4 address]\002 -- Convert an IPv4 address into decimal',
			'ip2hex': '\002/ip2hex [IPv4 address]\002 -- Convert an IPv4 address into hexadecimal',
			'lag': "\002/lag\002 -- Displays your lag time to the current channel",
			'man': "\002/man\002 -- Displays an ascii man",
			'melon': "\002/melon\002 -- Displays a giant melon in the current channel",
			'music': "\002/music\002 -- Displays the word 'music' in a large ascii",
			'nowplaying': "\002/np\002 -- Show the track you are currently playing to the current channel (Uses LastFM)",
			'num': "\002/num [hex/oct/binary]\002 -- Convert a hexadecimal, octal or binary into a number",
			'oct': "\002/oct [number]\002 -- Convert a number into octal",
			'rainbow': "\002/rainbow [text]\002 -- Writes text in rainbow colors to the given channel",
			'short': "\002/short [url]\002 -- Shortens a given URL",
			'slap': "\002/slap [nickname]\002 -- Slap a given nickname with a random object",
			'soap': "\002/soap\002 -- Displays a large ascii soap",
			'twitter': "\002/twitter [message]\002 -- Sends a tweet to your twitter account. (Requires Twitter Configuration)"
}

#### General Commands ####

def command_melon(command, command_eol, params):
	hexchat.command("say \x031,1melonmelo\x033,3n\x031,1mel")
	hexchat.command("say \x031,1melonmel\x034,4o\x033,3nm\x031,1el")
	hexchat.command("say \x031,1melonme\x034,4lon\x033,3me\x031,1l")
	hexchat.command("say \x031,1melonm\x034,4elo\x035,5n\x034,4m\x033,3el")
	hexchat.command("say \x031,1melon\x034,4melonm\x033,3el")
	hexchat.command("say \x031,1melo\x034,4nme\x035,5l\x034,4onm\x033,3el")
	hexchat.command("say \x031,1mel\x034,4onmelonm\x033,3el")
	hexchat.command("say \x031,1me\x034,4lon\x035,5m\x034,4elon\x033,3me\x031,1l")
	hexchat.command("say \x031,1m\x034,4el\x035,5o\x034,4nmelon\x033,3m\x031,1el")
	hexchat.command("say \x033,3m\x034,4elonmelo\x033,3nm\x031,1el")
	hexchat.command("say \x033,3me\x034,4lonme\x033,3lon\x031,1mel")
	hexchat.command("say \x031,1m\x033,3elonmel\x031,1onmel")
	hexchat.command("say \x031,1melonmelonmel")
	return 1

hexchat.hook_command("melon", command_melon, help=help['melon'])


def command_chatprotect(command, command_eol, params):
	hexchat.command("say Tᴏ ᴘʀᴏᴛᴇᴄᴛ ᴛʜᴇ ᴄʜᴀᴛ ғʀᴏᴍ ᴅᴇᴠᴀsᴛᴀᴛɪᴏɴ. ᴛᴏ ᴜɴɪᴛᴇ ᴀʟʟ sᴘᴀᴍᴍᴇʀs ᴡɪᴛʜɪɴ ᴏᴜʀ ɴᴀᴛɪᴏɴ. ᴛᴏ ᴅᴇɴᴏᴜɴᴄᴇ ᴛʜᴇ ᴇᴠɪʟ ᴏғ Tʀᴜᴍᴘ ᴀɴᴅ ᴍᴏᴅs. ᴛᴏ ᴇxᴛᴇɴᴅ ᴏᴜʀ sᴘᴀᴍ ᴛᴏ ᴛʜᴇ sᴛᴀʀs ᴀʙᴏᴠᴇ. ᴄᴏᴘʏ! ᴘᴀsᴛᴇ! ᴄʜᴀᴛ!")
	return hexchat.EAT_HEXCHAT

hexchat.hook_command("chatprotect", command_chatprotect, help=help['chatprotect'])


def command_dieman(command, command_eol, params):
	hexchat.command(r"say < DIEEEEEEEEEEEE > ")
	hexchat.command(r"say                  \ ")
	hexchat.command(r"say                   \ ")
	hexchat.command(r"say    \o/             o ")
	hexchat.command(r"say     █      - - ─╤╦.█\ ")
	hexchat.command(r"say    .Π.            .Π. ")
	return hexchat.EAT_HEXCHAT

hexchat.hook_command("dieman", command_dieman, help=help['dieman'])


def command_soap(command, command_eol, params):
	hexchat.command("say  ╭━━━━╮")
	hexchat.command("say  ┃╭╮╭╮┃")
	hexchat.command("say ┗┫┏━━┓┣┛")
	hexchat.command("say  ┃╰━━╯┃")
	hexchat.command("say  ╰┳━━┳╯")
	return hexchat.EAT_HEXCHAT

hexchat.hook_command("soap", command_soap, help=help['soap'])


def command_bass(command, command_eol, params):
	hexchat.command("say ╔══╗ ♫  ＴＵＲＮ ＵＰ ＴＨＥ")
	hexchat.command("say ║██║ ♪♪ ╔══════╦═╗╔═╦═══╦═╦═══╗")
	hexchat.command("say ║██║♫♪  ║░╔╗╔╗░║░║║░║╚══╣░║░╔═╝")
	hexchat.command("say ║ ◎♫♪♫  ║░║╚╝║░║░╚╝░╠══╗║░║░╚═╗")
	hexchat.command("say ╚══╝    ╚═╝░░╚═╩════╩═══╩═╩═══╝")
	return hexchat.EAT_HEXCHAT

hexchat.hook_command("bass", command_bass, help=help['bass'])


def command_music(command, command_eol, params):
	hexchat.command("say ╔══════╦═╗╔═╦═══╦═╦═══╗")
	hexchat.command("say ║░╔╗╔╗░║░║║░║╚══╣░║░╔═╝")
	hexchat.command("say ║░║╚╝║░║░╚╝░╠══╗║░║░╚═╗ ")
	hexchat.command("say ╚═╝░░╚═╩════╩═══╩═╩═══╝")
	return hexchat.EAT_HEXCHAT

hexchat.hook_command("music", command_music, help=help['music'])


def command_man(command, command_eol, params):
	hexchat.command(r"say \o/ ")
	hexchat.command(r"say  |  ")
	hexchat.command(r"say / \ ")
	return hexchat.EAT_HEXCHAT

hexchat.hook_command("man", command_man, help=help['man'])


def command_lag(command, command_eol, params): 
	server = hexchat.get_info("server")
	channel = hexchat.get_info("channel")
	context = hexchat.get_list('channels')

	for index,item in enumerate(context):
		if context[index].channel == channel and context[index].server == server:
			hexchat.command(f"say \002My Current Lag:\002 {(context[index].lag/1000)} seconds") 
	return hexchat.EAT_HEXCHAT

hexchat.hook_command('lag', command_lag, help=help['lag'])

def command_slap(command, command_eol, params): 
	try:
		hexchat.command(f"ACTION {slap(command[1])}")
	except IndexError:
		print(f"\002** Syntax:\002 /{command[0]} [nickname]")
	return hexchat.EAT_HEXCHAT

hexchat.hook_command('slap', command_slap, help=help['slap'])

def command_banhammer(command, command_eol, params): 
	try:
		hexchat.command(f"ACTION is getting out the ban hammer for {command_eol[1]}! ▬▬▬▬▬▬▬▋ Ò╭╮Ó")
	except IndexError:
		print(f"\002** Syntax:\002 /{command[0]} [nickname]")
	return hexchat.EAT_HEXCHAT

hexchat.hook_command('bh', command_banhammer, help=help['banhammer'])


def command_flip(command, command_eol, params): 
	chars = {
			"a": "ɐ", "b": "q", "c": "ɔ",
			"d": "p", "e": "ǝ", "f": "ɟ", 
			"g": "ƃ", "h": "ɥ", "i": "ı", 
			"j": "ɾ", "k": "ʞ", "l": "l", 
			"m": "ɯ", "n": "u", "o": "o", 
			"p": "d", "q": "b", "r": "ɹ",
			"s": "s", "t": "ʇ", "u": "n",
			"v": "ʌ", "w": "ʍ", "x": "x",
			"y": "ʎ", "z": "z", "!": "¡",

			"A": "∀", "B": "q", "C": "Ɔ", 
			"D": "◖", "E": "Ǝ", "F": "Ⅎ", 
			"G": "⅁", "H": "H", "I": "I", 
			"J": "ſ", "K": "⋊", "L": "˥", 
			"M": "W", "N": "N", "O": "O", 
			"P": "Ԁ", "Q": "Ό", "R": "ᴚ",
			"S": "s", "T": "⊥", "U": "∩",
			"V": "Λ", "W": "ʍ", "X": "X",
			"Y": "⅄", "Z": "Z", "?": "¿",

			"1": "Ɩ", "2": "ᄅ", "3": "Ɛ",
			"4": "ㄣ", "5": "ϛ", "6": "9",
			"7": "ㄥ", "8": "8", "9": "6",
			"0": "0", "_": "‾", "/": "\\",
			"\\": "/", "`": ",", ".": "˙",
			"(": ")", ")": "(", "[": "]",
			"]": "[", "<": ">", ">": "<",
			"{": "}", "}": "{", "\"": ",,",
			"&": "⅋"
	}

	try:
		newstring = ""
		for character in command_eol[1]:
			try:
				character = character.replace(character, chars[character])
			except KeyError:
				pass

			newstring += character

		newstring = ''.join(reversed(newstring))
		hexchat.command(f"say {newstring}") 
	except IndexError:
		print(f"\002** Syntax:\002 /{command[0]} [text]")
	return hexchat.EAT_HEXCHAT

hexchat.hook_command('flip', command_flip, help=help['flip'])


def command_rainbow(command, command_eol, params): 
	newstring = ""
	try:
		for character in command_eol[1]:
			character = character.replace(character, f"\x03{random.randrange(14)}{character}")
			newstring += character
	except IndexError:
		print(f"\002** Syntax:\002 /{command[0]} [text]")
		return hexchat.EAT_ALL

	hexchat.command(f"say {newstring}\x0f") 
	return hexchat.EAT_ALL

hexchat.hook_command('rainbow', command_rainbow, help=help['rainbow'])


def command_hashed(command, command_eol, params):
	try:
		algorithm = command[1]
		string = command_eol[2]
		if algorithm.lower() not in hashlib.algorithms_available:
			print("\002** Error:\002 Algorithm not available.")
			return hexchat.EAT_ALL
		else:
			print(f"\002** \002Your {algorithm} Hash is: {hashlib.new(algorithm, string.encode('utf8')).hexdigest()}")
			return hexchat.EAT_ALL
	except IndexError:
		print(f"\002** Syntax:\002 /{command[0]} [string]")
		print(f"\002** Valid Hash Types:\002 {', '.join(hashlib.algorithms_available)}")
		return hexchat.EAT_HEXCHAT

if hasattr(hashlib, 'algorithms_available'):	
	hexchat.hook_command('hashed', command_hashed, help=help['hashed'])

def command_hex(command, command_eol, params):
	try:
		command[1]
	except IndexError:
		print(f"\002** Syntax:\002 /{command[0]} [number]")		
		return hexchat.EAT_HEXCHAT

	if not re.search('^[\d ()]+$', command[1]):
		print(f"\002** Error:\002 Must be a number")
		return hexchat.EAT_HEXCHAT

	print(f"\002**\002 {command[1]} as a hexadecimal is {hex(int(command[1]))}")
	return hexchat.EAT_ALL

hexchat.hook_command('hex', command_hex, help=help['hex'])

def command_oct(command, command_eol, params):
	try:
		command[1]
	except IndexError:
		print(f"\002** Syntax:\002 /{command[0]} [number]")		
		return hexchat.EAT_HEXCHAT

	if not re.search('^[\d ()]+$', command[1]):
		print(f"\002** Error:\002 Must be a number")
		return hexchat.EAT_HEXCHAT

	print(f"\002**\002 {command[1]} as an octal is {oct(int(command[1]))[2:]}")
	return hexchat.EAT_ALL

hexchat.hook_command('oct', command_oct, help=help['oct'])

def command_binary(command, command_eol, params):
	try:
		command[1]
	except IndexError:
		print(f"\002** Syntax:\002 /{command[0]} [number]")		
		return hexchat.EAT_HEXCHAT

	if not re.search('^[\d ()]+$', command[1]):
		print(f"\002** Error:\002 Must be a number")
		return hexchat.EAT_HEXCHAT

	binary = "{0:b}".format(int(command[1]))
	print(f"\002**\002 {command[1]} as a binary is {binary}")
	return hexchat.EAT_ALL

hexchat.hook_command('bin', command_binary, help=help['binary'])

def command_num(command, command_eol, params):
	try:
		command[1]
	except IndexError:
		print(f"\002** Syntax:\002 /{command[0]} [number]")		
		return hexchat.EAT_HEXCHAT

	try:
		print(f"\002**\002 {command[1]} as a number is {int(str(command[1]), 0)}")
		return hexchat.EAT_HEXCHAT
	except ValueError:
		print(f"\002** Error:\002 {command[1]} cannot be converted to a number")
		return hexchat.EAT_HEXCHAT

hexchat.hook_command('num', command_num, help=help['num'])

def command_drunk(command, command_eol, params):
	try:
		f = open(f"{hexchat.get_info('configdir')}/{drunk_config}", "r")
		data = f.read()
		f.close()
	except IOError as e:
		print(f"\002** Error:\002 Drunk configuration file could not be read ({e})")
		return hexchat.EAT_HEXCHAT
		
	data = data.split(":")
	try:
		drinks_since = datetime(*(time.strptime(drunk_custom_date, "%d/%m/%Y")[0:6]))
	except (NameError, UnboundLocalError, ValueError, TypeError):
		drinks_since = datetime.fromtimestamp(int(os.path.getctime(f"{hexchat.get_info('configdir')}/{drunk_config}")))
	last_drink = datetime.now() - datetime.fromtimestamp(int(data[0].strip()))
	if (last_drink.days == 0) and (last_drink.seconds < 60):
		time_passed = "%s seconds ago" % last_drink.seconds
	elif last_drink.days == 0 and last_drink.seconds < 3600:
		time_passed = "%s minutes ago" % int(last_drink.seconds / 60 )
	elif last_drink.days == 0:
		time_passed = "%s hours ago" % int(last_drink.seconds / 3600 )
	else:
		time_passed = "%s days ago" % last_drink.days
	hexchat.command(f"say \002Last Drink Consumed:\002 {time_passed} ({data[1].strip()} drinks since {drinks_since.strftime('%d/%m/%Y')})")
	return hexchat.EAT_ALL

if os.path.exists(f"{hexchat.get_info('configdir')}/{drunk_config}"):
	hexchat.hook_command('drunk', command_drunk, help=help['drunk'])


def command_drink(command, command_eol, params):
	try:
		if not os.path.exists(f"{hexchat.get_info('configdir')}/{drunk_config}"):
			f = open(f"{hexchat.get_info('configdir')}/{drunk_config}", "w+")
			drinks_consumed = 1
		else:
			f = open(f"{hexchat.get_info('configdir')}/{drunk_config}", "r+")
			data = f.read()
			data = data.split(":")
			drinks_consumed = int(data[1].strip())+1

		f.seek(0)
		f.write(f"{int(time.time())}:{drinks_consumed}")
		f.truncate()
		f.close()
	except IOError as e:
		print(f"\002** Error:\002 Drunk configuration file could not be written ({e})")
		return hexchat.EAT_HEXCHAT
		
	print("\002** Drink Consumed!\002")
	return hexchat.EAT_ALL

hexchat.hook_command('drink', command_drink, help=help['drink'])


#### Brag/Stats ####

def command_brag(command, command_eol, params):
	opped = 0
	whole = 0
	znetworks = 0
	ownerchans = 0
	protectchans = 0
	oppedchans = 0
	hoppedchans = 0
	voppedchans = 0
	wholechannels = 0
	queries = 0

	oldcontext = hexchat.get_context()
	channels = hexchat.get_list('channels')

	for temp in channels:
		ztype = temp.type
		zid = temp.id;
		if ztype == 1:
			znetworks += 1
		elif ztype == 2:
			chan = temp.channel
			context = hexchat.find_context(channel=chan)
			context.set()
			userinfo = get_user(hexchat.get_info('nick'))
			if re.match("^[~\!]$", userinfo.prefix):
				users = hexchat.get_list('users')
				ownerchans += 1
				wholechannels += 1
				opped = opped+len(users)
				whole = whole+len(users)
			elif re.match("^[&\!]$", userinfo.prefix):
				users = hexchat.get_list('users')
				protectchans += 1
				wholechannels += 1
				opped = opped+len(users)
				whole = whole+len(users)
			elif re.match("^[@\!]$", userinfo.prefix):
				users = hexchat.get_list('users')
				oppedchans += 1
				wholechannels += 1
				opped = opped+len(users)
				whole = whole+len(users)
			elif re.match("^[%\!]$", userinfo.prefix):
				husers = hexchat.get_list('users')
				hoppedchans += 1
				wholechannels += 1
				opped = opped+len(husers)
				whole = whole+len(husers)
			elif re.match("^[+\!]$", userinfo.prefix):
				vusers = hexchat.get_list('users')
				voppedchans += 1
				wholechannels += 1
				whole = whole+len(vusers)
			else:
				uopusers = hexchat.get_list('users')
				wholechannels += 1
				whole = whole+len(uopusers)
		elif ztype == 3:
			queries += 1

	oldcontext.set()
	hexchat.command(f"say \002[STATS]\002 I am in {wholechannels} channels and private messaging {queries} people across {znetworks} networks. (Owner: {ownerchans}, Protected: {protectchans}, Op'd: {oppedchans}, Halfop'd: {hoppedchans}, Voiced: {voppedchans})")
	hexchat.command(f"say \002[STATS]\002 I currently have non-abusive power and mind-blowing influence over {opped} people")
	return hexchat.EAT_HEXCHAT

hexchat.hook_command('brag', command_brag, help=help['brag'])


#### Short URL ####

def command_short(command, command_eol, params): 
	
	try:
		url = command[1]
	except IndexError:
		print(f"\002** Syntax:\002 /{command[0]} [text]")
		return hexchat.EAT_ALL

	http_headers = {
		'User-Agent': f"Hexchat {__module_name__} v{__module_version__}"				
	}
	http_variables = {
		'url': url
	}

	try:
		r = requests.post("https://f0rk.in/api/create.php", http_variables, headers=http_headers, timeout=5)
	except requests.exceptions.RequestException as e:
		print(f"\002** Error:\002 HTTP Error {e}")
		return hexchat.EAT_ALL

	if r.status_code != 200:
		print(f"\002** Error:\002 Code {r.status_code} returned")
		return hexchat.EAT_ALL
		

	hexchat.command(f"say {r.text}\x0f")
	return hexchat.EAT_HEXCHAT

hexchat.hook_command('short', command_short, help=help['short'])

#### Twitter ####

def command_twitter(command, command_eol, params):
	try:
		message = command_eol[1]
	except IndexError:
		print(f"\002** Syntax:\002 /{command[0]} [message]")
		return hexchat.EAT_ALL

	api = twitter.Api(consumer_key=twitter['consumer_key'],
                      consumer_secret=twitter['consumer_secret'],
                      access_token_key=twitter['access_token'],
                      access_token_secret=twitter['access_secret'])

	if not api.VerifyCredentials():
		print("\002Twitter Error:\002 Your API credentials are incorrect. Check you have the correct keys from https://developer.twitter.com/")
		return hexchat.EAT_ALL

	try:
		if len(message) > 240:
		    split_messages = []
		    for index in range(0, len(message), 231):
		        split_messages.append(message[index : index + 231])

		    message_max = len(split_messages)
		    message_count = 1
		    
		    for part_message in split_messages:
		        if message_count == 1:
		            api.PostUpdate(f"({message_count}/{message_max}) {part_message}...")
		        elif message_count == message_max:
		            api.PostUpdate(f"({message_count}/{message_max}) ...{part_message}")
		        else:
		            api.PostUpdate(f"({message_count}/{message_max}) ...{part_message}...")
		        message_count = message_count + 1
		else:
		    api.PostUpdate(message)
		hexchat.command("echo \002**\002 Tweet posted successfully!")
		return hexchat.EAT_HEXCHAT
	except twitter.error.TwitterError as e:
		print(f"\002Twitter Error:\002 Tweets were not posted ({e})")
		return hexchat.EAT_ALL
		
hexchat.hook_command('twitter', command_short, help=help['twitter'])

#### LastFM ####
def command_nowplaying(command, command_eol, params):
	http_headers = {
		'User-Agent': f"Hexchat {__module_name__} v{__module_version__}"				
	}
	http_variables = {
		'api_key': lastfm['api_key'],
		'user': lastfm['username'],
		'method': 'user.getrecenttracks',
		'format': 'json'
	}

	try:
		r = requests.get(lastfm['api_url'], http_variables, headers=http_headers, timeout=5)
	except requests.exceptions.RequestException as e:
		print(f"\002** Error:\002 HTTP Error {e}")
		return hexchat.EAT_ALL

	if r.status_code != 200:
		print(f"\002** Error:\002 Code {r.status_code} returned")
		return hexchat.EAT_ALL

	try:
		data = json.loads(r.text)["recenttracks"]
	except KeyError:
		print(f"\002** Error:\002 You do not have any recent tracks")
		return hexchat.EAT_ALL

	user = data["@attr"]["user"]
	tracks = data["track"]

	try:
		trackdata = tracks[0]
	except IndexError:
		print(f"\002** Error:\002 You have not listened to anything yet")
		return hexchat.EAT_ALL

	artist = trackdata["artist"]["#text"].strip()
	track = trackdata["name"].strip()
	album = trackdata["album"]["#text"].strip()
	if album:
		album = " [%s]" % album
	else:
		album = ""

	try:		
		last_play = datetime.now() - datetime.fromtimestamp(int(trackdata["date"]["uts"]))
		if (last_play.days == 0) and (last_play.seconds < 60):
			time_passed = "%s seconds ago" % last_play.seconds
		elif last_play.days == 0 and last_play.seconds < 3600:
			time_passed = "%s minutes ago" % int(last_play.seconds / 60 )
		elif last_play.days == 0:
			time_passed = "%s hours ago" % int(last_play.seconds / 3600 )
		else:
			time_passed = "%s days ago" % last_play.days
	except KeyError:
		time_passed = "right now"

	try:
	   trackdata["@attr"]["nowplaying"]
	   hexchat.command(f"action is listening to \002{track}\002 by \002{artist}\002{album}")
	except:
	   hexchat.command(f"action was listening to \002{track}\002 by \002{artist}\002{album} ({time_passed})")

	return hexchat.EAT_HEXCHAT
	
hexchat.hook_command('np', command_nowplaying, help=help['nowplaying'])


#### IP Utilities ####

def command_hex2ip(command, command_eol, params):
	try:
		hexip = command_eol[1]
	except IndexError:
		print(f"\002** Syntax:\002 /{command[0]} [hexadecimal ip]")
		return hexchat.EAT_ALL

	if all(c in string.hexdigits for c in hexip) == False:
		print(f"\002** Error:\002 Your hex contains invalid characters.")
		return hexchat.EAT_ALL

	if len(hexip) != 8:
		print(f"The hex you have specified is too long or too short to be an hexadecimal ip.")
		return hexchat.EAT_ALL

	normalip = ".".join(["%d"%int(n, 16) for n in (hexip[0:2],hexip[2:4],hexip[4:6],hexip[6:8])])
	print(f"\002**\002 Hexadecimal IP '\002{hexip}\002' resolves to '\002{normalip}\002'")
	return hexchat.EAT_HEXCHAT	

hexchat.hook_command('hex2ip', command_hex2ip, help=help['hex2ip'])


def command_dec2ip(command, command_eol, params):
	try:
		decip = command_eol[1]
	except IndexError:
		print(f"\002** Syntax:\002 /{command[0]} [decimal ip]")
		return hexchat.EAT_ALL

	if len(decip) > 10 or int(decip) > 4294967295 or int(decip) < 0:
		print(f"\002** Error:\002 {decip} is not a valid decimal ip.")
		return hexchat.EAT_ALL

	normalip = socket.inet_ntoa(struct.pack('!L', int(decip)));
	print(f"\002**\002 Decimal IP '\002{decip}\002' resolves to '\002{normalip}\002'")
	return hexchat.EAT_HEXCHAT	

hexchat.hook_command('dec2ip', command_dec2ip, help=help['dec2ip'])


def command_ip2hex(command, command_eol, params):
	try:
		ip_address = command_eol[1]
	except IndexError:
		print(f"\002** Syntax:\002 /{command[0]} [hexadecimal ip]")
		return hexchat.EAT_ALL

	try:
		socket.inet_aton(normalip)
	except socket.error:
		print(f"\002**\002 {ip_address} is not a valid IPv4 address")
		return hexchat.EAT_ALL

	hexip = ""
	for octet in ip_address.split("."):     
		hexip = "%s%02X" % (hexip, int(octet))

	print(f"\002**\002 IP '\002{ip_address}\002' resolves to hexadecimal IP '\002{hexip}\002'")
	return hexchat.EAT_HEXCHAT	

hexchat.hook_command('ip2hex', command_ip2hex, help=help['ip2hex'])


def command_ip2dec(command, command_eol, params):
	try:
		ip_address = command_eol[1]
	except IndexError:
		print(f"\002** Syntax:\002 /{command[0]} [hexadecimal ip]")
		return hexchat.EAT_ALL

	try:
		socket.inet_aton(normalip)
	except socket.error:
		print(f"\002**\002 {ip_address} is not a valid IPv4 address")
		return hexchat.EAT_ALL

	packedip = socket.inet_aton(normalip)
	decip = struct.unpack("!L", packedip)[0]

	print(f"\002**\002 IP '\002{ip_address}\002' resolves to decimal IP '\002{decip}\002'")
	return hexchat.EAT_HEXCHAT	

hexchat.hook_command('ip2dec', command_ip2dec, help=help['ip2dec'])



#### Hooks & Callbacks ####


def hook_invite(channel, channel_eol, params):
	hexchat.command(f"JOIN {channel[0]}")
	return hexchat.EAT_NONE

if join_on_invite == True:
	hexchat.hook_print( "Invited", hook_invite)


def hook_opendialogue(window, window_eol, params):
	hexchat.command(f"whois {hexchat.get_info('channel')}");
	return hexchat.EAT_NONE;

if whois_on_private == True:
	hexchat.hook_print( "Open Dialog", hook_opendialogue)


def hook_ctcp(ctcp, ctcp_eol, params):
	if ctcp[0].upper() == "OS":
		try:
			system = platform.linux_distribution()
			hexchat.command(f"nctcp {ctcp[1]} OS Operating System: {system[0]} {system[1]}") 
		except IndexError:
			hexchat.command(f"nctcp {ctcp[1]} OS Operating System: Unknown")
		except Exception:
			hexchat.command(f"nctcp {ctcp[1]} OS Operating System: Unknown") 		
	elif ctcp[0].upper() == "DATE":
		today = datetime.now()
		hexchat.command(f"nctcp {ctcp[1]} DATE {today.strftime('%d/%m/%Y')}")
	elif ctcp[0].upper() == "TIME": 
		today = datetime.now()
		hexchat.command(f"nctcp {ctcp[1]} TIME {today.strftime('%H:%M:%S')}")
	elif ctcp[0].upper() == "VERSION":
		hexchat.command(f"nctcp {ctcp[1]} VERSION XChat (Powered by {__module_name__} v{__module_version__})");
	elif ctcp[0].upper() in custom_ctcp_replies:
		hexchat.command(f"nctcp {ctcp[1]} {ctcp[0].upper()} {custom_ctcp_replies[ctcp[0].upper()]}");
    
	return hexchat.EAT_ALL;

if custom_ctcps == True:
	hexchat.hook_print( "CTCP Generic", hook_ctcp)


def hook_wallops(message, message_eol, params):
	hexchat.command(f"QUERY -nofocus \"{wallops_window}\"")
	context = hexchat.find_context(server=hexchat.get_info('server'), channel=wallops_window)
	context.emit_print("Receive Wallops", message_eol[0])
	return EAT_ALL

if wallops_seperate == True:
	hexchat.hook_print( "Receive Wallops", hook_wallops)


def hook_disconnect(message, message_eol, params):
    network = hexchat.get_info('network')

    for chan in hexchat.get_list('channels'):
            if chan.network == network and chan.type == 2:
                    chan.context.command('timer 1 close')

if close_on_disconnect == True:
	hexchat.hook_print('Disconnected', hook_disconnect)


def hook_sasl_response(word, word_eol, userdata):
	if word[1] == '904':
		if len(require_sasl_networks) == 0:
			print(f"\002** \002SASL authentication has failed for {hexchat.get_info('network')} and require_sasl is configured for all networks. Disconnecting...")
			hexchat.command('timer .1 discon')			
		if hexchat.get_info('network') in require_sasl_networks:
			print(f"\002** \002SASL authentication has failed for {hexchat.get_info('network')} and require_sasl is configured for this network. Disconnecting...")
			hexchat.command('timer .1 discon')

if require_sasl == True:
	hexchat.hook_print('SASL Response', hook_sasl_response)


def hook_unload(userdata):
	hexchat.command(f"echo \002**\002 {__module_name__} v{__module_version__} Unloaded")

hexchat.hook_unload(hook_unload)

#### General Functions ####

def slap(nickname):
  verbs = ("slaps", "hits", "beats up", "bashes", "hurts", "kills", "tortures", "rapes", "shoots")
  types = ("a large", "an enormous", "a small", "a medium sized", "an extra large", "a questionable", "a suspicious", "a terrifying", "a scary", "a breath taking", "a horrifying", "a delinquent", "an enormous", "the worlds smallest", "the biggest", "the best", "the worst");
  items = ("Windows XP Disc", "brick", "axe", "hammer", "shovel", "Windows 95", "fish", "salmon", "Khaled Mardam-Bey", "iron bar", "Back Street Boys CD", "whip", "IRCNET server", "Pentium 4 CPU", "set of Windows 3.11 floppies", "camel", "christmas tree", "laptop", "picture of Bill Nyne", "Donald Trump", "Israeli flag", "burger", "used condom");

  sentence = f"{verbs[random.randrange(len(verbs))]} {nickname} with {types[random.randrange(len(types))]} {items[random.randrange(len(items))]}"
  return sentence

def get_user(nick):
	for user in hexchat.get_list('users'):
		if user.nick == nick:
			return user

#### End of Plugin ####
