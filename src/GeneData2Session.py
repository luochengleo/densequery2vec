fout = open('runData2Session.sh','w')
for i in range(0,24,1):
    fout.write('nohup python Data2Session.py '+str(i)+' > ../data/log/'+str(i)+'.log &\n')
fout.close()