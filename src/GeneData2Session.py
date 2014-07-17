fout = open('runData2SessionWithOutUrl.sh','w')
for i in range(0,40,1):
    fout.write('nohup python Data2SessionWithOutUrl.py '+str(i)+' > ../data/log/'+str(i)+'.log &\n')
fout.close()