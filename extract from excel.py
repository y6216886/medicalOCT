import  pandas as pd
import os
def loadexcel(path):
   # path="D:/medicalData/ASOCT_Label_Data(1)/ASOCT_Label_Data/user8/201801-201803"
    files=os.listdir(path)
    # print(files)
    u1=[]
    for file in files:
        temppath='D:/medicalData/ASOCT_Label_Data(1)/ASOCT_Label_Data/user8/201801-201803/'+file+'/'+file+'.xlsx'
        #print(temppath)
        a=pd.read_csv(temppath)
        #print(a)

#path="D:/medicalData/ASOCT_Label_Data(1)/ASOCT_Label_Data/user8/201801-201803"
#loadexcel(path)
file='20180330.1727702684-11568-1'
temppath='D:/medicalData/ASOCT_Label_Data(1)/ASOCT_Label_Data/user8/201801-201803/'+file+'/'+file+'.xlsx'
temp='G:/20180330.1727702684-11572-1.xlsx'
a=pd.read_excel(temp)
print(a)