# batchfuscation
# Make sure that this is in the same folder as batchfuscation file

import os,subprocess
prevLine=''

def compare_files(file1, file2):
    with open(file1, 'rb') as file1, open(file2, 'rb') as file2:
        content1 = file1.read()
        content2 = file2.read()
        if content1 == content2:
            return True
        else:
            return False

def __updateFile__(f, replaceWord, replaceWith):
    for j in f:
        if replaceWord in j:
            f2.write(j.replace(replaceWord, str(replaceWith)))
        else:
            f2.write(j)

while True:
    f = open('batchfuscation', 'r')
    f2 = open('batchfuscation.txt', 'w')
    for i in f:
        if 'set' in i and "exitcodeAscii" not in i and 'rem' not in i:
            if i.split()[1] == '/a':
                index = i.find('=')
                num1 = i.split(i[index])[1].split()[0]
                num2 = i.split(i[index])[1].split()[2]
                replaceWord = '%' + i.split('=')[0].split()[2] + '%'
                replaceWith = (int(num1)%int(num2))
                __updateFile__(f, replaceWord, replaceWith)
            elif 'flag' in i:
                f2.write(i)
            else:
                index = i.find('=')
                replaceWord = '%' + i.split('=')[0].split()[1] + '%'
                replaceWith = i[index+1:-1]
                __updateFile__(f, replaceWord, replaceWith)
        elif 'exitcodeAscii' in i:
            replaceWord = "%" + i.split('=')[0].split()[1] + "%"
            replaceWith = chr(int(prevLine.split()[3]))
            __updateFile__(f, replaceWord, replaceWith)
        elif '@echo' in i:
            f2.write(i)
        else:
            f2.write(i)
        prevLine=i
    f2.close()
    f.close()
    if compare_files('batchfuscation', 'batchfuscation.txt') == True:
        os.system('rm batchfuscation')
        os.system('mv batchfuscation.txt batchfuscation')
        exit()
    else:
        os.system('rm batchfuscation')
        os.system('mv batchfuscation.txt batchfuscation')
