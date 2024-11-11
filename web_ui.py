from flask import Flask, request, render_template_string
from SplitticAPI.meowgpt import ChatModule
import config

# Initialize the Flask app
app = Flask(__name__)

# Initialize the ChatModule with the API key
ChatModule.initialize(config.api_key)
chat_instance = ChatModule.create_chat(config.api_key)

# HTML template for the web interface
html_template = """
<!doctype html>
<html lang="en">
  <head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
    <title>MeowGPT Web Interface</title>
  </head>
  <body>
    <div style="max-width: 600px; margin: auto; padding: 20px;">
      <h1>MeowGPT Web Interface</h1>
      <form method="post" action="/chat">
        <div>
          <label for="user_input">Enter your message:</label>
          <textarea id="user_input" name="user_input" rows="4" style="width: 100%;"></textarea>
        </div>
        <div style="margin-top: 10px;">
          <button type="submit">Send</button>
        </div>
      </form>
      {% if bot_response %}
      <div style="margin-top: 20px;">
        <h2>Bot Response:</h2>
        <p>{{ bot_response }}</p>
      </div>
      {% endif %}
    </div>
  </body>
</html>
"""

@app.route('/', methods=['GET'])
def home():
    return render_template_string(html_template)

@app.route('/chat', methods=['POST'])
def chat():
    user_input = request.form['user_input']
    bot_response = chat_instance.reply(user_input)
    return render_template_string(html_template, bot_response=bot_response)

if __name__ == '__main__':
    app.run(debug=True)

