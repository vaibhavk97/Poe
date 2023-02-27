from POE import load_chat_id_map, clear_context, send_message, get_latest_message, set_auth

#Auth
set_auth('Quora-Formkey','xxxx')
set_auth('Cookie','m-b=xxxxx')
#---------------------------------------------------------------------------
print("Who do you want to talk to?")
print("1. Claude - Anthropic (a2)")
print("2. ChatGPT-Big - OpenAI (capybara)")
print("3. ChatGPT-Small - Openai (nutria)")
#---------------------------------------------------------------------------
option = input("Please enter your choice : ")
bots = {1:'a2',2:'capybara',3:'nutria'}
bot = bots[int(option)]
print("The selected bot is : ", bot)
#---------------------------------------------------------------------------
chat_id = load_chat_id_map(bot)
clear_context(chat_id)
print("Context is now cleared")
while True:
    message = input("Human : ")
    if message =="!clear":
        clear_context(chat_id)
        print("Context is now cleared")
        continue
    if message =="!break":
        break
    send_message(message,bot,chat_id)
    reply = get_latest_message(bot)
    print(f"{bot} : {reply}")