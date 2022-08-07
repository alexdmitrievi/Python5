##Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.
##Входные и выходные данные хранятся в отдельных текстовых файлах.'''



def compression():
    f = open('full.txt', 'r')
    o = open('comressed.txt', 'w')
    s = ''
    for i in f.read():
        if s == '': 
            s = i
        elif s[0] == i:
            s += i  
        else:
            o.write(s[0] + str(len(s)))
            s = ''

    o.write(s[0] + str(len(s)))
    f.close
    o.close

compression()
