#!/usr/bin/env python3
# -*- config: utf-8 -*-

# Написать программу, которая считывает текст из файла и определяет, сколько в нем слов,
# состоящих из не менее чем семи букв.

if __name__ == '__main__':
    with open('text.txt', 'r') as f:
        text = f.read()
        words = []
        k = 0
        m = 0
        w = ''
        for i in text:
            if i.isalpha() :
                m += 1
                w += i
            else:
                if w != '' :
                    words.append(w)
                if m > 6 :
                    k += 1
                m = 0
                w = ''
words = [i for i in words if len(i) > 6]
print(*words, sep = '\n')
print(len(words))
