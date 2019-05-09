import pandas as pd       ##用pandas处理csv比csv模块方便
from loadmats import loadma
from loadmats import loadma1
from loadmats import  loadma3

#csvfile = open('D:/medicalData/ASOCT_Label_Data(1)/for_angle_label/for_angle_label/oct_label.csv', 'wb')  #打开方式还可以使用file对象
#writer = csv.writer(csvfile)


#将DataFrame存储为csv,index表示是否显示行名，default=True

#return finallis,u1,u2,u3,u4,files
##########四个用户###########
# label1='rightstatus'
# lis,u1,u2,u3,u4,files=loadma(label1)
# dataframe = pd.DataFrame({'filename':files,'user_label_after_voting':lis,'user1_label':u1,'user2_label':u2,'user3_label':u3,'user4_label':u4})#'filename':files,  意味着列名是filename 该列数据来自列表files
# dataframe.to_csv("D:/medicalData/ASOCT_Label_Data(1)/for_angle_label/for_angle_label/oct_label_right_v1.csv",index=True)
##########四个用户############


###########三个用户###########
label1='rightstatus'
lis,u5,u6,u7,u8,files=loadma3(label1)
dataframe = pd.DataFrame({'filename':files,'user_label_after_voting':lis,'user5_label':u5,'user6_label':u6,'user7_label':u7,'user8_label':u8})#'filename':files,  意味着列名是filename 该列数据来自列表files
dataframe.to_csv("D:/medicalData/ASOCT_Label_Data(1)/for_angle_label/for_angle_label/oct_label_right_user5_user8.csv",index=True)

###########三个用户###########



#writer.writerows(lis)

# csvfile.close()