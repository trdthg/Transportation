routes = {
    '1号线': ['Sta65', 'Sta49', 'Sta149', 'Sta74', 'Sta128', 'Sta34', 'Sta106', 'Sta110', 'Sta97', 'Sta80', 'Sta89', 'Sta64', 'Sta150', 'Sta154', 'Sta107', 'Sta83', 'Sta108', 'sta47','Sta159', 'Sta1'], 
    '2号线': ['Sta63','Sta129', 'Sta9', 'Sta163', 'Sta53', 'Sta79', 'Sta18', 'Sta47', 'Sta123', 'Sta127', 'Sta81', 'Sta27', 'Sta48', 'Sta151', 'Sta68', 'Sta52', 'Sta76', 'Sta57', 'Sta71', 'Sta139', 'Sta105', 'Sta51', 'Sta24'], 
    '3号线': ['Sta143', 'Sta156', 'Sta61', 'Sta50', 'Sta119', 'Sta66', 'Sta12', 'Sta161', 'Sta21', 'Sta133', 'Sta22', 'Sta138', 'Sta41', 'Sta30', 'Sta67', 'Sta144', 'Sta29', 'Sta126','Sta115', 'Sta40', 'Sta131', 'Sta39', 'Sta100','Sta135', 'Sta167', 'Sta113', 'Sta141', 'Sta142', 'Sta158', 'Sta44', 'Sta117', 'Sta147', 'Sta42', 'Sta35','Sta87' 'Sta109', 'Sta33', 'Sta112', 'Sta153', 'Sta125', 'Sta121', 'Sta11'], 
    '10号线': ['Sta157', 'Sta114', 'Sta168', 'Sta135', 'Sta134', 'Sta85', 'Sta2', 'Sta4', 'Sta103', 'Sta145', 'Sta88', 'Sta87', 'Sta94', 'Sta160', 'Sta7', 'Sta6', 'Sta8', 'Sta75', 'Sta102'], 
    '4号线': ['Sta90','Sta84', 'Sta59', 'Sta19', 'Sta62', 'Sta165', 'Sta38', 'Sta58'], 
    '5号线': ['Sta43', 'Sta10', 'Sta96', 'Sta132', 'Sta37', 'Sta16', 'Sta69', 'Sta54', 'Sta56'], 
    '11号线': ['Sta45','Sta75', 'Sta152', 'Sta164', 'Sta82', 'Sta111', 'Sta140', 'Sta13', 'Sta70', 'Sta55', 'Sta20', 'Sta23', 'Sta56', 'Sta118', 'Sta115', 'Sta162','Sta114', 'Sta15', 'Sta86', 'Sta46', 'Sta3','Sta63',  'Sta25', 'Sta146', 'Sta130', 'Sta120'], 
    '11号线_': ['Sta77', 'Sta122', 'Sta36', 'Sta28', 'Sta124', 'Sta166', 'Sta99', 'Sta140'],
    '12号线': ['Sta136','Sta89', 'Sta137', 'Sta101', 'Sta31', 'Sta17','Sta23', 'Sta26', 'Sta90','Sta134', 'Sta95','Sta15', 'Sta72', 'Sta93','Sta3', 'Sta92', 'Sta116', 'Sta32','Sta41', 'Sta91','Sta127', 'Sta60', 'Sta148', 'Sta73']
}

for key in routes:
    aaa = routes[key]
    print(key, end=' ')
    for item in aaa :

        print(item, end=' ')
    print()