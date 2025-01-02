import os

requirements_path = "../requirement/"
# if not os.path.exists(requirements_path):
#     requirements_path = "..\\requirement\\"


class RequirementReader:
    def __init__(self):
        self.pdf_path = os.path.join(requirements_path, "requirement.pdf")
        self.description_path = os.path.join(requirements_path, "description.txt")
        print("Reading requirements")

    def read_pdf_path(self):
        if os.path.isfile(self.pdf_path):
            return self.pdf_path
        return None

    def read_description(self):
        description = str()
        if os.path.isfile(self.description_path):
            with open(self.description_path, "r", encoding="utf-8") as f:
                description = f.read()
            return description
        return None


if __name__ == "__main__":
    requirement_reader = RequirementReader()
    print(requirement_reader.read_pdf_path())
    print(requirement_reader.read_description())
