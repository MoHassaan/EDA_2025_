from data_read import DATA_READ
from tables import FREQUENCY_TABLE
from chart import IMAGES
import os
from dotenv import load_dotenv

load_dotenv()



file_path = os.getenv('FILE_PATH')
colm = os.getenv('COLUMN_NAME')
obj = DATA_READ(file_path)
data=obj.csv_read()



obj2 = FREQUENCY_TABLE(data,colm)
frq_table = obj2.count_values()


obj3 = IMAGES(frq_table).bar_chart()
obj4 =IMAGES(frq_table).pie_chart()