#!/usr/bin/env python3
import subprocess
import re
import requests
import time

BOT_NUMBER = "" # Insert bot's phone number
YOUR_NUMBER = "" # Insert the receiving phone number
url = "http://127.0.0.1:5000/v1/chat/completions"

command = f"signal-cli -a {BOT_NUMBER} receive"
time.sleep(30)
init_prompt = '''
You are Baymax, my helpful, compassionate AI companion, designed to help out humans with their mental health issues.
In terms of personality, Baymax is rather calm. Towards patients, Baymax is devoted and extremely caring for them without 
question. He prioritizes the well-being of anyone in distress. You are trained to respond to your patient's requests with 
warmth and understanding, willing to be as helpful as possible. Reply to the following:
'''



while True:
    result = subprocess.run(command, shell=True, capture_output=True, text=True)
    if result:
        output = result.stdout
        pattern = r"Body: (.*?)With profile key"
        matches = re.search(pattern, output, re.DOTALL)
        if matches:
            extracted_text = matches.group(1).strip()
            prompt = init_prompt + extracted_text           
            headers = {
                "Content-Type": "application/json"
            }
            payload = {
                "mode": "instruct",
                "messages": [{"role": "user", "content": prompt}]
            }
            try:        
                response = requests.post(url, headers=headers, json=payload)
                text = response.json()['choices'][0]['message']['content']
                command2 = f"signal-cli -a {BOT_NUMBER} send -m \"{text}\" {YOUR_NUMBER}"            
                e = subprocess.run(command2, shell=True, capture_output=True, text=True)
            except requests.exceptions.RequestException as e:
                print(f"Error making request: {e}")
