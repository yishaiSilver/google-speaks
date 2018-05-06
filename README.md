# googleSpeaks
This is a simple python module that I made for casting sentences to google home from a Raspberry Pi. It gets around pychromecast's inability to cast local files, and, when paired with other services, it allows google home to offer me information without me having to ask for said information. Likewise, it also allows me to ask for information beyond that which the Google Assistant and IFTTT allow for (that is to say, of course, a premade response), such as the connection status of my devices. Also, this is a bit of a throw-together; if you feel you can improve it let me know.

## Prerequisites
Install pychromecast, gtts, and urllib3 with the following commands:
```
sudo pip install pychromecast
sudo pip install gtts
sudo pip install urllib3
```
You'll also need to run an apache server. Install apache2 with:
```
sudo apt-get install apache2 apache2-utils
```

## Setup
Change YOUR_DEVICE'S_NAME_HERE to your device's name. Also change 192.168.0.39 to your RPi's (hopefully static) IP address.

## Usage

Import it and call upon the cast_sentence method. Example:
```python
import googleSpeaks
googleSpeaks.cast_sentence('Hello World!')
```

## Built With
+ [pychromecast](www.google.com) - What is used to actually cast the audio file.
+ [gTTS](www.google.com) -  Google Translate-based TTS Engine
+ [apache2](www.google.com) - What makes the audio file available for casting.

## License
I don't care.
