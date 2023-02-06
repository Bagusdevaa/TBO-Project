import grammar

def gabung_rumus(table:list):
    temptable = []
    x=0
    while(x<len(table)-1):
        ada=0 
        temp = ''
        for key,(id,value) in enumerate(grammar.production.items()):
            if(table[x] in value):
                temp = str(id) + ' ' + table[x+1]
                print(temp)
        for key,(id,value) in enumerate(grammar.production.items()):
            if(temp in value):
                temptable.append(temp)
                ada=1
                break
        for key,(id,value) in enumerate(grammar.production.items()):
            if(table[x+1] in value):
                temp = table[x] + ' ' + str(id)
                print(temp)
        for key,(id,value) in enumerate(grammar.production.items()):
            if(temp in value):
                temptable.append(temp)
                #print(temptable)
                ada=1
                break
        if(ada):
            x=x+2
            ubah=1
            continue
        else:
            temptable.append(table[x])
            print(temptable)
            x+=1
    #print(temptable)
    table=temptable
    for x in range(len(table)):
        for key,(id,value) in enumerate(grammar.production.items()):
            if(table[x] in value):
                temptable2 = []
                for a,b in enumerate(table):
                    if(a!=x):
                        temptable2.append(b)
                    else:
                        temptable2.append(id)
                table = temptable2
    print(table)
    return table

def create_table(n):
    table = []
    for i in range(n):
        temp = []
        for j in range(n):
            temp.append("")
        table.append(temp)
    return table

def concat(x, y):
    z = []
    for i in x:
        for j in y:
            z.append("{} {}".format(i, j))
    return z

def table_filling_process(array):
    susunan = grammar.susunan_kata.copy() 
    table = ['' for x in range(len(array))] 
    for i in range(len(array)): # Untuk mendapatkan rule lexicon tiap kata inputan
        table[i] = grammar.check_production([array[i]])[0]
    table = gabung_rumus(table) # [NP,VP,NP]
    print('ini table',table)
    for a,b in enumerate(table):
        for index,(key,value) in enumerate(grammar.main_production.items()):
            if(b in value):
                ada = 0
                for cari in susunan:
                    if(key == cari):
                        ada =1
                        table[a] = key
                        susunan.remove(key)
                        if(len(susunan)==0):
                            susunan=grammar.susunan_kata
                        break
                if(ada):
                    break
    print('ini hasil',table)
    hasil = ' '.join(table)
    print(hasil)
    if(hasil in grammar.production['K']):
        return 1
    else:
        return 0