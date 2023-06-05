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

def send_rfid_id_2(rfid_id):
    # Replace the URL and payload with your actual web application details
    url = "http://test.liam-reinhard.com/vms/webclock/clocking"
    payload = {"type": "clockout", "idno": rfid_id}

    try:
        response = requests.post(url, json=payload)
        if response.status_code == 200:
            print("RFID ID sent successfully")
        else:
            print("Error sending RFID ID:", response.status_code)
    except requests.exceptions.RequestException as e:
        print("Error sending RFID ID:", str(e))


try:
    id = 321312 #The ID that gets passed in the POST request. Change accordingly

    # Send the RFID ID to your web application
    send_rfid_id(id)
    send_rfid_id_2(id)

finally:
    GPIO.cleanup()
