import aes_function
key = '0f1571c947d9e8590cb7add6af7f6798'
key = key.upper()
def en_img(lst):
    # chia ve cac block
    block = []
    for i in range(0, len(lst), 32):
        block.append(lst[i:i + 32])
    # padding
    m = len(block) - 1
    n = len(block[m])
    if n != 32:
        block[m] = block[m] + '8'
        for i in range(32 - n - 1):
            block[m] = block[m] + '0'
    # aes encryption
    e_lst = ''  # cipher string
    for i in block:
        e_lst += aes_function.encrypt(i, key)
    # go padding
    e_lst = e_lst[:len(e_lst) - (32 - n)]
    # tra ve list hexa
    cipher = []
    for i in range(0, len(e_lst), 2):
        cipher.append(aes_function.bintodec(int(aes_function.hextobin(e_lst[i:i + 2]))))  # tra ve chuoi dec
    return cipher