from RequirementReader import RequirementReader
from HomeworkReader import HomeworkReader
from openai import OpenAI


class GptUploader:

    def __init__(self):
        self.pdf_path = str()
        self.descirption = str()
        self.check_file_correctness()
        self.openAI = OpenAI(api_key=self.load_api_key())

    def check_file_correctness(self):
        pdf_result = RequirementReader().read_pdf_path()
        description_result = RequirementReader().read_description()
        if pdf_result != None and description_result != None:
            self.pdf_path = pdf_result
            self.descirption = description_result
            return True
        return False

    def load_api_key(self):
        with open("api_key.txt", "r", encoding="utf-8") as f:
            api_key = f.read()
        return api_key

    def openAI_chat(self):
        student_file = HomeworkReader().get_student_file_dict()
        for student_id in student_file:
            completion = self.openAI.chat.completions.create(
                model="gpt-4o-mini",
                messages=[
                    {
                        "role": "system",
                        "content": "一個程式設計課程的助教,被要求修改作業",
                    },
                    {
                        "role": "user",
                        "content": self.descirption + student_file[student_id],
                    },
                ],
            )
            print(f"{student_id}成績為: {completion.choices[0].message.content}")


if __name__ == "__main__":
    gpt = GptUploader()
    print(f"{gpt.openAI_chat()}")
