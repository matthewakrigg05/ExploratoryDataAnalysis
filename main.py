import data
import pandas as pd

def main():
    pd.set_option('display.max_columns', None)
    csv_data = data.DataHandler()
    
    csv_data.format_data()
    
    print(csv_data.df)
    
if __name__ == '__main__':
    main()