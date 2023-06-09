import random
import requests
import sys
import re

def is_valid_slack_webhook_url(url):
    # Define a regular expression pattern for Slack webhook URLs
    pattern = r'^https://hooks\.slack\.com/services/.+/.+$'
    
    # Use regex to match the input string against the pattern
    match = re.match(pattern, url)
    
    # If there is a match, the input string is a valid Slack webhook URL
    if match:
        return True
    else:
        return False

# Check if an argument was provided
if len(sys.argv) > 2:
    csv_values  = sys.argv[1]
    team_members = csv_values.split(',')

    # Get the first argument
    url = sys.argv[2]

else:
    print("Not enough argument provided.")
    exit(1)

if not is_valid_slack_webhook_url(url):
    print("Invalid url entered")
    exit(1)

# Open the file for reading
with open("facts.txt", "r") as file:
    # Read all lines from the file into a list
    lines = file.readlines()
    
    # Remove leading/trailing whitespaces from each line
    lines = [line.strip() for line in lines]
    
    # Select a random line from the list
    random_line = random.choice(lines)

# Use the random.choice() function to randomly select a value from the list
random_value = random.choice(team_members)

text = "Today's daily will be facilitated by " + random_value + ". If (s)he cannot join, Jarda will facilitate.\n\nFun fact: " + random_line;

payload = {
    "text": text
}

# Send a GET request using the requests library
response = requests.post(url, json=payload)

# Check if the request was successful (status code 200 indicates success)
if response.status_code != 200:
    print("Request failed with status code:", response.status_code)
