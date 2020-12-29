import csv
headers = ['arrival','Stain','departure','Staout','time']
rows = []
with open('dataFolder/a_b_1.csv') as f1:
    f1_csv = csv.reader(f1)
    for row1 in f1_csv:

        stain = '1'
        staout = '1'
        with open('dataFolder/station.csv') as f2:
            f2_csv = csv.reader(f2)
            for row2 in f2_csv:
                if row2[1] == row1[0]:
                    stain = row2[2]
                if row2[1] == row1[2]:
                    staout = row2[2]
        if stain=='1' or staout=='1':
            continue
        rows.append([f'{row1[0]}',stain,f'{row1[2]}',staout,f'{row1[4]}'])
            
with open('dataFolder/a_b_2.csv','w',newline='') as f3:
    f3_csv = csv.writer(f3)
    f3_csv.writerow(headers)
    f3_csv.writerows(rows)
