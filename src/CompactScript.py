import os

fout = open('../data/compact.sh','w')
for f in os.listdir('../data/querylog'):
    fout.write('nohup 7z a ./querylog_7z/'+f+'.7z ./querylog/'+f+' > ./log/'+f+'.log &\n')
fout.close()