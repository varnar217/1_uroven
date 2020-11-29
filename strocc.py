# Вывести последнюю букву в слове
word = 'Архангельск'
# ???
print(word[len(word)-1])


# Вывести количество букв "а" в слове
word = 'Архангельск'
j1=0
#print()

for i in range(len(word)):

    if word[i] == "а" or word[i] == "А":
        j1+=1



print('j1=',j1)

# ???


# Вывести количество гласных букв в слове
word = 'Архангельск'
# ???


# Вывести количество слов в предложении
sentence = 'Мы приехали в гости'
ert=list(sentence.split(' '))
#print(ert[1])
j=0
for i in range(len(ert)):
    #print(ert[i])
    if len((ert[i]))>1:
        j=j+1
    elif ert[i] =='Я' or ert[i] =='я':
        j=j+1
    else:
        continue
print(j)

# ???


# Вывести первую букву каждого слова на отдельной строке
sentence = 'Мы приехали в гости'
ert=list(sentence.split(' '))
for i in range(len(ert)):

    if len((ert[i]))>1:

        print(ert[i][0])

    elif ert[i] =='Я' or ert[i] =='я':

        print(ert[i])

    else:

        continue



# Вывести усреднённую длину слова.
sentence = 'Мы приехали в гости'
ert=list(sentence.split(' '))
number_list=len(ert)
nuber_dlian=0
for i in range(len(ert)):

    if len((ert[i]))>1:

        nuber_dlian+=len((ert[i]))

    elif ert[i] =='Я' or ert[i] =='я':

        nuber_dlian+=1

    else:

        continue
print(nuber_dlian/number_list)
