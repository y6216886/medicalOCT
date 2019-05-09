import scipy.io as sio
import os
from  voting import vote
from  voting import vote2
from voting import vote3

#'leftstatus'
def loadma(label):
    path="D:/medicalData/ASOCT_Label_Data(1)/for_angle_label/for_angle_label/user1"
    files=os.listdir(path)
    #print(files)
    u1=[]
    for file in files:
        a=sio.loadmat("D:/medicalData/ASOCT_Label_Data(1)/for_angle_label/for_angle_label/user1/"+file)[label][0][0] ##从.mat 文件中载入数据
        u1.append(a)


    #
    path="D:/medicalData/ASOCT_Label_Data(1)/for_angle_label/for_angle_label/user2"
    files=os.listdir(path)
    #print(files)
    u2=[]
    for file in files:
        a=sio.loadmat("D:/medicalData/ASOCT_Label_Data(1)/for_angle_label/for_angle_label/user2/"+file)[label][0][0]
        u2.append(a)


    path="D:/medicalData/ASOCT_Label_Data(1)/for_angle_label/for_angle_label/user3"
    files=os.listdir(path)
    #print(files)
    u3=[]
    for file in files:
            a=sio.loadmat("D:/medicalData/ASOCT_Label_Data(1)/for_angle_label/for_angle_label/user3/"+file)[label][0][0]
            u3.append(a)


    path="D:/medicalData/ASOCT_Label_Data(1)/for_angle_label/for_angle_label/user4"
    files=os.listdir(path)
    #print(files)
    u4=[]
    for file in files:
        a=sio.loadmat("D:/medicalData/ASOCT_Label_Data(1)/for_angle_label/for_angle_label/user4/"+file)[label][0][0]
        u4.append(a)

    # print(len(u1),len(u2),len(u3),len(u4))
    # print(u1)
    # print(u2)
    # print(u3)
    # print(u4)
    lens=len(u1)
    finallis=[0]*lens
    vote(u1, u2, u3, u4, lens, finallis)
    # for i in range(lens):
    #     finallis[i]=(str(i+1),str(finallis[i]))
    # print(finallis)
    # print("done")
    return finallis,u1,u2,u3,u4,files

# label1='leftstatus'
# loadma(label1)
# label2='rightstatus'
# loadma(label2)

###########################三个用户####################################################
def loadma1(label):
    path="D:/medicalData/ASOCT_Label_Data(1)/for_angle_label/for_angle_label/user5"
    files=os.listdir(path)
    #print(files)
    u5=[]
    for file in files:
        a=sio.loadmat("D:/medicalData/ASOCT_Label_Data(1)/for_angle_label/for_angle_label/user5/"+file)[label][0][0] ##从.mat 文件中载入数据
        u5.append(a)


    #
    path="D:/medicalData/ASOCT_Label_Data(1)/for_angle_label/for_angle_label/user6"
    files=os.listdir(path)
    #print(files)
    u6=[]
    for file in files:
        a=sio.loadmat("D:/medicalData/ASOCT_Label_Data(1)/for_angle_label/for_angle_label/user6/"+file)[label][0][0]
        u6.append(a)


    path="D:/medicalData/ASOCT_Label_Data(1)/for_angle_label/for_angle_label/user7"
    files=os.listdir(path)
    #print(files)
    u7=[]
    for file in files:
            a=sio.loadmat("D:/medicalData/ASOCT_Label_Data(1)/for_angle_label/for_angle_label/user7/"+file)[label][0][0]
            u7.append(a)


    print(len(u5),len(u6),len(u7))
    print(u5)
    print(u6)
    print(u7)
    lens=len(u5)
    finallis=[0]*lens
    vote2(u5, u6, u7, lens, finallis)
    # for i in range(lens):
    #     finallis[i]=(str(i+1),str(finallis[i]))
    print(finallis)
    print("done")
    return finallis,u5,u6,u7,files

#loadma1('leftstatus')

def loadma3(label):
    path="D:/medicalData/ASOCT_Label_Data(1)/for_angle_label/for_angle_label/user5"
    files=os.listdir(path)
    #print(files)
    u1=[]
    for file in files:
        a=sio.loadmat("D:/medicalData/ASOCT_Label_Data(1)/for_angle_label/for_angle_label/user5/"+file)[label][0][0] ##从.mat 文件中载入数据
        u1.append(a)


    #
    path="D:/medicalData/ASOCT_Label_Data(1)/for_angle_label/for_angle_label/user6"
    files=os.listdir(path)
    #print(files)
    u2=[]
    for file in files:
        a=sio.loadmat("D:/medicalData/ASOCT_Label_Data(1)/for_angle_label/for_angle_label/user6/"+file)[label][0][0]
        u2.append(a)


    path="D:/medicalData/ASOCT_Label_Data(1)/for_angle_label/for_angle_label/user7"
    files1=os.listdir(path)
    #print(files)
    u3=[]
    for file in files1:
            a=sio.loadmat("D:/medicalData/ASOCT_Label_Data(1)/for_angle_label/for_angle_label/user7/"+file)[label][0][0]
            u3.append(a)


    path="D:/medicalData/ASOCT_Label_Data(1)/for_angle_label/for_angle_label/user8"
    files2=os.listdir(path)
    #print(files)
    retD = list(set(files1).difference(set(files2)))
    # retB = list(set(listA).intersection(set(listB))
    u4=[]
    count=0
    for file in files1:
        if file not in retD:
            a=sio.loadmat("D:/medicalData/ASOCT_Label_Data(1)/for_angle_label/for_angle_label/user8/"+file)[label][0][0]
            u4.append(a)
        if file in retD:
            count+=1
            u4.append(0)

    # print(len(u1),len(u2),len(u3),len(u4))
    # print(u1)
    # print(u2)
    # print(u3)
    # print(u4)
    lens=len(u1)
    finallis=[0]*lens
    vote3(u1, u2, u3, u4, lens, finallis)
    # for i in range(lens):
    #     finallis[i]=(str(i+1),str(finallis[i]))
    # print(finallis)
    ###################求差集###############################
    # retD = list(set(files1).difference(set(files2)))
    # print(retD)
    # print(len(retD))



    #####################求差集#############################
    # print(u1)
    # print(u2)
    # print(u3)
    # print(u4)
    # print(count)
    # print("done")
    return finallis,u1,u2,u3,u4,files

# label='leftstatus'
# loadma3(label)