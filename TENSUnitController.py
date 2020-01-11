import socket
import RPi.GPIO as GPIO
import time

HOST = "irc.twitch.tv"
PORT = 6667
NICK = "tens7000"
PASS = 'oauth:od0og7k7tycso4lon84tgnp3ukzdir'
CHAN = "#grahamrl"

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM) # GPION Numbers instead of board numbers.
GPIO.setup(23, GPIO.OUT) # GPIO Set Output Mode
GPIO.output(23, GPIO.LOW) # LOW PIN AKA CANCEL SHOCK

def send_message(message):
    s.send(bytes("PRIVMSG #" + NICK + " :" + message + "\r\n", "UTF-8"))

s = socket.socket()
s.connect((HOST, PORT))
s.send(bytes("PASS " + PASS + "\r\n", "UTF-8"))
s.send(bytes("NICK " + NICK + "\r\n", "UTF-8"))
s.send(bytes("JOIN #" + NICK + " \r\n", "UTF-8"))
s.send("JOIN {}\r\n".format(CHAN).encode("utf-8"))


while True:
    line = str(s.recv(1024))
    if "End of /NAMES list" in line:
        break

while True:
    s.send(bytes())
    for line in str(s.recv(1024)).split('\\r\\n'):
        parts = line.split(':')
        if len(parts) < 3:
            continue

        if "QUIT" not in parts[1] and "JOIN" not in parts[1] and "PART" not in parts[1]:
            message = parts[2][:len(parts[2])]

        usernamesplit = parts[1].split("!")
        username = usernamesplit[0]

        print(username + ": " + message)
        if "SHOCK" in message.upper() and username == "tens7000":
            send_message("Message recieved " + username + "\r\n")
            print('you sadistic fuck')
            GPIO.output(23, GPIO.HIGH) # HIGH PIN AKA Shock Pin
            time.sleep(1)
            GPIO.output(23, GPIO.LOW) # LOW PIN AKA CANCEL SHOCK
            
             