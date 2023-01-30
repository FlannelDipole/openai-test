import openai

openai.api_key = "[your api key here]"

def generate_response(prompt):
    completions = openai.Completion.create(
        engine="text-davinci-003", # This is ChatGPT's learning model
        prompt=prompt,
        max_tokens=1024,
        n=1,
        stop=None,
        temperature=0.5,
    )

    message = completions.choices[0].text
    return message

while True:
    user_input = input("You: ")
    print("OpenAI: Processing request...")
    response = generate_response(user_input)
    print("OpenAI: " + response)
