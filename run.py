from SplitticAPI.meowgpt import ChatModule
import config

# Set the global API key
api_key = config.api_key
ChatModule.initialize(api_key)

# Create a ChatModule instance with a unique chat ID
chat_instance = ChatModule.create_chat(api_key)

# Send a synchronous message and get a reply
def main():
    while True:
        reply = chat_instance.reply(input("> "))
        print(reply)

# Run the program
if __name__ == "__main__":
    main()

