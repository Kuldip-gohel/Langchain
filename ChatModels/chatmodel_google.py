from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv

load_dotenv()

model = ChatGoogleGenerativeAI(model='gemini-3.7-flash', temperature= 0.7, max_output_tokens=100)

result = model.invoke('What is the capital of India?')

# print(result.content)

# Output 
[{'type': 'text', 'text': 'The capital of India is **New Delhi**.', 'extras': {'signature': 'EqgDCqUDARFNMg+nbEm335nVYWeVcO4WoZGaw1N6GZ1KPpa6qvoMJPYVD86lQ9aA1jD6bXnP6vVmKPe6XcMq12sbpIYl3JmGJ6Y/j2npC5qOAvCSRz5QUNa1TdJXzMPPWOEQ5xC6QhHxS+E6sKICBgcUqy+PxDDKMYpheS8geOTVT9AjLoZAMlEkY0x51+/HqcJSOpJEzCsvDobNL++JnHzlLPOhoeWk924tCZG1PbIc0C9ssInk8+YpOF7yB/BZmubRUiGmpXuml8qHcYlroj7XJpLGihGzABHWUWEDKS/OrfFBwKLQ79FLEq0MiE/AiVWI1bABT376M8BtbzpmEGLDzHfBR2Tn8fvwt5kqm0m3GIqIndWNtjdhUT22eICXQGgmkV2nfSgezP6tOpjvrZZwpZ3MkKuElfGsvGyw5VbNcoCdcTr1cGIi27omTJsjId/6lKGmVO8WUO/kie1EZjqd5iS5nwhdFBAC131Y7b1RU8TrVkaPbgwPl2Snkedzb7KjNmu+or6gQEodygJ8+QwaCEQGpaWcgKK4B9m7y+0mByVztL0BA0xvcA=='}}]

# why this output is coming in this format because the Google Generative AI model returns a structured response that includes not only the text output but also additional metadata.

# if we want only content then,
result = result.content[0]['text']  # Access the first item in the list and get the 'text' field
print(result)  