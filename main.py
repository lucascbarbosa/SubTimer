from os import listdir
minutes = int(input('How many minutes of difference?(positive to add and negative to cut) '))
seconds = int(input('How many seconds of difference?(positive to add and negative to cut) '))
ep = input('File relative path: ')
subs = open(ep,'r')
lines = subs.readlines()
subs.close()
for i in range(len(lines)):
    timestamp = lines[i].split(' --> ')
    if len(timestamp) == 2:
        start_hour = timestamp[0].split(':')[0]
        start_min = timestamp[0].split(':')[1]
        start_sec = timestamp[0].split(':')[2].split(',')[0]
        start_milisec = timestamp[0].split(':')[2].split(',')[1]
        end_hour = timestamp[1].split(':')[0]
        end_min = timestamp[1].split(':')[1]
        end_sec = timestamp[1].split(':')[2].split(',')[0]
        end_milisec = timestamp[1].split(':')[2].split(',')[1]
        start_min = str(int(start_min)+minutes)
        end_min = str(int(end_min)+minutes)
        start_sec = str(int(start_sec)+seconds)
        end_sec = str(int(end_sec)+seconds)

        if int(start_sec) >= 60:
            start_sec = str(int(start_sec)-60)
            start_min = str(int(start_min)+1)
        
        if int(start_min) >= 60:
            start_min = str(int(start_min)-60)
            start_hour = str(int(start_hour)+1)
        
        if int(end_sec) >= 60:
            end_sec = str(int(end_sec)-60)
            end_min = str(int(end_min)+1)
        
        if int(end_min) >= 60:
            end_min = str(int(end_min)-60)
            end_hour = str(int(end_hour)+1)
            
        if int(start_sec) < 0:
            start_sec = str(int(start_sec)+60)
            start_min = str(int(start_min)-1)
        
        if int(start_min) < 0:
            start_min = str(int(start_min)+60)
            start_hour = str(int(start_hour)-1)
        
        if int(end_sec) < 0:
            end_sec = str(int(end_sec)+60)
            end_min = str(int(end_min)-1)
        
        if int(end_min) < 0:
            end_min = str(int(end_min)+60)
            end_hour = str(int(end_hour)-1)
        
        if len(start_sec) < 2:
            start_sec = '0'+start_sec
        if len(start_min) < 2:
            start_min = '0'+start_min
        if len(end_sec) < 2:
            end_sec = '0'+end_sec
        if len(end_min) < 2:
            end_min = '0'+end_min

        timestamp[0] = start_hour+':'+start_min+':'+start_sec+','+start_milisec
        timestamp[1] = end_hour+':'+end_min+':'+end_sec+','+end_milisec
        lines[i] = ' --> '.join(timestamp)
subs2 = open(ep,'w')
subs2.write(''.join(lines))
subs2.close()
print('Successfull!')