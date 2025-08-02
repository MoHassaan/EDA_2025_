# import pandas as pd

# class FREQUENCY_TABLE:
    
#     def __init__(self,file_path,col):
#         self.file_path=file_path
#         self.col=col

#     def csv_read(self):
#         data = pd.read_csv(self.file_path)
#         return data
    
#     def count_values(self):
#         data=self.csv_read()
#         df=data[self.col].value_counts().reset_index()
#         df.to_csv(f'{self.col}_df.csv',index=False)
#         return df

    
# if __name__=='__main__':
#     obj = FREQUENCY_TABLE(r"C:\Users\mdhas\OneDrive\Naresh IT\Data files\Visadataset.csv",'continent')
#     print(obj.count_values())



import pandas as pd

class FREQUENCY_TABLE:
    
    def __init__(self,data,col):
        self.data=data
        self.col=col

    def count_values(self):
        
        df=self.data[self.col].value_counts().reset_index()
        df.columns=['label','count']
        df.to_csv(f'{self.col}_df.csv',index=False)
        return df

    
if __name__=='__main__':
    data = pd.read_csv(r"C:\Users\mdhas\OneDrive\Naresh IT\Data files\Visadataset.csv")
    col= 'continent'
    obj = FREQUENCY_TABLE(data,col)
    print(obj.count_values())