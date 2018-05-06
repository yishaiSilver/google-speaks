import time
import pychromecast
import gtts
import urllib3

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

standardSentence = "Hello world!"
tts_init = gtts.gTTS(text=standardSentence, slow=False)

def cast_sentence(sentence):
    # Find your device.
    chromecasts = pychromecast.get_chromecasts()
    [cc.device.friendly_name for cc in chromecasts]
    cast = next(cc for cc in chromecasts if cc.device.friendly_name == "YOUR_DEVICE'S_NAME_HERE")

    cast.wait()

    # Translate text to audio and save it to available directory
    tts = gtts.gTTS(text=sentence, slow=False)
    tts.save("/var/www/html/audio_output.mp3")

    mc = cast.media_controller
    mc.play_media('http://192.168.0.39/audio_output.mp3', 'audio/mp3') # Change 192.168.0.39 to your RPi's IP address
    mc.block_until_active()
    print(mc.status)

    mc.play()
