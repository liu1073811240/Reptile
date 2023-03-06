import openai


cmpletion = openai.ChatCompletion.create (
 model="gpt-3.5-turbo",
 messages=[{"role": "user", "content": "Tell the world about the ChatGPT API in the style of a pirate."}]
)

print (cmpletion)

