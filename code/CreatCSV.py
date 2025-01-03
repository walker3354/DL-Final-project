import csv
import os

class CreatCSV:
    def __init__(self, data):

        self.csv_path = '../output_csv/score.csv'
        # 將字典轉換為字典列表
        self.csv_data = [{'student_id': student_id, 'score': score} for student_id, score in data.items()]
        self.title = ['student_id', 'score']
        if not os.path.exists(self.csv_path):
            self.csv_path = '..\\output_csv\\score.csv'

    def creat_csv(self):  
        with open(self.csv_path, "w", newline="") as f:
            writer = csv.DictWriter(f, fieldnames=self.title)
            writer.writeheader()  # 寫入標題
            for row in self.csv_data:  # 現在 self.csv_data 是一個字典列表
                writer.writerow(row)  # 寫入每一行

if __name__ == "__main__":
    csv_loader  = CreatCSV({'1':10,'2':20})
    csv_loader.creat_csv()