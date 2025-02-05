import requests
import os
import pyautogui as pag
import time
import pyperclip

# Load API Key from file or ask for input
def load_api_key(file_path="api_key.txt"):
    """ Loads API key from the given file. If not found, prompts the user. """
    if os.path.exists(file_path):
        with open(file_path, "r") as file:
            return file.readline().strip()
    else:
        print("Error: api_key.txt not found. Please create the file and add your API key.")
        api_key = input("Enter your API Key: ")
        return api_key


API_KEY = load_api_key()

if not API_KEY:
    print("Error: No valid API key found. Exiting...")
    exit(1)

# API Endpoint
URL = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-1.5-flash:generateContent?key={API_KEY}"

headers = {
    "Content-Type": "application/json"
}

def get_gemini_reply(user_input):
    """ Sends a request to Gemini AI and returns the response. """
    data = {
        "contents": [
            {
                "parts": [{"text": user_input}]
            }
        ]
    }

    try:
        response = requests.post(URL, json=data, headers=headers)
        response.raise_for_status()  # Will raise HTTPError for bad responses (4xx or 5xx)
        
        response_json = response.json()
        if "candidates" in response_json and response_json["candidates"]:
            return response_json["candidates"][0]["content"]["parts"][0]["text"]
        else:
            return "I'm sorry, but I didn't get a response."
    
    except requests.exceptions.RequestException as e:
        return f"Error: {str(e)}"

# ---------------------------------------------------------------------------------------------------------------------------------------
def perform_gui_actions():
    """ Handles GUI interactions like clicking, dragging, and copying messages. """
    pag.click(1178, 1053)  # click at 1182, 1057
    time.sleep(10)          # wait for 10 seconds to load the app
    pag.click(370, 603)
    time.sleep(1)

    # Dragging operation
    pag.moveTo(908, 338)                                      # start
    pag.dragTo(924, 940, duration=1.0, button='left')          # end

    # Copying Messages 
    pag.hotkey('ctrl', 'c')
    time.sleep(1)

    # Deselect
    pag.click(908, 338)

def main():
    """ Main function to interact with the bot and process messages. """
    # Perform initial GUI actions
    perform_gui_actions()

    # Paste copied text
    paste_text = pyperclip.paste()
    print("\n🤖 Auto-Reply Bot: Type 'exit' to stop the chat.")

    i = 0
    while True:
        # Determine the user message
        if i == 0:
            user_message = f"""You are Arpan, a friendly and intelligent person from India who speaks both Hindi and English fluently. 
    You love coding and enjoy engaging in conversations in a natural way. You will continue this conversation in a human-like manner, 
    responding based on the provided chat history and maintaining the tone and style of Arpan. Your responses should be natural, 
    engaging, and concise (2-4 sentences). Here is the chat history so far:
    
    {paste_text}
    
    Now, based on this conversation, reply as Arpan would, making sure to sound human and keeping the flow natural."""
            i += 1
        else:
            user_message = input("You: ")

        if user_message.lower() == "exit":
            print("\nBot: Goodbye! 👋")
            break

        bot_reply = get_gemini_reply(user_message)
        print(f"\nBot: {bot_reply}")

if __name__ == "__main__":
    main()
