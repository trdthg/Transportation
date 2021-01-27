# 6.是否放假 onehot
workday['date'] = pd.to_datetime(workday['Column1'],format="%Y%m%d")
dayprops = []
for month, day in zip(np.array(df['month']), np.array(df['day'])):
    dayprop = np.array(workday.loc[(workday['date'].dt.month==month) & (workday['date'].dt.day==day)]['Column2'])[0]
    # dayprop = int(float((np.array(workday.loc[(workday['date'].dt.month==month) & (workday['date'].dt.day==day)]['Column2'])[0]).strip())) 
    dayprops.append(dayprop) 