# Russell's Awesome Hexchat Plugin
 *Just a hexchat plugin with a variety of features...*

### Installation
* Download or clone [this repository](https://github.com/RussellB28/hexchat-plugin) into your hexchat plugins directory 
* Unzip master.zip *(if you have downloaded, using unzip master.zip)*
* Run ```pip3 install -r requirements.txt```
* Open ```russell.py``` and make changes to the configuration section if required
* Load the plugin using ```/load russell.py``` or hexchats graphical interface

### Configuration ###
This plugin comes with a few configuration options. Note that these configuration options are in the plugin itself therefore if any changes are made, you will need to reload the plugin using ```/reload russell.py``` or using hexchats graphical interface.

##### General Configuration #####
General configuration options are as follows:
| Configuration Option | Values | Description|
| ------ | ------ | ------ |
| close_on_disconnect | True/False | If True, closes channel windows when you disconnect or are disconnected from networks.
| custom_ctcps | True/False | If True, custom CTCP's will be used. See the CTCP Replies section below for further info.
|drunk_config | String | This is the configuration file name that will be used for ```/drunk``` and ```/drink``` commands. The configuration file when created will appear in same directory as other hexchat configuration files. By default it is set to 'drunk.conf'
|drunk_custom_date | Date String (DD/MM/YY) | The date that will be displayed on the 'Drinks Since' section of the ```/drunk``` command. If this is not set or not a valid date, it will default to using the date that the file configured in ```drunk_config``` was created.
| join_on_invite | True/False | If True, you will automatically join channels if you are invited to them.
| require_sasl | True/False | If True, SASL will be required and networks will be disconnected if SASL authentication fails. See the SASL Networks section below for further info.
| wallops_seperate | True/False | If True, wallops will be sent to a seperate window. The window name can be configured using ```wallops_window``` configuration setting
| wallops_window | String | This setting controls the name of the wallops window when ```wallops_seperate``` is enabled. By default it is set to '(wallops)''
| whois_on_private | True/False | If True, hexchat will automatically ```/whois``` any user that sends you a private message.

##### CTCP Replies #####
If ```custom_ctcps``` is set to True, Custom CTCP replies will be used rather than hexchat's own replies. Custom replies can be configured using ```custom_ctcp_replies```. For example, If you wanted to add a custom reply to CTCP FINGER, you would configure ```custom_ctcp_replies``` as follows:
```
custom_ctcp_replies = {
			'FINGER': "127.0.0.1"
}
```
You can also configure other CTCP replies to be customised. Configuration for multiple customisations would look something like this:
```
custom_ctcp_replies = {
			'FINGER': "127.0.0.1",
			'EMAIL': "my.email@example.com",
			'MYREPLY', "My custom ctcp reply"
}
```
##### LastFM #####
The ``/np`` (Now Playing) command relies on LastFM to retrieve data. You will need to obtain API keys from https://www.last.fm/api and configure these within the plugin. The configuration should look as follows:
```
lastfm = {
			'api_url': 'http://ws.audioscrobbler.com/2.0/',
			'api_key': 'Your API Key',
			'username': 'Your Last FM Username'
}
```
##### SASL Networks #####
if ```require_sasl``` is set to True, Networks will be configured to require SASL which means they will disconnect if SASL authentication is unsuccessful. To enable this for specific networks, ```require_sasl_networks``` needs to be configured. For example, if we only want to require SASL on Freenode, you would configure ```require_sasl_networks``` as follows:
```
require_sasl_networks = (
			'Freenode'
)
```
You can also configure multiple networks to require SASL. Configuration for multiple networks would look something like this:
```
require_sasl_networks = (
			'Freenode',
			'Rizon',
			'SomeOtherNetwork'
)
```
You can also configure SASL to be required on all networks. To do this, simply leave ```require_sasl_networks``` empty as follows:
```
require_sasl_networks = (
)
```
##### Twitter #####
The ```/twitter``` (Tweet) command relies on Twitter's API to be able to post tweets. You will need to obtain API keys from https://developer.twitter.com/ and configure these within the plugin. The configuration should look as follows:
```
twitter = {
			'consumer_key': 'My Applications Consume Key',
			'consumer_secret': 'My Applications Consume Secret',
			'access_token': 'My Applications Access Token',
			'access_secret': 'My Applications Access Secret'
}
```
### Bugs/Feature suggestions ###
If you've found a bug or have any suggestions on how this plugin could be improved, throw us a line [here](https://github.com/RussellB28/hexchat-plugin/issues) and we'll take a look.
