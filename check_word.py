import time
import os
import requests


path1 = r'金融壹账通词频统计.txt'
path2 = r'360数科词频统计.txt'


d1 = {}
d2 = {}
l1 = []
l1_ = []
l2 = []
l2_ = []


with open(path1,'r',encoding='utf-8') as f:
    for i in f:
        line = i.strip().split()
        # print(len(line[0]))
        # print(line[0].split(':')[0],int(line[0].split(':')[-1]))
        d1.update({(line[0].split(':')[0]):int(line[0].split(':')[-1])})
        l1.append(line[0].split(':')[0])
        l1_.append(int(line[0].split(':')[-1]))
        # exit()

with open(path2,'r',encoding='utf-8') as f:
    for i in f:
        line = i.strip().split()
        l2.append(line[0].split(':')[0])
        l2_.append(int(line[0].split(':')[-1]))
        d2.update({(line[0].split(':')[0]):int(line[0].split(':')[-1])})
# print(d1['金融'])
if not os.path.exists('check.txt'):       
    with open('check.txt','w',encoding='utf-8') as f:
        f.write('%s\t%s\t%s\t%s\n'%('词汇名','壹账通','360','差距'))
        # print(d1)
        for k in d1:
            # print(d1[k],k)
            # exit()
            if k in l2 and d1[k]>50:
                f.write('%s\t%d\t%d\t%f\n'%(k,d1[k],d2[k],abs((d1[k]-d2[k])/d1[k])))
else:
    with open('check.txt','r',encoding='utf-8') as f:
        for i in f:
            line = i.strip().split()
            # print((line[3]))
            try:
                line[3] = float(line[3])
                # line[3] = float(line[3])
            except:
                pass
            # exit()
            try:
                print(line[3])
                if line[3] <0.4:
                    # print(line)
                    with open('num_same.txt','a',encoding='utf-8') as f_:
                        f_.write('%s'%i)
                elif line[3] > 0.4:
                    with open('num_diff.txt','a',encoding='utf-8') as f_:
                        f_.write('%s'%i)
            except:
                pass
                # print(line)
# else:
    # d3 = {}
    # d4 = {}
    
    # with open('check.txt','w',encoding='utf-8') as f:
        
