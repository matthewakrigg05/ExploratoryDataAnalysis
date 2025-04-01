import pandas as pd

class DataHandler:
    
    data_path = './sports_data.csv'
    df = None
    
    def __init__(self):
        self.df = pd.read_csv(self.data_path)
        
        
    def format_data(self):
        
        self.df = self.df.drop('S.NO', axis=1) # removing seemingly meaningless column
        
        for col in self.df.select_dtypes(include=['object']).columns:
            self.df[col] = self.df[col].apply(DataHandler.to_title)
            
            
    @staticmethod    
    def to_title(text):
        
        if pd.isna(text):
            return text
        
        return " ".join(word.capitalize() for word in str(text).split())