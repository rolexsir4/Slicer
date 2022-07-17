keywords = ['import ','with ','for ','if ','while ','=','def ','return']

dict = {}

with open('text.py') as file:
    for num, line in enumerate(file, 1):
        for word in keywords:
            if word in line:
                if dict.get(word) == None:
                    dict[word] = str(num)
                else:
                    dict[word] = (str(dict.get(word)) + ' ' + str(num))

file.close()
print(dict)







