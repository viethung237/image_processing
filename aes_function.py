# Function Use for all
def dectohex(n):
    hex_n = hex(n)
    hex_n = hex_n.replace('0x','')
    if len(hex_n) == 1:
        hex_n = '0' + hex_n
    return hex_n
# hextobin function

def hextobin(s):
    changehex = {'0': '0000',
                 '1': '0001',
                 '2': '0010',
                 '3': '0011',
                 '4': '0100',
                 '5': '0101',
                 '6': '0110',
                 '7': '0111',
                 '8': '1000',
                 '9': '1001',
                 'A': '1010',
                 'B': '1011',
                 'C': '1100',
                 'D': '1101',
                 'E': '1110',
                 'F': '1111'}
    binary = ''
    for i in range(len(s)):
        binary = binary + changehex[s[i]]
    return binary


# bintohex function
def bintohex(s):
    changebin = {'0000': '0',
                 '0001': '1',
                 '0010': '2',
                 '0011': '3',
                 '0100': '4',
                 '0101': '5',
                 '0110': '6',
                 '0111': '7',
                 '1000': '8',
                 '1001': '9',
                 '1010': 'A',
                 '1011': 'B',
                 '1100': 'C',
                 '1101': 'D',
                 '1110': 'E',
                 '1111': 'F'}
    heximal = ''
    for i in range(0, len(s), 4):
        ch = ''
        ch += s[i]
        ch += s[i + 1]
        ch += s[i + 2]
        ch += s[i + 3]
        heximal = heximal + changebin[ch]
    return heximal


# bin to dec function
def bintodec(binary):  # ham chuyen bin ve dec
    decimal = 0
    i = 0
    while (binary != 0):
        dec = binary % 10
        decimal += dec * pow(2, i)
        binary = binary // 10
        i += 1
    return decimal
#dec to hex function


# permute function
def permute(k, arr, n):
    permutation = ''
    for i in range(0, n):
        permutation += k[arr[i] - 1]
    return permutation


# xor two string function
def xor(a, b):
    cal = ''
    for i in range(len(a)):
        if a[i] == b[i]:
            cal += '0'
        else:
            cal += '1'
    return cal

def xor_hex(a,b):
    a = hextobin(a)
    b = hextobin(b)
    c = xor(a,b)
    c = bintohex(c)
    return c

# function change input to 16 byte matrix with type bin
def ge_matrix(pt):
    c_matrix = []
    for i in range(0, len(pt), 2):
        ch = ''
        ch += pt[i]
        ch += pt[i + 1]
        c_matrix.append(ch)
    for i in range(len(c_matrix)):
        c_matrix[i] = hextobin(c_matrix[i])
    return c_matrix


# Function use for one:
#pt = '0123456789abcdeffedcba9876543210'
#key = '0f1571c947d9e8590cb7add6af7f6798'
#pt = pt.upper()
#key = key.upper()
# use for shiftrow:
shiftrow_table = [1, 5, 9, 13,
                  6, 10, 14, 2,
                  11, 15, 3, 7,
                  16, 4, 8, 12]
# use for mixcolumn:
re_table = [1, 5, 9, 13,
            2, 6, 10, 14,
            3, 7, 11, 15,
            4, 8, 12, 16]


def gmul(x, a):  # phep nhan trong GF(2^8)
    x = hextobin(x)
    value = ''
    if int(a) == 1:  # nhan x voi '01'
        return x  # bintohex(x)
    elif int(a) == 2:  # nhan x voi '02'
        if int(x[0]) == 0:
            for i in range(1, len(x)):
                value += x[i]
            value += '0'
        else:
            value = xor(x[1:] + '0', '00011011')
        return value  # bintohex(value)


def mixColumns(a, b, c, d):
    val = []
    val.append(xor(xor(xor(gmul(a, 2), xor(gmul(b, 1), gmul(b, 2))), gmul(c, 1)), gmul(d, 1)))
    val.append(xor(xor(xor(gmul(a, 1), gmul(b, 2)), xor(gmul(c, 1), gmul(c, 2))), gmul(d, 1)))
    val.append(xor(xor(xor(gmul(a, 1), gmul(b, 1)), gmul(c, 2)), xor(gmul(d, 1), gmul(d, 2))))
    val.append(xor(xor(xor(xor(gmul(a, 1), gmul(a, 2)), gmul(b, 1)), gmul(c, 1)), gmul(d, 2)))
    return val


def change_to_dictionary(pt):
    new_pt = []
    for i in range(len(pt)):
        for j in range(len(pt[i])):
            new_pt.append(pt[i][j])
    return new_pt


def permute_dictionary(k, arr, n):
    permutation = []
    for i in range(0, n):
        permutation.append(k[arr[i] - 1])
    return permutation


# Sbox
sbox = [['63', '7C', '77', '7B', 'F2', '6B', '6F', 'C5', '30', '01', '67', '2B', 'FE', 'D7', 'AB', '76'],
        ['CA', '82', 'C9', '7D', 'FA', '59', '47', 'F0', 'AD', 'D4', 'A2', 'AF', '9C', 'A4', '72', 'C0'],
        ['B7', 'FD', '93', '26', '36', '3F', 'F7', 'CC', '34', 'A5', 'E5', 'F1', '71', 'D8', '31', '15'],
        ['04', 'C7', '23', 'C3', '18', '96', '05', '9A', '07', '12', '80', 'E2', 'EB', '27', 'B2', '75'],
        ['09', '83', '2C', '1A', '1B', '6E', '5A', 'A0', '52', '3B', 'D6', 'B3', '29', 'E3', '2F', '84'],
        ['53', 'D1', '00', 'ED', '20', 'FC', 'B1', '5B', '6A', 'CB', 'BE', '39', '4A', '4C', '58', 'CF'],
        ['D0', 'EF', 'AA', 'FB', '43', '4D', '33', '85', '45', 'F9', '02', '7F', '50', '3C', '9F', 'A8'],
        ['51', 'A3', '40', '8F', '92', '9D', '38', 'F5', 'BC', 'B6', 'DA', '21', '10', 'FF', 'F3', 'D2'],
        ['CD', '0C', '13', 'EC', '5F', '97', '44', '17', 'C4', 'A7', '7E', '3D', '64', '5D', '19', '73'],
        ['60', '81', '4F', 'DC', '22', '2A', '90', '88', '46', 'EE', 'B8', '14', 'DE', '5E', '0B', 'DB'],
        ['E0', '32', '3A', '0A', '49', '06', '24', '5C', 'C2', 'D3', 'AC', '62', '91', '95', 'E4', '79'],
        ['E7', 'C8', '37', '6D', '8D', 'D5', '4E', 'A9', '6C', '56', 'F4', 'EA', '65', '7A', 'AE', '08'],
        ['BA', '78', '25', '2E', '1C', 'A6', 'B4', 'C6', 'E8', 'DD', '74', '1F', '4B', 'BD', '8B', '8A'],
        ['70', '3E', 'B5', '66', '48', '03', 'F6', '0E', '61', '35', '57', 'B9', '86', 'C1', '1D', '9E'],
        ['E1', 'F8', '98', '11', '69', 'D9', '8E', '94', '9B', '1E', '87', 'E9', 'CE', '55', '28', 'DF'],
        ['8C', 'A1', '89', '0D', 'BF', 'E6', '42', '68', '41', '99', '2D', '0F', 'B0', '54', 'BB', '16']]

# use for key expansion:

# Rcon
Rcon = ['01', '02', '04', '08', '10', '20', '40', '80', '1B', '36']


# ge_matrix_hex function:
def ge_matrixhex(pt):
    c_matrix = []
    for i in range(0, len(pt), 2):
        ch = ''
        ch += pt[i]
        ch += pt[i + 1]
        c_matrix.append(ch)
    # for i in range(len(c_matrix)):
    # c_matrix[i]=hextobin(c_matrix[i])
    return c_matrix


# left shift function
def rotword(word):
    return word[1:] + word[:1]


# subtitute function
def subword(word):
    b_word = []
    s_word = []

    for i in range(len(word)):
        b_word.append(hextobin(word[i]))
    for i in range(len(b_word)):
        row = bintodec(int(b_word[i][0] + b_word[i][1] + b_word[i][2] + b_word[i][3]))
        column = bintodec(int(b_word[i][4] + b_word[i][5] + b_word[i][6] + b_word[i][7]))
        val = sbox[row][column]
        s_word.append(val)

    return s_word


# xor with rcon function
def r_xor(rcon, y):
    val = []
    val.append(bintohex(xor(hextobin(rcon), hextobin(y[0]))))
    val = val + y[1:]
    return val


# xor two list function
def wt_xor(word, temp):
    value = []
    for i in range(len(word)):
        value.append(bintohex(xor(hextobin(word[i]), hextobin(temp[i]))))
    return value


# Use for add round key
def tuptolist(pt):
    back = []
    for i in range(len(pt)):
        for j in range(len(pt[i])):
            back.append(hextobin(pt[i][j]))
    return back


def list_bin(pt):
    val = []
    for i in range(len(pt)):
        val.append(hextobin(pt[i]))
    return val


# KEY EXPANSION ALGORITHM
def key_expansion(key):
    key = key.upper()
    key = ge_matrixhex(key)
    w = [()] * 44
    # tao ra 4 word ban dau
    for i in range(4):
        w[i] = (key[4 * i], key[4 * i + 1], key[4 * i + 2], key[4 * i + 3])

    for i in range(4, 44):
        # get required previous keywords
        temp = w[i - 1]
        word = w[i - 4]

        # if multiple of 4 use rot, sub, rcon et
        if i % 4 == 0:
            x = rotword(temp)
            y = subword(x)
            rcon = Rcon[int(i / 4) - 1]
            temp = tuple(r_xor(rcon, y))

        xord = ''.join(wt_xor(word, temp))
        w[i] = (xord[:2], xord[2:4], xord[4:6], xord[6:8])
    return w





def encrypt(pt_u,key):
    w = key_expansion(key)
    w_bin = tuptolist(w)
    #print('w_bin : ', w_bin)
    pre_pt = ge_matrix(pt_u)
    # pre_pt = permute(pre_pt,re_table,16)
    for i in range(len(pre_pt)):
        pre_pt[i] = bintohex(xor(pre_pt[i], w_bin[i]))

    # 10 round

    k = 16
    for i in range(10):

        # s box algorithm
        sub_pt = subword(pre_pt)
        #print('after_sub_ pt : ', sub_pt)
        # shiftrow algorithm
        s_pt = ge_matrix(permute(sub_pt, shiftrow_table, 16))
        for p in range(len(s_pt)):
            s_pt[p] = bintohex(s_pt[p])
        #print('after_shift_row :  ', s_pt)
        # Mix column algorithm
        # print(' i : ' , i)
        if (i != 9):
            sm_pt = []
            for m in range(0, 4):
                sm_pt.append(mixColumns(s_pt[m], s_pt[m + 4], s_pt[m + 8], s_pt[m + 12]))
            for n in range(len(sm_pt)):
                for j in range(len(sm_pt[n])):
                    sm_pt[n][j] = bintohex(sm_pt[n][j])
            s_pt = change_to_dictionary(sm_pt)
            #print('after mix : ', s_pt)
        else:
            s_pt = permute_dictionary(s_pt, re_table, 16)

            # Addroundkey algorithm
        pt = []
        for j in range(len(s_pt)):
            # print('w_bin : ' , bintohex(w_bin[k+j]) )
            pt.append(bintohex(xor(hextobin(s_pt[j]), w_bin[k + j])))
        pre_pt = pt
        #print('new_round_matrix : ', pre_pt)
        k += + 16
        # print( ' k : ' , k)
    ciphertext =''
    for i in range(len(pre_pt)):
        ciphertext += pre_pt[i]

    return ciphertext


#print('ciphertext : ', encrypt(w, pt))
