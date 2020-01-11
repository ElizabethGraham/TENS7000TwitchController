# TENS7000TwitchController
 Raspberry Pi Twitch IRC bot that controls a TENS unit. You should probably think twice before using this and honestly just don't. It's a really stupid project. Use at your own risk.



GPIO_Test.py is a test script meant to confirm the circuit is connected and functioning properly. If everything is set up properly, the 'G' key should activate GPIO 23, sending a shock through the TENS unit for 1 second.

GPIO_Test_Shock30Sec.py is a script meant to activate GPIO 23 for 1 second every 30 seconds.

TENSUnitController.py is a Twitch IRC bot that scrubs chat looking for a trigger phrase from a specific user. When triggered, the script will activate GPIO 23 for 1 second and then sleep until the next trigger phrase is given.
