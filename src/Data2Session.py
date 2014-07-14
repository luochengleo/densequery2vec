import sys


fin = open('../data/querylogbyid/'+sys.argv[1]+'.dat')
line = fin.readline()
count = 0
currtime = 0
dataOfSession = dict()
while line != '':
    count +=1
    if count %10000000==0:
        print count
    try:
        segs = line.strip().split('\t')
        
        sessionid= segs[1]
        
        dataOfSession[sessionid] = list()
        
    except:
        print line
    
    line = fin.readline()
fin.close()

def session2text(lt):
    text = ''
    for (q,s,t) in lt:
        text = text+' '+q
    return text

fin = open('../data/querylogbyid/'+sys.argv[1]+'.dat')
fout = open('../data/sessiontext/'+sys.argv[1]+'.txt','w')
line = fin.readline()
count = 0
currtime = 0
while line != '':
    count +=1
#     if count %1000000==0:
#         print float(count)/160000000.0,' clear'
#         for k in dataOfSession.keys():
#             existData = dataOfSession[k]
#             if len(existData)>0:
#                 existTime = existData[-1][2]
#                 if currtime - existTime > 1800.0:
#                     fout.write(session2text(existData)+'\n')
#                     dataOfSession[k] = list()
    segs = line.strip().split('\t')

    if len(segs) ==4 :
        if segs[0]=='P':
            
            type = segs[0]
            sessionid= segs[1]
            time = float(segs[2])
            query = segs[3]

            currtime = time
            existData = dataOfSession[sessionid]
            if len(existData)>0:
                existTime = existData[-1][2]
                if currtime - existTime > 1800.0:
                    fout.write(session2text(existData)+'\n')
                    dataOfSession[sessionid] = list()
                    dataOfSession[sessionid].append(('P@'+query,sessionid,time))
                else:
                    dataOfSession[sessionid].append(('P@'+query,sessionid,time))
            if len(existData) == 0:
                dataOfSession[sessionid].append(('P@'+query,sessionid,time))
    if len(segs) == 5:
        if segs[0] == 'C':
            type = segs[0]
            sessionid= segs[1]
            time = float(segs[2])
            query = segs[3]
            url=segs[4]

            currtime = time
            existData = dataOfSession[sessionid]
            
            if 'www.sogou.com' in url:
                bullet = ('P@'+query,sessionid,time)
            else:
                bullet = ('C@'+url,sessionid,time)
                
            if len(existData)>0:
                existTime = existData[-1][2]
                if currtime - existTime > 1800.0:
                    fout.write(session2text(existData)+'\n')
                    dataOfSession[sessionid] = list()
                    dataOfSession[sessionid].append(bullet)
                else:
                    dataOfSession[sessionid].append(bullet)
            if len(existData) == 0:
                dataOfSession[sessionid].append(bullet)
    line = fin.readline()
fin.close()

for k in dataOfSession.keys():
    existData = dataOfSession[k]
    if len(existData)>0:
        fout.write(session2text(existData)+'\n')
        dataOfSession[k] = list()
fout.close()