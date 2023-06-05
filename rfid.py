#!/usr/bin/env python

import RPi.GPIO as GPIO
from mfrc522 import SimpleMFRC522
import requests

reader = SimpleMFRC522()

def send_rfid_id(rfid_id):
    # Replace the URL and payload with your actual web application details
    url = "http://test.liam-reinhard.com/vms/webclock/clocking"
    payload = {"type": "clockin", "idno": rfid_id}

    try:
        response = requests.post(url, json=payload)
        if response.status_code == 200:
            print("RFID ID sent successfully")
        else:
            print("Error sending RFID ID:", response.status_code)
    except requests.exceptions.RequestException as e:
        print("Error sending RFID ID:", str(e))

try:
    id, text = reader.read()
    print(id)
    #print(text)

    # Send the RFID ID to your web application
    send_rfid_id(id)

finally:
    GPIO.cleanup()
