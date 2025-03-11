

## Creating an Intaractive Chatbot

import google.generativeai as ai 

#API KEY
##API_Key = "AIzaSyB0XXH9BACyNCY92DYRPV1GVG029IjVwz4"


GOOGLE_API_KEY = "AIzaSyB0XXH9BACyNCY92DYRPV1GVG029IjVwz4"
ai.configure(api_key=GOOGLE_API_KEY)

#congifuring the API
#ai.configure(api_key=API_Key)


#Creating a new model
model = ai.GenerativeModel("gemini-1.5-pro")
chat = model.start_chat()


#Starting the chat
while True:
    message = input("You: ")
    if message.lower() == "bye":
        print("Chatbot: Goodbye!")
        break
    response = chat.send_message(message)
    print("Chatbot:", response.text)

