import openai
import sys

while True:
    sys.stdout.flush()

    sys.stdout.write('\b')

    openai.api_key = "yourAPIkeyHere"

    print("What is your question? \n")

    question=input()
    print("\n")

    def generate_response(question):
        prompt = f"What is the answer to the following question?\n\n{question}\n\nAnswer:"
        response1 = openai.Completion.create(
            engine="text-davinci-003",
            prompt=prompt,
            temperature=0.2,
            max_tokens=1024,
            top_p=1,
            frequency_penalty=0.33,
            presence_penalty=0.2
        )
        answer = response1.choices[0].text.strip()
        return answer


    response1 = generate_response(question)
    print(response1 + "\n\n\n" + "#Starting again...")
