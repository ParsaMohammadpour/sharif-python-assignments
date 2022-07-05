#Almost all of test cases in folder 'q5-finglish' are wrong!
import pandas as pd
#df = pd.read_csv('4th-Assignment/q5-finglish/2/words-csv-finglish.csv')
df = pd.read_csv('4th-Assignment/words-csv-finglish.csv')
#with open('4th-Assignment/q5-finglish/dwords-finglish.txt') as f:
with open('4th-Assignment/dwords-finglish.txt') as f:
    lines = [line.rstrip() for line in f]
answer = []
for i in range(len(df['word'].values)):
    ls = []
    if not df['prefix'].values[i]:
        for j in lines:
            if j.endswith(df['word'].values[i]):# and len(j) != len(df['word'].values[i]):
                ls.append(j)
    elif df['prefix'].values[i]:
        for j in lines:
            if j.startswith(df['word'].values[i]):# and len(j) != len(df['word'].values[i]):
                ls.append(j)
    print(len(ls))
    answer.append(len(ls))
    ls = ls[:50]
    for k in ls:
        print(k)
        answer.append(k)
#with open('q5-finglish/3/ans-finglish.txt', encoding='utf-16-le') as file:
#    anss_line = [line.rstrip() for line in file]
#for i in range(len(anss_line)):
#    if anss_line[i].__eq__(answer[i]):
#        print('Mistake.')
#        print(anss_line[i])
#        print(answer[i])
#        exit(0)
#print('Successful')