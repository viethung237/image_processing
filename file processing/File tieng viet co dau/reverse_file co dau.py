import  aes_function
with open('File chua gia tri chuyen doi.txt','r',encoding = 'UTF-8') as changetext, open('File chua gia tri tra ve.txt','w',encoding = 'UTF-8') as originaltext:
    pt = changetext.read()
    for i in range(len(pt)):
        if(pt[i] == '\n'):
            k = i
    value_lst =''
    value_lst = pt[:k]
    temp = int(aes_function.bintodec(int(pt[k:])))
    bin_lst = ''
    for i in range(0,len(value_lst),temp):
        bin_lst += chr(aes_function.bintodec(int(value_lst[i:i+temp])))
    originaltext.write((bin_lst))


