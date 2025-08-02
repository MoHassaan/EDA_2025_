# import pandas as pd
# class DATA_READ:

#     def __init__(self,file_path):
#         self.file_path=file_path

#     def read_csv(self):
#         data = pd.read_csv(self.file_path)
#         return data


# if __name__=='__main__':
#     data = DATA_READ(r"C:\Users\mdhas\OneDrive\Naresh IT\Data files\Visadataset.csv").read_csv()
#     print(data)



import pandas as pd

class DATA_READ:
    
    def __init__(self,file_path):
        self.file_path=file_path

    def csv_read(self):
        data = pd.read_csv(self.file_path)
        return data

    
if __name__=='__main__':
    obj = DATA_READ(r"C:\Users\mdhas\OneDrive\Naresh IT\Data files\Visadataset.csv")
    print(obj.csv_read())