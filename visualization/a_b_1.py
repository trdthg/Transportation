import csv
headers = ['arrival','departure','time']
rows = []
stations_name = {}
i = 0
with open('dataFolder/a_b_0.csv') as f:
    f_csv = csv.reader(f)
    for row in f_csv:
        # print(i)
        if i==0:
            i += 1
            continue

        if (f'{row[1]}{row[0]}' in stations_name.keys()):
            if rows[stations_name[f'{row[1]}{row[0]}']][2] > row[2]:
                rows[stations_name[f'{row[1]}{row[0]}']][2] = row[2]
            continue
        if (f'{row[0]}{row[1]}' in stations_name.keys()):
            if rows[stations_name[f'{row[0]}{row[1]}']][2] > row[2]:
                rows[stations_name[f'{row[0]}{row[1]}']][2] = row[2]
            continue
        stations_name[f'{row[0]}{row[1]}']=i-1
        # intime = row[2].split(' ')[1].split(':')
        # intime = int(intime[0])*60 + int(intime[1])
        # outtime = row[4].split(' ')[1].split(':')
        # outtime = int(outtime[0])*60 + int(outtime[1])
        # dettime = outtime-intime
        rows.append([f'{row[0]}',f'{row[1]}',row[2]])
        i+=1
with open('dataFolder/a_b_1.csv','w',newline='') as f2:
    f2_csv = csv.writer(f2)
    f2_csv.writerow(headers)
    f2_csv.writerows(rows)