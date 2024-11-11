# MeowGPT Discord Bot Setup Guide

## Introduction

This guide will help you set up your own MeowGPT Discord bot using the provided code. MeowGPT is a chatbot powered by the SplitticAPI.

### Prerequisites

1. **Python**: Ensure that you have Python installed on your system. If not, download it from [python.org](https://www.python.org/downloads/).

2. **Discord Bot Token**: Obtain a Discord bot token by creating a new bot on the [Discord Developer Portal](https://discord.com/developers/applications).

3. **SplitticAPI Key**: Sign up for an account on SplitticAPI and get your API key from the [FreeAI Discord server](https://discord.gg/W4bwWX3HJx).

4. **Text Prompt (Optional)**: Prepare a text prompt to initiate conversations. You can provide an empty string if you don't want to use a specific prompt.

5. **Channel IDs**: Identify the Discord channels where you want the bot to operate. Collect the Channel IDs of these channels.

6. **Free Hosting**: Visit [splittic.app](https://splittic.app) for free hosting. Follow their instructions to set up your bot hosting.

### Environment Setup

1. **Create a Virtual Environment**: It's recommended to use a virtual environment to manage dependencies. Run the following command to create one:

    ```bash
    python -m venv venv
    ```

2. **Activate the Virtual Environment**: Activate the virtual environment using the command below:

    - On Windows:

        ```bash
        .env\Scriptsctivate
        ```

    - On macOS and Linux:

        ```bash
        source venv/bin/activate
        ```

3. **Install Dependencies**: Install the required packages using the `requirements.txt` file. Run:

    ```bash
    pip install -r requirements.txt
    ```

### Configuration

1. Open the `config.py` file and update the following variables:
    - `api_key`: Replace `"YOUR_API_KEY"` with your SplitticAPI key.
    - `token`: Replace `"YOUR_DISCORD_BOT_TOKEN"` with the Discord bot token you obtained.
    - `activity`: Customize the activity message as desired. Use `{s}` for the server count and `{u}` for the user count.
    - `channel_ids`: Add the Channel IDs of the Discord channels where you want the bot to respond.

4. **Configure the Bot**: Open the `example_config.py` file and update the following variables:

    - `api_key`: Replace `"YOUR_API_KEY"` with your SplitticAPI key.
    - `token`: Replace `"YOUR_DISCORD_BOT_TOKEN"` with the Discord bot token you obtained.
    - `activity`: Customize the activity message as desired. Use `{s}` for the server count and `{u}` for the user count.
    - `channel_ids`: Add the Channel IDs of the Discord channels where you want the bot to respond.

5. **Rename the Configuration File**: After updating, rename `example_config.py` to `config.py` to ensure the bot can access your configuration.

### Web UI Setup

To interact with MeowGPT through a web interface, follow these steps:

1. **Install Flask**: Ensure Flask is installed in your environment. If not, you can install it using pip:

    ```bash
    pip install Flask
    ```

2. **Run the Flask Server**: Execute the `web_ui.py` script to start the web server. Use the following command:

    ```bash
    python web_ui.py
    ```

3. **Access the Web Interface**: Open your web browser and go to `http://127.0.0.1:5000/` to interact with the MeowGPT bot through the web interface.

### Bot Initialization

1. Save your text prompt (if any) in a file named `prompt.txt`. If you don't have a prompt, you can leave the file empty.

2. **Run the Bot**: Execute the `bot.py` script to start your bot. Use the following command:

    ```bash
    python bot.py

    ```bash
    python bot.py
    ```

3. Your bot should now be running and will display "Logged in as [your bot name]" in the console.

### Usage

1. Invite your bot to your Discord server using the OAuth2 link generated on the [Discord Developer Portal](https://discord.com/developers/applications).

2. Ensure the bot has the necessary permissions in the channels you specified in `config.py`.

3. Start chatting with your MeowGPT bot in the designated channels. The bot will respond to messages in the configured channels.

### Customization

Feel free to modify the code in `bot.py` and `config.py` to customize the bot further. You can adjust the prompt, change the activity message, or add more features as needed.

### Free Hosting on splittic.app

Visit [splittic.app](https://splittic.app) to take advantage of free hosting for your MeowGPT Discord bot. Follow the provided instructions to set up and host your bot effortlessly.

## Troubleshooting

If you encounter issues during the setup, check the console for error messages and ensure that you have followed all the steps correctly. If problems persist, refer to the documentation of the libraries used in the code (Discord.py and SplitticAPI) for additional guidance.

Congratulations! You have successfully set up your MeowGPT Discord bot. Enjoy chatting with your AI-powered companion!

