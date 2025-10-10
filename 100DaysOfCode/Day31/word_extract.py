import pandas as pd

class EngToArabic:
    def __init__(self):
        self.dict_of_words = {}
        self.create_dict()

    def create_dict(self):
        df = pd.read_csv('arabic.csv')
        for (index, row) in df.iterrows():
            self.dict_of_words[index] = {"English": row.English, "Arabic": row.Arabic}
    
    def get_dict(self):
        return self.dict_of_words
    