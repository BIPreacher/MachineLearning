import pymysql as mdb
import pandas as pd
import sys
import datetime
from pandas import Series, DataFrame


conn = mdb.connect(host ='**', user = '**', password = '**', db = '**', port = 3306)
sql1 = '''SELECT DISTINCT channel, supplier, expedia.`process` as expedia , result FROM expedia WHERE result = 'Success' ORDER BY supplier ASC;'''
expedia = pd.read_sql(sql1,conn)
writer = pd.ExcelWriter('H://lhy//20161025//business_log.xlsx')
expedia.to_excel(writer,'expedia')




