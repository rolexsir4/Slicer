vdef = 'def'
vreturn = 'return'

kv = {}
linereturn = 0
linedef = 0

with open('text.py') as file:
    for num, line in enumerate(file, 1):
        if vdef in line:
            if line.split()[0] == 'def':
                linedef = num
                funcname = line.split()[1]
                funcdef = funcname[0:funcname.find('(')]
        if vreturn in line:
            if line.split()[0] == 'return':
                linereturn = num
        kv[funcdef]=(str(linedef)+'-'+str(linereturn))

file.close()
print(kv)






