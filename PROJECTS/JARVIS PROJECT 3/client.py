import openai

# Set your OpenAI API key
openai.api_key="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"  # ← your actual key here


response = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "system", "content": "You are a virtual assistant named Jarvis, skilled in general tasks like Alexa and Google Cloud."},
        {"role": "user", "content": "What is coding?"}
    ]
)

# Print the assistant's reply
print(response.choices[0].message["content"])
