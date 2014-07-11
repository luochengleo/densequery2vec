import re
import urllib

datacontent = open('../data/pb_access_log.201107012345.10.12.12.78.nginx')
line = datacontent.readline()
while line != '':
    type = ''
    if 'GET /pv.gif' in line:
        type = 'P'
    if 'GET /cl.gif' in line:
        type = 'C'
    
    uid = re.compile(r'(?<=uigs_cookie=SUID%)(\S{34})')
    uuids = uid.search(line)
    uuid = ''
    if uuids:
        uuid = uuids.groups()[0]
    
    qr = re.compile(r'(?<=query=)(.*?)(?=&rn)')
    querys = qr.search(line)
    query = ''
    if querys:
        query = urllib.unquote(urllib.unquote(querys.groups()[0])).replace('+', '')
    
    tm = re.compile(r'\[(.*?)\]')    
    times = tm.search(line)
    time = ''
    if times :
        time = times.groups()[0]
        segs = time.split(' ')
        time = ''
        if len(segs) == 2:
            ssegs = segs[1].split(':')
            if len(ssegs) ==2:
                time = ssegs[1]
    
    u = re.compile('(?<=href%3D)(.*?)(?=&txt)')
    urls = u.search(line)
    url = ''
    if urls:
        url = urllib.unquote(urls.groups()[0])
    
    print type,uuid,query,time,url
    
    line = datacontent.readline()