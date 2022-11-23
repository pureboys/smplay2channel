import requests as rq

r = rq.get('https://raw.githubusercontent.com/iptv-org/iptv/master/streams/jp.m3u')
i = 0

with open('./tv.m3u8', 'wb+') as f:
    for line in r.iter_lines():
        i = i + 1
        if line:
            column = line.split(b',')
            print(column[0])
            if i % 2 == 0:
                f.write(b'#EXTINF:0,' + column[1] + b',,0\n')
            else:
                f.write(column[0] + b'\n')
