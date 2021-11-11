# TENS7000TwitchController
#### Summary
A Raspberry Pi controlled Twitch IRC bot that also controls a TENS unit (transcutaneous electrical nerve stimulator). You should probably think twice before using this and honestly just don't. It's a really stupid project. Use at your own risk. 

#### Background
I spliced the electrode wires from a TENS unit together with a relay hooked up to a Raspberry Pi. From there, I could programmatically control when the relay opened to allow the electricity from the TENS unit to travel freely through the electrodes. I ended up taking it a step further and setting up a Streamlabs bot on a Twitch channel to send a trigger message in chat whenever a viewer interacted with the stream. The TENSUnitController.py script would then be listening on the Twitch channel's IRC and would open the relay for 'n' seconds before returning it to it's closed state.


#### Project Overview
GPIO_Test.py is a test script meant to confirm the circuit is connected and functioning properly. If everything is set up properly, the 'G' key should activate GPIO 23, sending a shock through the TENS unit for 1 second.

GPIO_Test_Shock30Sec.py is a script meant to activate GPIO 23 for 1 second every 30 seconds.

TENSUnitController.py is a Twitch IRC bot that listens to the chat looking for a trigger phrase from a specific user. When triggered, the script will activate GPIO 23 for 1 second and then sleep until the next trigger phrase is given.
