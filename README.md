# ESP8266-Connected-MP3-Player
Browser controlled MP3 Player built using the ESP8266 and CATALEX MP3 Player based on YX5300 chip. This implementation uses the MicroPython Firmware for the ESP8266 modules. http://docs.micropython.org/en/latest/esp8266/index.html

Example implementation of network connected MP3 player based on the ESP8266 WiFi module and the CATALEX Serial controlled MP3 Player. The MP3 player is controlled using a proprietary serial protocol. The file YX5300.py implements the protocol definition defined in the Serial MP3 Player v1.0 Manual. 

The MP3 module has a 4 pin connector. VC +, VC -, RX, TX. Power can be drawn from the ESP8266 ground and +5v pin. for serial communication cross the RX to TX between the two modules. 

Check out this YouTube video for see how it works. https://www.youtube.com/watch?v=linWEj72V1Y

Links to modules

ESP8266, I am using the WeMos implementation. (anyone running micropython should work)

https://www.ebay.com/itm/392276865235

CATALEX MP3 player. 

https://www.ebay.com/itm/391707147944
