import hashlib, pyperclip

secretKey = pyperclip.paste()

i = 0
while i != -1: # infinite loop, break when answer found
    hash = hashlib.md5(secretKey.encode('ascii') + str(i).encode('ascii')).hexdigest()

    if hash[0:5] == '00000':
        print('Five zero answer: ' + str(i))
        print('Five zero hash: ' + hash)
        break

    i += 1

# restarts from i above so if i starts with 6 zeroes it will also find it
while i != -1: # infinite loop, break when answer found
    hash = hashlib.md5(secretKey.encode('ascii') + str(i).encode('ascii')).hexdigest()

    if hash[0:6] == '000000':
        print('Six zero answer: ' + str(i))
        print('Six zero hash: ' + hash)
        break

    i += 1
