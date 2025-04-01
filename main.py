import data

def main():
    csv_data = data.DataHandler()
    
    csv_data.format_data()
    
    print(csv_data.df)
    
if __name__ == '__main__':
    main()