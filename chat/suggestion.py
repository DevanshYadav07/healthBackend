



OPENAI_API_KEY='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'
OPENAI_ORG_ID='org-QAP4mBOdqe4FTJjZHs20mO8K'


#
# def suggestion()
import openai

# Set your OpenAI GPT API key
openai.api_key = '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'

def chatgpt(chat):
    # Set the model name (you can change this based on the available models)
    model_name = "text-davinci-003"

    prompt="the person is having disease "+chat+"give suggestion to the patient initial step he should do reply in 50 words max"
    # Make a request to the OpenAI GPT API
    response = openai.Completion.create(
        engine=model_name,
        prompt=prompt,
        max_tokens=150  # You can adjust this parameter based on your desired response length
    )

    print("gpt reply>>",response.choices[0].text.strip())
    # Extract and return the generated text from the API response
    return response.choices[0].text.strip()

