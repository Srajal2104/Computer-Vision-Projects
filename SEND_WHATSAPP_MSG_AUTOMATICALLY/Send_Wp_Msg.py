# Import pywhatkit module
# pywhatkit is a Python library used for automation tasks
# such as sending WhatsApp messages, playing YouTube videos, searching Google etc.
import pywhatkit


# sendwhatmsg() is a built-in function of pywhatkit module
# It sends a WhatsApp message automatically at a scheduled time

# Parameters of sendwhatmsg():
# "+911234567890" -> phone number of the receiver (must include country code)
# "Hi Happy Birthday..." -> message that will be sent
# 19 -> hour (24-hour format)
# 28 -> minute when the message should be sent

pywhatkit.sendwhatmsg("+911234567890","Hi Happy Birthday...",19,28)