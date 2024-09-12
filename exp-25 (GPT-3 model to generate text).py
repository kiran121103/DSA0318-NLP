import openai
import time
import random

openai.api_key = 'sk-MDKkj34WaITe-mG91Uo3LpTIIIlsVklYYkqpk_oO2WT3BlbkFJdQQTg6dyWmzppBAxywD4Dv5Om5YLG-MnDTjlyS6_0A'

prompt = "Write a story about an adventure in space."

def generate_text():
    retry_attempt = 0
    while True:
        try:
            response = openai.Completion.create(
                model="gpt-3.5-turbo",
                prompt=prompt,
                max_tokens=150
            )
            print(response.choices[0].text.strip())
            break
        except openai.error.RateLimitError:
            retry_attempt += 1
            wait_time = min(2 ** retry_attempt + random.uniform(0, 1), 60)
            print(f"Rate limit exceeded. Waiting for {wait_time:.2f} seconds before retrying...")
            time.sleep(wait_time)
        except openai.error.OpenAIError as e:
            print(f"An unexpected error occurred: {e}")
            break
        
print(generate_text())
