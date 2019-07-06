from pystardict import Dictionary
import datetime, os, sys

# Download the dict from http://download.huzheng.org/zh_CN/

class MyDict:
    lazyworm_path = './stardict-lazyworm-ec-2.4.2/lazyworm-ec'
    quick_path ='./stardict-quick_eng-zh_CN-2.4.2/quick_eng-zh_CN'

    def __init__(self):
        self.dict_lazyworm = Dictionary(self.lazyworm_path)
        self.dict_quick = Dictionary(self.quick_path)

    def query(self, word):
        answer = self.mini_query(word)

        if answer == '':
            answer = self.mini_query(word[0].upper() + word[1:])

        if answer == '':
            answer = self.mini_query(word.upper())

        if answer == '' and (word[-1] == 's' or word [-1] == 'd'):
            answer = self.mini_query(word[:-1])
        
        if answer == '' and (word[-2:] == 'es' or word [-2:] == 'ed'):
            answer = self.mini_query(word[:-2])     

        if answer == '' and (word[-3:] == 'ies'):
            answer = self.mini_query(word[:-3] + 'y')  

        return answer

    def mini_query(self, word):
        if word in self.dict_lazyworm:
            return self.dict_lazyworm[word]
        elif word in self.dict_quick:
            return self.dict_quick[word]
        else:
            return ''        


d = MyDict()

m1 = datetime.datetime.today()

with open("input.txt", 'r', encoding="utf-8") as fin:
    with open("output.txt", 'w', encoding="utf-8") as fout:
        lines = fin.readlines()
        #lines = sorted(lines)
        print(len(lines))
        # e.g. line in input.txt, number is optional 
        # the, 127
        # to, 50
        # ...
        for line in lines:
            word = line.strip('\r\n ').split(',')[0]
            if  len(line.strip('\r\n ').split(',')) > 1:
                num = line.strip('\r\n ').split(',')[1]
            else:
                num = '' 
            result = d.query(word.strip('\r\n '))
            fout.write(word + '\t' + num + '\n  ' + result.replace('\n', '\n  ') + '\n'+ '\n')

m2 = datetime.datetime.today()
print(m2-m1)
