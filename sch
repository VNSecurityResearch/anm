import math as m

def sum_input(input):
    sum = 0x0
    for c in input:
        sum += ord(c)

    sum = sum & 0x0000007F

    if sum == 0x0:
        sum = 0x2A

    return sum

def test(password):
    sum = 0x0
    for c in password:
        if c == "A":
            sum += 0x1
        elif c == "B":
            sum += 0x2
        elif c == "C":
            sum += 0x4
        elif c == "D":
            sum += 0x8
        else:
            break

    return sum


def serial(name):
    sumA = sum_input(name)

    # sumA = 1a + 2b + 4c + 8d
    d = int(m.floor(sumA / 8))
    sumA -= d * 8
    c = int(m.floor(sumA / 4))
    sumA -= c * 4
    b = int(m.floor(sumA / 2))
    sumA -= b * 2
    a = sumA

    result = ""
    for i in range(0, d):
        result += "D"
    for i in range(0, c):
        result += "C"
    for i in range(0, b):
        result += "B"
    for i in range(0, a):
        result += "A"

    return str(result)

import socket
import re

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(("10.61.214.216", 9003))

i = 1
while i <= 501:
    data = s.recv(1024)
    if data == "":
        break

    name = data.decode("ASCII")
    print(str(i) + "-" + name)
    name = re.sub(r'[\W_]+', '', name)
    name = name[-8:]
    if (name != ""):
        code = serial(name) + '\r\n'
        print(code)
        s.send(code.encode())

    i += 1

print("Connection closed.")
s.shutdown(socket.SHUT_WR)
s.close()
