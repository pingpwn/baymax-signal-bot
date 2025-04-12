# Baymax Signal Bot
![baymax](baymax.png "Baymax")
### What is this?

This very simple python script connects an online or local LLM (using the OpenAI-style API) with [signal-cli](https://github.com/AsamK/signal-cli) to host a Signal bot that imitates the character Baymax from Disney's [Big Hero 6](https://en.wikipedia.org/wiki/Big_Hero_6_(film)). 

### Why?
I wanted to learn how to make a bot on signal, I also like the movie and the friendly vibes the character gives to AI. That's basically it.

### Set it up
+ First you need to set up [signal-cli](https://github.com/AsamK/signal-cli), you will need an extra phone number for this.
+ Set up your LLM. You can use I am using The Bloke's [CapyBaraHermes 2.5 Mistral 7B - GPTQ](https://huggingface.co/TheBloke/CapybaraHermes-2.5-Mistral-7B-GPTQ) which I host locally using [Text Generation WebUI ](https://github.com/oobabooga/text-generation-webui). One cool idea would be to use LLMs specifically fine-tuned for [mental health](https://huggingface.co/klyang/MentaLLaMA-chat-7B).
+ Inside bot.py, change the number placeholders to your number and the bot's number. 
+ Run bot.py. Test it out by adding the bot on Signal and sending a prompt.

### To-do
+ Implement prompt history
+ Add the ability to chat with multiple numbers
### Warnings
 + The Baymax character as well as the entirety of the Big Hero 6 **are trademarks of Disney** (please don't sue me).
 + This script has NOT BEEN CHECKED TO BE SECURE (run at your own risk).
