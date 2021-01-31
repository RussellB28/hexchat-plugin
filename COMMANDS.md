# Russell's Awesome Hexchat Plugin Commands
Below is a list of commands and their description/syntax that are implemented by this plugin. 
You can use ```/help [command]``` for further info on any of these commands.

### General Commands ###
##### Ban Hammer  ```/bh``` #####
###### Description: ######
Gets out a ban hammer for a given nickname and shows the message as an action in the current channel.
###### Syntax: ######
```/bh [nickname]```
###### Sample Output: ######
```
* MyNickname is getting out the ban hammer for italians! ▬▬▬▬▬▬▬▋ Ò╭╮Ó
```

##### Bass  ```/bass``` #####
###### Description: ######
Tells the current channel to turn up the music with some ascii art.
###### Syntax: ######
```/bass```
###### Sample Output: ######
```
<MyNickname> ╔══╗ ♫  ＴＵＲＮ ＵＰ ＴＨＥ
<MyNickname> ║██║ ♪♪ ╔══════╦═╗╔═╦═══╦═╦═══╗
<MyNickname> ║██║♫♪  ║░╔╗╔╗░║░║║░║╚══╣░║░╔═╝
<MyNickname> ║ ◎♫♪♫  ║░║╚╝║░║░╚╝░╠══╗║░║░╚═╗
<MyNickname> ╚══╝    ╚═╝░░╚═╩════╩═══╩═╩═══╝
```

##### My IRC Statistics  ```/brag``` #####
###### Description: ######
Tells the current channel how many channels you're in, networks you're on, what status you have on those channels, how many private messages you have open and how much power and influence you have over channel uses.
###### Syntax: ######
```/brag```
###### Sample Output: ######
```
<MyNickname> [STATS] I am in 111 channels and private messaging 6 people across 13 networks. (Owner: 10, Protected: 8, Op'd: 62, Halfop'd: 0, Voiced: 15)
<MyNickname> [STATS] I currently have non-abusive power and mind-blowing influence over 1088 people
```

##### Chat Protect  ```/chatprotect``` #####
###### Description: ######
Displays a random chat protection message to the current channel.
###### Syntax: ######
```/chatprotect```
###### Sample Output: ######
```
<MyNickname> Tᴏ ᴘʀᴏᴛᴇᴄᴛ ᴛʜᴇ ᴄʜᴀᴛ ғʀᴏᴍ ᴅᴇᴠᴀsᴛᴀᴛɪᴏɴ. ᴛᴏ ᴜɴɪᴛᴇ ᴀʟʟ sᴘᴀᴍᴍᴇʀs ᴡɪᴛʜɪɴ ᴏᴜʀ ɴᴀᴛɪᴏɴ. ᴛᴏ ᴅᴇɴᴏᴜɴᴄᴇ ᴛʜᴇ ᴇᴠɪʟ ᴏғ Tʀᴜᴍᴘ ᴀɴᴅ ᴍᴏᴅs. ᴛᴏ ᴇxᴛᴇɴᴅ ᴏᴜʀ sᴘᴀᴍ ᴛᴏ ᴛʜᴇ sᴛᴀʀs ᴀʙᴏᴠᴇ. ᴄᴏᴘʏ! ᴘᴀsᴛᴇ! ᴄʜᴀᴛ!
```

##### Dieeeee  ```/dieman``` #####
###### Description: ######
Displays an ascii art of a man being shot by another ascii man to the current channel
###### Syntax: ######
```/dieman```
###### Sample Output: ######
```
<MyNickname> < DIEEEEEEEEEEEE > 
<MyNickname>                  \ 
<MyNickname>                   \ 
<MyNickname>    \o/             o 
<MyNickname>     █      - - ─╤╦.█\ 
<MyNickname>    .Π.            .Π. 
```

##### Drink!  ```/drink``` #####
###### Description: ######
Updates the last date that you had a drink and the count of how many drinks you've had since a given date and echo's to the current window that the command has been successful.
*See the configuration section of the readme for info on how to configure this command*
###### Syntax: ######
```/drink```
###### Sample Output: ######
```
** Drink Consumed!
```

##### Drunk?  ```/drunk``` #####
###### Description: ######
Displays the last time you had a drink and the number of drinks you have had since a given date to the current channel.
*See the configuration section of the readme for info on how to configure this command*
###### Syntax: ######
```/drink```
###### Sample Output: ######
```
<MyNickname> Last Drink Consumed: 1 days ago (26 drinks since 01/01/2021)
```

##### Flip Text  ```/flip``` #####
###### Description: ######
Flip a given message upside down.
###### Syntax: ######
```/flip [message]```
###### Sample Output: ######
```
<MyNickname> ǝƃɐssǝɯ ɐ sı sıɥʇ
```

##### Current Lag  ```/lag``` #####
###### Description: ######
Displays the current lag in seconds to the current channel. Lag is calculated on a per channel basis using the Send and Recieve Queues.
###### Syntax: ######
```/lag```
###### Sample Output: ######
```
<MyNickname> My Current Lag: 0.116 seconds
```

##### Stick Man  ```/man``` #####
###### Description: ######
Displays an ascii stick man to the current channel.
###### Syntax: ######
```/man```
###### Sample Output: ######
```
<MyNickname> \o/ 
<MyNickname>  |  
<MyNickname> / \ 
```

##### Huge Melon  ```melon``` #####
###### Description: ######
Displays a giant sized melon in the current channel using color codes.
###### Syntax: ######
```/melon```
###### Sample Output: ######
```
None Available
```

##### Music ```/music``` #####
###### Description: ######
Displays the word 'Music' in ascii
###### Syntax: ######
```/music```
###### Sample Output: ######
```
<MyNickname> ╔══════╦═╗╔═╦═══╦═╦═══╗
<MyNickname> ║░╔╗╔╗░║░║║░║╚══╣░║░╔═╝
<MyNickname> ║░║╚╝║░║░╚╝░╠══╗║░║░╚═╗ 
<MyNickname> ╚═╝░░╚═╩════╩═══╩═╩═══╝
```

##### Rainbow ```/rainbow``` #####
###### Description: ######
Displays a given message in random rainbow colors
###### Syntax: ######
```/rainbow [message]```
###### Sample Output: ######
```
None Available
```

##### URL Shorten ```/short``` #####
###### Description: ######
Shortens a given long URL using https://f0rk.in/ and displays the short url to the channel.
###### Syntax: ######
```/short [URL]```
###### Sample Output: ######
```
<MyNickname> https://f0rk.in/a
```

##### Slap ```/slap``` #####
###### Description: ######
Slaps a given nickname with a completely random item.
###### Syntax: ######
```/slap [nickname]```
###### Sample Output: ######
```
* MyNickname bashes OtherNickname with a terrifying Pentium 4 CPU
```

##### Soap ```/soap``` #####
###### Description: ######
Displays an ascii bar of soap to the current channel.
###### Syntax: ######
```/soap```
###### Sample Output: ######
```
<MyNickname>  ╭━━━━╮
<MyNickname>  ┃╭╮╭╮┃
<MyNickname> ┗┫┏━━┓┣┛
<MyNickname>  ┃╰━━╯┃
<MyNickname>  ╰┳━━┳╯
```
### Converters ###
##### Number to Binary ```/bin``` #####
###### Description: ######
Converts a given number into binary and prints the result in the current window.
###### Syntax: ######
```/bin [Number]```
###### Sample Output: ######
```
 ** 33 as a binary is 100001
```

##### IPv4 Decimal to IPv4 IP ```/dec2ip``` #####
###### Description: ######
Converts a given IPv4 decimal to an actual IPv4 address and prints the result in the current window.
###### Syntax: ######
```/dec2ip [IPv4 Decimal]```
###### Sample Output: ######
```
 ** Decimal IP '1337133701' resolves to '79.179.10.133'
```

##### String to Hash ```/hashed``` #####
###### Description: ######
Hashes a given message against a given algorithm and prints the results in the current window. Using this command with no parameters shows a list of available hash types on your system.
###### Syntax: ######
```/hashed [algorithm] [message]```
###### Sample Output: ######
```
 ** Your sha256 Hash is: 2e99758548972a8e8822ad47fa1017ff72f06f3ff6a016851f45c398732bc50c
```

##### Number to Hexadecimal ```/hex``` #####
###### Description: ######
Converts a given number into hexadecimal and prints the result in the current window.
###### Syntax: ######
```/hex [number]```
###### Sample Output: ######
```
 ** 33 as a hexadecimal is 0x21
```

##### IPv4 Hexadecimal to IPv4 IP ```/hex2ip``` #####
###### Description: ######
Converts a given IPv4 hexadecimal to an actual IPv4 address and prints the result in the current window.
###### Syntax: ######
```/hex2ip [IPv4 Hexadecimal]```
###### Sample Output: ######
```
 ** Hexadecimal IP '0FFD671A' resolves to '15.253.103.26'
```

##### IPv4 IP to IPv4 Decimal ```/ip2dec``` #####
###### Description: ######
Converts a given IPv4 address to an IPv4 Decimal and prints the result in the current window.
###### Syntax: ######
```/ip2dec [IPv4 address]```
###### Sample Output: ######
```
 ** IP '127.0.0.1' resolves to decimal IP '2130706433'
```

##### IPv4 IP to IPv4 Hexadecimal ```/ip2hex``` #####
###### Description: ######
Converts a given IPv4 hexadecimal to an actual IPv4 address and prints the result in the current window.
###### Syntax: ######
```/ip2hex [IPv4 address]```
###### Sample Output: ######
```
 ** IP '127.0.0.1' resolves to hexadecimal IP '7F000001'
```

##### Number to Hexadecimal ```/num``` #####
###### Description: ######
Converts a given hexadecimal, octal or binary into a number
###### Syntax: ######
```/num [hexadecimal/binary/octal]```
###### Sample Output: ######
```
 ** 0x45 as a number is 69
```

##### Number to Octal ```/oct``` #####
###### Description: ######
Converts a given number into octal and prints the result in the current window.
###### Syntax: ######
```/hex [number]```
###### Sample Output: ######
```
 ** 33 as an octal is 41
```

### Other / API ###
##### Tweet ```/twitter``` #####
###### Description: ######
Post a message to your twitter account from hexchat.
*See the configuration section of the readme for info on how to configure this command*
###### Syntax: ######
```/twitter [message]```
###### Sample Output: ######
```
 ** Tweet posted successfully
```

##### Now Playing ```/np``` #####
###### Description: ######
Display the track you are currently playing or last played to the current channel using [LastFM](https://last.fm/)
*See the configuration section of the readme for info on how to configure this command*
###### Syntax: ######
```/np```
###### Sample Output: ######
```
* MyNickname is listening to Finally by CeCe Peniston [Finally]
```
