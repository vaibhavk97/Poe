# Quora Poe reverse-engineered API
This is a reverse-engineered API for Quora's Poe that allows access to the following chatbots:

1. Sage - OpenAI (capybara)
2. GPT-4 - OpenAI (beaver)
3. Claude+ - Anthropic (a2_2)
4. Claude - Anthropic (a2)
5. ChatGPT - OpenAI (chinchilla)
6. Dragonfly - OpenAI (nutria)
### Requirements
To use this API, you will need to have the following cookies:

2. Quora-Formkey: This is obtained by logging in to Quora.com, viewing the page source, and finding the "formkey" dictionary key. Use its value in the Quora-Formkey field.
3. Cookie: 'm-b=xxxx' - This is the value of the cookie with the key m-b, which is present in the list of cookies used on Quora.com, you can simply inspect cookies in Chrome to get it.

### Example
You can find an example of how to use this API in the example.py file.

### Disclaimer
This repository is for educational and research purposes only, and the use of this API for any other purpose is at your own risk. We are not responsible for any actions taken by users of this API.

#### Requirements: 
requests. 
