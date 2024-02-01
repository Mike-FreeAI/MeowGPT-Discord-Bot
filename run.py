from SplitticAPI.meowgpt import ChatModule

# Set the global API key
api_key = "sk-a374c38c9d72cc7490868521648d6ac47762b629501574cca0c7f9c803bcfd68"
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
