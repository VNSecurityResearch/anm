import math


def fill_zero(n):
    n = n[2:]
    result = n
    while len(result) < 32:
        result = "0" + result

    return result


def ror(n, num):
    num = num - (math.floor(num / 32) * 32)
    nb = fill_zero(bin(n))
    return int(nb[(32 - num):] + "" + nb[0:(32 - num)], 2)


def rol(n, num):
    num = num - (math.floor(num / 32) * 32)
    nb = fill_zero(bin(n))
    return int(nb[num:] + "" + nb[0:num], 2)


def swap(a, b):
    return b, a


def en(n):
    n = hex(n)
    return int("0x" + n[(2 + len(n) - 10):], 16)


def bu2(n):
    if n < 0:
        return 2 ** 32 + n
    else:
        return n


def bit_not(n):
    nb = fill_zero(bin(n))
    result = ""
    for c in nb:
        if c == "0":
            result += "1"
        else:
            result += "0"

    return int(result, 2)


eax = 0x64636261

ebx = 0x7b2ece63
eax = bit_not(eax)
edx = 0x654f0e9c
eax = en(eax + edx)
eax, ebx = swap(eax, ebx)
eax = 0x7f8b6ea6
ebp = 0x653d93c8
ebx = bu2(ebx - ebp)
ebp = 0xadea7de6
ebx = bu2(ebx - ebp)
edx = 0x6faa838e
ecx = 0x1f68bfb0
ebx = bu2(ebx - ecx)
ebx = bit_not(ebx)
edx = 0xfd11e26d
ebx = en(ebx + edx)
ebp = 0xe7c96e0a
ebx = bu2(ebx - ebp)
edi = 0x366ee99b6
ecx = 0x4d6957ea
ebx = ror(ebx, 0x1e)
eax = 0xcbaa27dd
ebx = en(ebx + eax)
ecx = 0xfcabebff
ebx = bit_not(ebx)
edx = 0xade67923
ebx = en(ebx + edx)
ebx = bit_not(ebx)
eax = 0xe96d2b49
ebx = bu2(ebx - eax)
edx = 0x70ce0c6f
ebx = ebx ^ edx
edx = 0xc49e9e32
eax = 0x964de05a
ebp = 0x93bb2002
ebx = bu2(ebx - ebp)
ebx, edx = swap(ebx, edx)
esi = 0x80db8182
edx = bu2(edx - esi)
eax = 0xa26ea099
edx = bu2(edx - eax)

edx = bit_not(edx)
ebx = 0x185dde4f
edx = bu2(edx - ebx)
edx = rol(edx, 0x66)
esi = 0xdfd46071
edx = ror(edx, 0x54)
edx, ebp = swap(edx, ebp)
ebp = rol(ebp, 0x5c)
ebp = bit_not(ebp)
ebp, edi = swap(ebp, edi)
edi = ror(edi, 0x35)
edx = 0x9e8b974d
edi, esi = swap(edi, esi)
esi, edx = swap(esi, edx)
esi = 0xd9dc07a8
edx = en(edx + esi)
edx = rol(edx, 0x33)
edi = 0xc21ae935
edx = edx ^ edi
ecx = 0x8b68b365
edx = en(edx + ecx)
edx = ror(edx, 0x3c)
edx, ecx = swap(edx, ecx)
ebx = 0x80aea59
ecx = bu2(ecx - ebx)
edi = 0xd830d580
ecx = ecx ^ edi
eax = 0xdffdd910
ecx = bu2(ecx - eax)
ecx = ror(ecx, 0x0c7)
esi = 0xc2da46f2
esi = 0x68c65aba
ecx = ecx ^ esi
ecx = rol(ecx, 0x1c)
esi = 0xaed42ef8
ecx = rol(ecx, 0x0a3)
ecx = rol(ecx, 0x83)
ebp = 0x791dbc7f
ecx = en(ecx + ebp)
ecx = bit_not(ecx)
eax = 0x43e7b0be
ecx = ror(ecx, 0x9a)
eax = 0xf0716a5a
ecx = en(ecx + eax)
ecx = bit_not(ecx)
ecx = bit_not(ecx)
eax = 0x7eeb8405
ecx = en(ecx + eax)
esi = 0x674a9997
ecx = ecx ^ esi
ecx = rol(ecx, 0x3e)
ecx = bit_not(ecx)
esi = 0xdeeaf5b9
ecx = bu2(ecx - esi)

print(hex(ecx))
