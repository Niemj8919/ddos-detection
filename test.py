f = open("f.flow","r")
dict={}
dict_1={}
data = f.read()
data = data.split('\n')
n=len(data)
for i in range(1,n-1):
    line = data[i]
    line = line.split(' ')
    while '' in line:
        line.remove('')
    if line[4] in dict:
        dict[line[4]]+=1
        dict_1[line[4]]+=int(line[-2])    #在测试用f.flow文件中，目的IP、流量分别对应line[4]、line[-2],实际使用时应根据netflow包的具体格式加以修改。
    else:
        dict[line[4]]=1
        dict_1[line[4]]=int(line[-2])
dict=sorted(dict.items(),key=lambda x:x[1],reverse=True)
dict_1=sorted(dict_1.items(),key=lambda x:x[1],reverse=True)
print("Sorted by total number of connections")
print("       IP         CON")
for i in range(0,min(200,len(dict)-1)):
    print(dict[i])
print("Sorted by total number of Bytes")
print("       IP         TotByts")
for i in range(0,min(200,len(dict)-1)):
    print(dict_1[i])
