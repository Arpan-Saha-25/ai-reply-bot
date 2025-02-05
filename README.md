# 🧠 Automated AI Chatbot using Gemini API & PyAutoGUI  

This project is a Python-based chatbot that interacts with **Gemini AI** to generate intelligent responses. It also automates GUI interactions using **PyAutoGUI**, allowing for message selection, copying, and automated replies.

## 🚀 Features
- 🌐 **Uses Google Gemini AI** for intelligent chatbot responses.  
- 🖥️ **Automates GUI interactions** using PyAutoGUI.  
- 🔑 **Secure API Key Handling** by reading from a file (`api_key.txt`).  
- 📋 **Clipboard Integration** with Pyperclip for copying and pasting text.  
- 🔁 **Human-like Conversations** mimicking a predefined personality.  

## 🛠️ Installation  

1. Clone this repository:  
   ```sh
   git clone https://github.com/Arpan-Saha-25/ai-reply-bot.git
   cd ai-reply-bot
   ```
   
2. Install dependencies:  
   ```sh
   pip install requests pyautogui pyperclip
   ```

3. Add your **API Key**:  
   - Create a file named `api_key.txt` in the project directory.  
   - Paste your Google Gemini API key inside `api_key.txt`.

4. Run the script:  
   ```sh
   python main.py
   ```

## 📌 How It Works  

1. Loads the API key from `api_key.txt`.  
2. Captures text from the GUI using **PyAutoGUI** and **Pyperclip**.  
3. Sends the extracted text to **Gemini AI** for generating responses.  
4. Displays the AI-generated response in the console.  

## 🔒 Security Considerations  
- **DO NOT hardcode your API key in the script.** Use `api_key.txt` for secure handling.  
- Avoid running the script with **admin privileges** unless necessary.  

## 👨‍💻 Author  
Developed by **Arpan Saha**.  

## 📜 License  
This project is licensed under the MIT License.  

---