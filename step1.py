new = open('newfile.txt','w')

i = 1
with open('text.py') as f:
    for string in f:
        new.write(str(i)+' '+string)
        i = i+1

new.close()
f.close()







