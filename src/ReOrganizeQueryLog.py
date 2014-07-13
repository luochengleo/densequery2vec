
SPLITS = 2048
cache = dict()
for i in range(0,SPLITS,1):
    cache[i] = list()

count = 0
for i in range(1,31,1):
    digit = ''
    if i<10:
        digit = '0'+str(i)
    else:
        digit = str(i)
    filename = '../data/querylog/201204'+digit+'.dat'
    print filename
    fin = open(filename)
    line  = fin.readline()
    while line != '':
        count +=1
        segs = line.strip().split('\t')
        if len(segs)>2:
            userid =segs[1]
            hashmod = userid.__hash__()%SPLITS
            cache[hashmod].append(l)
        if count%10000000==0:
            for idx in range(0,SPLITS,1):
                fout = open('../data/querylogbyid/'+str(idx)+'.dat','a')
                for item in cache[idx]:
                    fout.write(item)
                fout.close()
                cache[idx] = list()
        line  = fin.readline()
    