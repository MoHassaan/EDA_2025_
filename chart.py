import pandas as pd
import matplotlib.pyplot as plt

class IMAGES:
    
    def __init__(self,freTable):
        self.freqTable=freTable

    def bar_chart(self):
        
        plt.bar(self.freqTable['label'],self.freqTable['count'])
        plt.savefig('bar_chart.jpg')
        plt.show()

    def pie_chart(self):
        plt.pie(self.freqTable['count'],labels=self.freqTable['label'],autopct='%0.2F%%')
        plt.savefig('pie_chart.jpg')
        plt.show()



if __name__=='__main__':
    data = pd.read_csv(r"C:\Users\mdhas\OneDrive\Naresh IT\Data files\Visadataset.csv")
    freq_table = data['continent'].value_counts().reset_index()
    freq_table.columns =['label','count']
    obj = IMAGES(freq_table)
    print(obj.bar_chart())