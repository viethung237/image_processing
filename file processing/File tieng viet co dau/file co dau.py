import  aes_function

def change(value,temp):

    if len(value) != temp :
        k = len(value)
        for i in range(temp - k):
            value = '0' + value
    return value

with open('tieng viet co dau.txt','r',encoding = 'UTF-8') as plaintext, open('File chua gia tri chuyen doi.txt','w',encoding = 'UTF-8') as changetext:
    pt = plaintext.read()
    value_lst =[]
    str_len =[]
    bin_str =''
    for i in pt :
        value_lst.append((bin(ord(i)).replace('0b','')))
    for i in value_lst:
        str_len.append(len(i))
    temp  = str_len[0]
    for i in str_len:
        if temp < i :
            temp = i
    for i in range(len(value_lst)):
        value_lst[i] = change(value_lst[i],temp)
        bin_str += value_lst[i]
    changetext.write(bin_str +'\n' + bin(temp)[2:])
