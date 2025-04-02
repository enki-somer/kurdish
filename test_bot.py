import requests
import json

def send_message(message, sender="test_user"):
    url = "http://localhost:5005/webhooks/rest/webhook"
    payload = {
        "sender": sender,
        "message": message
    }
    headers = {
        "Content-Type": "application/json"
    }
    response = requests.post(url, data=json.dumps(payload), headers=headers)
    return response.json()

def main():
    print("Starting conversation with the Kurdish Chatbot...")
    
    # Greet the bot
    print("\nUser: سڵاو")
    responses = send_message("سڵاو")
    for response in responses:
        print(f"Bot: {response['text']}")
    
    # Provide name
    print("\nUser: ناوم ئاریە")
    responses = send_message("ناوم ئاریە")
    for response in responses:
        print(f"Bot: {response['text']}")
    
    # Provide phone number
    print("\nUser: ٠٧٥٠١٢٣٤٥٦٧")
    responses = send_message("٠٧٥٠١٢٣٤٥٦٧")
    for response in responses:
        print(f"Bot: {response['text']}")
    
    # Provide address
    print("\nUser: سلێمانی، گەڕەکی ڕزگاری")
    responses = send_message("سلێمانی، گەڕەکی ڕزگاری")
    for response in responses:
        print(f"Bot: {response['text']}")
    
    # Thank the bot
    print("\nUser: زۆر سوپاس")
    responses = send_message("زۆر سوپاس")
    for response in responses:
        print(f"Bot: {response['text']}")
    
    # Say goodbye
    print("\nUser: خوا حافیز")
    responses = send_message("خوا حافیز")
    for response in responses:
        print(f"Bot: {response['text']}")

if __name__ == "__main__":
    main() 