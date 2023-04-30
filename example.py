from POE import load_chat_id_map, clear_context, send_message, get_latest_message, set_auth

#Auth
set_auth('Quora-Formkey','xxxx')
set_auth('Cookie','m-b=xxxxx')
#---------------------------------------------------------------------------
print("Who do you want to talk to?")
print("1. Sage - OpenAI (capybara)")
print("2. GPT-4 - OpenAI (beaver)")
print("3. Claude+ - Anthropic (a2_2)")
print("4. Claude - Anthropic (a2)")
print("5. ChatGPT - OpenAI (chinchilla)")
print("6. Dragonfly - OpenAI (nutria)")
print("7. Neeva - NeevaAI (hutia)")
#---------------------------------------------------------------------------
option = input("Please enter your choice : ")
bots = {1:'capybara', 2:'beaver', 3:'a2_2', 4:'a2', 5:'chinchilla', 6:'nutria', 7:'hutia'}
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
