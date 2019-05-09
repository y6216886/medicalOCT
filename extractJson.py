import json

lis = []              ##json.loads (and json.load) does not decode multiple json object.  所以使用一个列表来存储数据
with open('D:/medicalData/user1/u1.txt','r') as fp:
    # for i in data["favourite"]["bkmrk"].values():
    #     print(i["guid"],i["lcate"])

    for item in fp:
        lis.append(json.loads(item))
    k=1
    for i in lis:
        print(k,i["left_radio_value"])             ##将Json 当做一个字典
        k+=1
