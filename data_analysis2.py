#加载数据文件
def dataLoad():
    data_file = open("testdata.pcap.flow","r")
    data = data_file.read()
    data = data.split('\n')
    data = data[1:]
    lineNum = len(data)
    result = []
    for i in range(1,lineNum-1):
        line = data[i]
        line = line.split(' ')
        while '' in line:
            line.remove('')
        result.append(line)
    return result
#筛选单向连接并按目标IP计数
def ipCount(data):
    ipPool = {}
    for record in data:
        if record[4] == '->' or record[4] == '?>':
            if record[5] not in ipPool:
                ipPool[record[5]] = 1
            else:
                ipPool[record[5]] += 1
    result = sorted(ipPool.items(),key=lambda x:x[1],reverse=True)
    return result[0]
#筛选目标流量
def dataFilter(data,Dip):
    filteredData = []
    for record in data:
        if record[5] == Dip[0] and (record[4] == '->' or record[4] == '?>'):
            filteredData.append(record)
    return filteredData
#计算时间间隔 单位为us
def timeCal(now,before):
    timeInt = 0.0
    timeInt += (float(now[0]) - float(before[0]))*3600
    timeInt += (float(now[1]) - float(before[1]))*60
    timeInt += (float(now[2]) - float(before[2]))
    timeInt += (float(now[3]) - float(before[3]))/1000000

    return timeInt*1000000
#计算平均时间间隔
def avgInterval(data,Dip):
    data = dataFilter(data,Dip)
    time = []
    avgInt = 0
    for i in range(0,len(data)):
        timeStamp = data[i][0]
        timeStamp = timeStamp.replace(".",":")
        timeStamp = timeStamp.split(':')
        time.append(timeStamp)
        if i >= 1:
            avgInt += timeCal(time[i],time[i-1])
    avgInt = avgInt / (len(time) - 1)
    return avgInt

def main():
    data = dataLoad()
    maxDip = ipCount(data)
    avgInter = avgInterval(data,maxDip)
    print(1000000/avgInter)

main()
