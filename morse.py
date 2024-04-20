"""
========================================================
文件添加默认信息的模板（文件和代码模板中:Python Script）
作者: Lalevin Martin
邮箱: zzlyxht@outlook.com 或 su-57@foxmail.com
创建时间：2023-02-18:21:55
使用的编译器: nano
========================================================
"""
import time
import os
os.system("clear")
os.system("figlet MORSE NACG")
# 导入摩尔斯电码对应的字母、数字、字符，并以字典的形式保存 。
morse_dict = {
    'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.',
    'F': '..-.', 'G': '--.', 'H': '....', 'I': '..', 'J': '.---',
    'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---',
    'P': '.--.', 'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-',
    'U': '..-', 'V': '...-', 'W': '.--',  'X': '-..-', 'Y': '-.--',
    'Z': '--..', '0': '-----', '1': '.----', '2': '..---', '3': '...--',
    '4': '....-', '5': '.....', '6': '-....', '7': '--...', '8': '---..',
    '9': '----.', 'a': '.-', 'b': '-...', 'c': '-.-.', 'd': '-..',
    'e': '.', 'f': '..-.', 'g': '--.', 'h': '....', 'i': '..',
    'j': '.---', 'k': '-.-', 'l': '.-..', 'm': '--', 'n': '-.',
    'o': '---', 'p': '.--.', 'q': '--.-', 'r': '.-.', 's': '...',
    't': '-', 'u': '..-', 'v': '...-', 'w': '.--', 'x': '-..-',
    'y': '-.--', 'z': '--..', '.': '.-.-.-', ',': '--..--', '?': '..--..',
    '\'': '.----.', '!': '-.-.--', '/': '-..-.', '(': '-.--.', ')': '-.--.-',
    '&amp;': '.-...', ':': '---...', ';': '-.-.-.', '=': '-...-', '+': '.-.-.',
    '-': '-....-', '_': '..--.-', '"': '.-..-.', '$': '...-..-', '@': '.--.-.',
    ' ': '/', '\\': '-..-..'}
# 字符与字符之间用空格连接,单词与单词用“/”区分,输入的文本区分大小写,
# 空格在摩尔斯电码中通常用正斜杠 / 代替。

# 用"滴"表示"."，用"答"表示"-"
morse_dida_dict = {
    'A': '滴答', 'B': '答滴滴滴', 'C': '答滴答滴', 'D': '答滴滴', 'E': '滴',
    'F': '滴滴答滴', 'G': '答答滴', 'H': '滴滴滴滴', 'I': '滴滴', 'J': '滴答答答',
    'K': '答滴答', 'L': '滴答滴滴', 'M': '答答', 'N': '答滴', 'O': '答答答',
    'P': '滴答答滴', 'Q': '答答滴答', 'R': '滴答滴', 'S': '滴滴滴', 'T': '答',
    'U': '滴滴答', 'V': '滴滴滴答', 'W': '滴答答', 'X': '答滴滴答', 'Y': '答滴答答',
    'Z': '答答滴滴', 'a': '滴答', 'b': '答滴滴滴', 'c': '答滴答滴', 'd': '答滴滴',
    'e': '滴', 'f': '滴滴答滴', 'g': '答答滴', 'h': '滴滴滴滴', 'i': '滴滴',
    'j': '滴答答答', 'k': '答滴答', 'l': '滴答滴滴', 'm': '答答', 'n': '答滴',
    'o': '答答答', 'p': '滴答答滴', 'q': '答答滴答', 'r': '滴答滴', 's': '滴滴滴',
    't': '答', 'u': '滴滴答', 'v': '滴滴滴答', 'w': '滴答答', 'x': '答滴滴答',
    'y': '答滴答答', 'z': '答答滴滴', '0': '答答答答答', '1': '滴答答答答', '2': '滴滴答答答',
    '3': '滴滴滴答答', '4': '滴滴滴滴答', '5': '滴滴滴滴滴', '6': '答滴滴滴滴', '7': '答答滴滴滴',
    '8': '答答答滴滴', '9': '答答答答滴', '.': '滴答滴答滴 答答滴', ',': '答答滴滴答答答答', '?': '滴滴答答滴滴答答',
    '!': '答滴答滴答答答答', ':': '答答答滴滴滴答', ';': ' 答滴答滴答滴答答', '-': '答滴滴滴滴答', '_': '滴滴答答滴答 答',
    '(': '答滴答答答滴', ')': '答滴答答答滴答', '"': '滴答 滴滴答滴滴', '$': '滴滴滴答滴滴答滴', '@': '滴答答滴滴答滴',
    '&amp;': '滴答滴滴滴滴滴', '+': '滴答滴答滴滴', '=': ' 答滴滴滴答', '/': '答滴滴答滴答', '\\': '答滴滴答滴滴',
    '#': '滴滴答答答滴滴', ' ': '/'
}


# 文本化为摩尔斯电码
def text_to_morse(text):
    # 定义一个可以将文本转换成摩尔斯电码的函数
    morse_code = ""  # morse_code用来储存摩尔斯电码
    for i in text:
        if i in morse_dict.keys():
            morse_code = morse_code+morse_dict[i]+' '
        else:
            morse_code = morse_code+''  # 如遇其他陌生字符 省略
    return morse_code


# 摩尔斯电码化为文本
def morse_to_text(morse_code):
    # 定义一个可以将摩尔斯电码转换为文本的函数
    # 需要将字符串转化为列表
    morse_code = morse_code.split(' ')
    # 反转字典
    new_morse_dict = {}  # new_morse_dict:定义一个新的字典 用来储存反转后的字典
    for i, j in morse_dict.items():
        if i in 'abcdefghigklmnopqrstuvwxyz':
            i = i.upper()
            new_morse_dict[j] = i  # 反转字典
        else:
            new_morse_dict[j] = i  # 反转字典
    text = ''  # text用来储存解码后的文本
    for k in morse_code:
        if k in new_morse_dict.keys():
            text = text+new_morse_dict[k]
        else:
            text = text+''  # 如遇其他陌生字符省略
    return text


# 文本化为摩尔斯拟声电码
def text_to_dida(text):
    # 定义一个可以将文本转换成摩尔斯拟声电码的函数
    morse_dida_code = ""  # morse_dida_code用来储存拟声摩尔斯电码
    for i in text:
        if i in morse_dida_dict.keys():
            morse_dida_code = morse_dida_code+morse_dida_dict[i]+' '
        else:
            morse_dida_code = morse_dida_code+''  # 如遇其 他陌生字符省略
    return morse_dida_code


# 摩尔斯拟声电码化为文本
def dida_to_text(dida):
    # 定义一个可以将摩尔斯拟声电码转换为文本的函数
    # 字符串化为列表
    dida = dida.split(' ')
    # 反转字典（morse_dida_dict）
    new_morse_dida_dict = {}
    for i, j in morse_dida_dict.items():
        if i in 'abcdefghigklmnopqrstuvwxyz':
            i = i.upper()
            new_morse_dida_dict[j] = i
        else:
            new_morse_dida_dict[j] = i
    # 反转结束
    text = ''
    for k in dida:
        if k in new_morse_dida_dict.keys():
            text = text+new_morse_dida_dict[k]
        else:
            text = text+''  # 如遇其他陌生字符省略
    return text


# 摩尔斯拟声电码化为摩尔斯电码
def dida_to_morse(dida):
    # 定义一个可以将摩尔斯拟声电码转换为摩尔斯电码的函数
    # 将摩尔斯拟声电码转换为文本
    a = dida_to_text(dida)
    # 将文本转换为摩尔斯电码
    return text_to_morse(a)


# 摩尔斯电码化为摩尔斯拟声电码
def morse_to_dida(morse):
    # 定义一个可以将摩尔斯电码转换为摩尔斯拟声电码的函数
    # 将摩尔斯电码转换为文本
    b = morse_to_text(morse)
    # 将文本转换为摩尔斯拟声电码
    return text_to_dida(b)


while True:
    print('{:-^70}'.format('分割线'))
    print('{:^50}'.format('本程序可以将摩尔斯电码与文本相互转换（符号“.”与"-"）'))
    print('{:^50}'.format('输入1：表示将文本转换为摩尔斯电码'))
    print('{:^50}'.format('输入2：表示将摩尔斯电码转换为文本'))
    print('{:^50}'.format('输入3：表示将文本转换为摩尔斯拟声电码（滴答）'))
    print('{:^50}'.format('输入4：表示将摩尔斯拟声电码（滴 答）转换为文本'))
    print('{:^50}'.format('输入5：表示将摩尔斯拟声电码（滴 答）转换为摩尔斯电码'))
    print('{:^50}'.format('输入6：表示将摩尔斯电码转换为摩尔斯拟声电码（滴答）'))
    print('{:^50}'.format('输入其他字符：程序结束运行！'))
    print('{:-^70}'.format('分割线'))
    x = input('\n请选择：')
    if x == '1':
        print('\n接下来将文本转换为摩尔斯电码')
        text2 = input('请输入文本(英语，大小写都可以)：')
        print('文本转换为摩尔斯电码的结果为：\n')
        print(text_to_morse(text2), '\n')
        print('{:-^70}'.format('请稍等'))
        time.sleep(4)
    elif x == '2':
        print('\n接下来将摩尔斯电码转换为文本')
        print('空格在摩尔斯电码中通常用正斜杠 / 代替')
        morse_code1 = input('请输入摩尔斯电码:')
        print('摩尔斯电码转化为文本的结果为：\n')
        print(morse_to_text(morse_code1), '\n')
        print('{:-^70}'.format('请稍等'))
        time.sleep(4)
    elif x == '3':
        print('\n接下来将文本转换为摩尔斯拟声电码（滴答）')
        text3 = input('请输入文本(英语，大小写都可以)：')
        print('文本转换为拟声摩尔斯电码（滴答）的结果为：\n')
        print(text_to_dida(text3), '\n')
        print('{:-^70}'.format('请稍等'))
        time.sleep(4)
    elif x == '4':
        print('\n接下来将摩尔斯拟声电码（滴答）转换为文本')
        print('空格在摩尔斯电码中通常用正斜杠 / 代替')
        dida4 = input('请输入摩尔斯拟声电码(用"滴"表示"."，用"答"表示"-")：')
        print('拟声摩尔斯电码（滴答）转换为文本的结果为：\n')
        print(dida_to_text(dida4), '\n')
        print('{:-^70}'.format('请稍等'))
        time.sleep(4)
    elif x == '5':
        print('\n接下来将摩尔斯拟声电码（滴答）转换为摩尔斯电码')
        dida5 = input('请输入摩尔斯拟声电码(用"滴"表示"."，用"答"表示"-")：')
        print('拟声摩尔斯电码（滴答）转换为摩尔斯电码的结果为：\n')
        print(dida_to_morse(dida5), '\n')
        print('{:-^70}'.format('请稍等'))
        time.sleep(4)
    elif x == '6':
        print('\n接下来将摩尔斯电码转换为摩尔斯拟声电码（滴答）')
        print('空格在摩尔斯电码中通常用正斜杠 / 代替')
        morse_code6 = input('请输入摩尔斯电码：')
        print('摩尔斯电码转换为拟声摩尔斯电码（滴答）的结果为：\n')
        print(morse_to_dida(morse_code6), '\n')
        print('{:-^70}'.format('请稍等'))
        time.sleep(4)
    else:
        break
print('已退出')