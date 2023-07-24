import openai

# Set up the OpenAI API key
openai.api_key = "api key"

def get_chatbot_response(message):
    response = openai.Completion.create(
        engine='text-davinci-003',
        prompt=message,
        max_tokens=50,
        temperature=0.6,

        stop=None
    )
    bot_message = response.choices[0].text.strip()
    return bot_message

while True:
    user_message = input("User: ").lower()
    print(get_chatbot_response(user_message))
