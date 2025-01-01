from RequirementReader import RequirementReader
from openai import OpenAI


class GptUploader:

    def __init__(self):
        self.pdf_path = str()
        self.descirption = str()

    def check_file_correctness(self):
        pdf_result = RequirementReader().read_pdf_path()
        description_result = RequirementReader().read_description()
        if pdf_result != None and description_result != None:
            self.pdf_path = pdf_result
            self.descirption = description_result
            return True
        return False


def read_api_key():
    with open("api_key.txt", "r", encoding="utf-8") as f:
        api_key = f.read()
    return api_key


if __name__ == "__main__":
    client = OpenAI(api_key=read_api_key())
    try:
        completion = client.chat.completions.create(
            model="gpt-4o",
            store=True,
            messages=[{"role": "user", "content": "write a haiku about ai"}],
        )
        print(completion.choices[0].message["content"])
    except Exception as e:
        print(f"An error occurred: {e}")
