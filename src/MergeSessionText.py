for i in range(0,1024,1):
    fout = open('../data/sessionmerge.txt','a')
    print i
    fout.write(open('../data/sessiontext/'+str(i)+'.txt').read())
    