###################################################四个用户投票###############################################################
def vote(list1,list2,list3,list4,lens,finallist):
    for i in range(lens):
        index=0
        temp=-1
        lis=[0,0,0,0,0]
        lis[list1[i]]+=1
        lis[list2[i]] += 1
        lis[list3[i]] += 1
        lis[list4[i]] += 1
        print(i+1,lis)
        #print(currentnum)
        for j in range(1,5):
            if lis[j]==4:
                finallist[i]=j
                continue
            if lis[j]==3:
                finallist[i]=j
                continue
            if lis[j]==2:
                index+=1
                temp=j
        if index==1:                 ##2,1,1 的情况
            finallist[i] = temp
#############################################################四个用户投票###################################################

#############################################################三个用户投票##################################################
def vote2(list1,list2,list3,lens,finallist):
            for i in range(lens):
                index=0
                temp=-1
                lis=[0,0,0,0,0]
                lis[list1[i]]+=1
                lis[list2[i]] += 1
                lis[list3[i]] += 1
                for j in range(1,5):
                    if lis[j]==3:
                        finallist[i]=j
                        continue
                    if lis[j]==2:
                        finallist[i] =j
                        continue
            #finallist[i] = -1
#############################################################三个用户投票##################################################


###################################################三个或者四个投票#########################################################
def vote3(list1,list2,list3,list4,lens,finallist):
    for i in range(lens):
        index=0
        temp=-1
        lis=[0,0,0,0,0]
        if list4[i]!=0:
            lis[list1[i]]+=1
            lis[list2[i]] += 1
            lis[list3[i]] += 1
            lis[list4[i]] += 1
            # print(i+1,lis)
            #print(currentnum)
            for j in range(1,5):
                if lis[j]==4:
                    finallist[i]=j
                    continue
                if lis[j]==3:
                    finallist[i]=j
                    continue
                if lis[j]==2:
                    index+=1
                    temp=j
            if index==1:                 ##2,1,1 的情况
                finallist[i] = temp
        else:
            lis = [0, 0, 0, 0, 0]
            lis[list1[i]] += 1
            lis[list2[i]] += 1
            lis[list3[i]] += 1
            for j in range(1, 5):
                if lis[j] == 3:
                    finallist[i] = j
                    continue
                if lis[j] == 2:
                    finallist[i] = j
                    continue

###################################################三个或者四个投票#########################################################


##############################################################for test#####################################################
# list1=[2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 1, 1, 1, 1, 4]
# list2=[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 2]
# list3=[1, 1, 1, 1, 1, 1, 2, 1, 1, 1, 2, 2, 1, 2, 2, 1, 1, 2, 1, 2, 1, 4, 4, 4, 4, 4, 4, 4, 4, 4, 2, 2, 1, 2, 2, 1, 3, 1]
# list4=[1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 2, 2, 0, 2, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 0, 1, 1, 1, 0, 4]
# lens=len(list1)
# finallist=[0]*lens
# # # vote(list1,list2,list3,list4,lens,finallist)
# # vote2(list1,list2,list3,lens,finallist)
# vote3(list1,list2,list3,list4,lens,finallist)
# print(list1)
# print(list2)
# print(list3)
# print(list4)
# print(finallist)

