# Задание 1
# Дан список учеников, нужно посчитать количество повторений каждого имени ученика.
students = [
  {'first_name': 'Вася'},
  {'first_name': 'Петя'},
  {'first_name': 'Маша'},
  {'first_name': 'Маша'},
  {'first_name': 'Петя'},
]
students_2 =list()
#print(students_2)
counter = {}
for i in students:
    #students_2.append(i.items()[1])
    for j in (i.items()):
        students_2.append(j[1])
        #print(j[1])
    #print(a)
for elem in students_2:
    counter[elem] = counter.get(elem, 0) + 1
doubles = {element: count for element, count in counter.items() if count > 0}
#print(doubles)
for i,j in (doubles).items():
    print(i,' : ',j)
#for i in doubles:
    #print(i)



# Пример вывода:
# Вася: 1
# Маша: 2
# Петя: 2


# Задание 2
# Дан список учеников, нужно вывести самое часто повторящееся имя.
students = [
  {'first_name': 'Вася'},
  {'first_name': 'Петя'},
  {'first_name': 'Маша'},
  {'first_name': 'Маша'},
  {'first_name': 'Оля'},
]
# ???
students_2 =list()
#print(students_2)
counter = {}
for i in students:
    #students_2.append(i.items()[1])
    for j in (i.items()):
        students_2.append(j[1])
        #print(j[1])
    #print(a)
for elem in students_2:
    counter[elem] = counter.get(elem, 0) + 1
doubles = {element: count for element, count in counter.items() if count > 0}
#print(doubles)
ii=0
jj=0
for ele in doubles.items():
    if jj==0:
        ii=ele
        jj=jj+1
    else:
        if ele[1]>ii[1]:
            ii=ele


print('Самое частое имя среди учеников: {}'.format(ii[0]))



# Пример вывода:
# Самое частое имя среди учеников: Маша

# Задание 3
# Есть список учеников в нескольких классах, нужно вывести самое частое имя в каждом классе.
school_students = [
  [  # это – первый класс
    {'first_name': 'Вася'},
    {'first_name': 'Вася'},
  ],
  [  # это – второй класс
    {'first_name': 'Маша'},
    {'first_name': 'Маша'},
    {'first_name': 'Оля'},
  ]
]
a= 0
#school_students_2 ={}

for aer in school_students:
    a=a+1


    #print(j)
    counter = {}
    students_2 =list()
    for i in aer:
        #students_2.append(i.items()[1])
        for j in (i.items()):
            students_2.append(j[1])
            #print(j[1])
        #print(a)
    for elem in students_2:
        counter[elem] = counter.get(elem, 0) + 1
    doubles = {element: count for element, count in counter.items() if count > 0}
    #print(doubles)
    ii=0
    jj=0
    for ele in doubles.items():
        if jj==0:
            ii=ele
            jj=jj+1
        else:
            if ele[1]>ii[1]:
                ii=ele

    print('Самое частое имя в классе {}: {}'.format(a,ii[0]))










# ???

# Пример вывода:
# Самое частое имя в классе 1: Вася
# Самое частое имя в классе 2: Маша


# Задание 4
# Для каждого класса нужно вывести количество девочек и мальчиков в нём.
school = [
  {'class': '2a', 'students': [{'first_name': 'Маша'}, {'first_name': 'Оля'}]},
  {'class': '3c', 'students': [{'first_name': 'Олег'}, {'first_name': 'Миша'}]},
]
is_male = {
  'Маша': False,
  'Оля': False,
  'Олег': True,
  'Миша': True,
}

for i in school:


    nummber_mmen=0
    nummber_women=0
    sscals=''

    for j in i.items():

        if j[0] == 'class':
            sscals=j[1]


        if j[0] == 'students':
            for k in j[1]:
                for jj in k.items():
                    #print(jj[1])
                    if (is_male.get(jj[1])):
                        nummber_mmen=nummber_mmen+1
                    else:
                        nummber_women=nummber_women+1
    print('В классе {} {} девочки и {} мальчика'.format(sscals,nummber_women,nummber_mmen))



# ???

# Пример вывода:
# В классе 2a 2 девочки и 0 мальчика.
# В классе 3c 0 девочки и 2 мальчика.


# Задание 5
# По информации о учениках разных классов нужно найти класс, в котором больше всего девочек и больше всего мальчиков.

numbber=[]
school = [
  {'class': '2a', 'students': [{'first_name': 'Маша'}, {'first_name': 'Оля'}]},
  {'class': '3c', 'students': [{'first_name': 'Олег'}, {'first_name': 'Миша'}]},
]
is_male = {
  'Маша': False,
  'Оля': False,
  'Олег': True,
  'Миша': True,
}
for i in school:


    nummber_mmen=0
    nummber_women=0
    nummber_peaple=[]
    sscals=''

    for j in i.items():

        if j[0] == 'class':
            sscals=j[1]


        if j[0] == 'students':
            for k in j[1]:
                for jj in k.items():
                    #print(jj[1])
                    if (is_male.get(jj[1])):
                        nummber_mmen=nummber_mmen+1
                    else:
                        nummber_women=nummber_women+1

    nummber_peaple.append(nummber_mmen)   #print('В классе {} {} девочки и {} мальчика'.format(sscals,nummber_women,nummber_mmen))
    nummber_peaple.append(nummber_women)
    nummber_peaple.append(sscals)

    numbber.append(nummber_peaple)
#print(numbber)
mmenn=0
ss_mmean=''
wommenn=0
ss_wommen=''
mmenn=numbber[0][0]
wommenn=numbber[0][1]
ss_mmean=numbber[0][2]
ss_wommen=numbber[0][2]


for i in range(1,len(numbber)):
    #print(i)
    if mmenn<numbber[i][0]:
        mmenn=numbber[i][0]
        ss_mmean=numbber[i][2]
    else:
        pass
    if wommenn<numbber[i][1]:
        wommenn=numbber[i][1]
        ss_wommen=numbber[i][2]
    else:
        pass


print('Больше всего мальчиков в классе {}'.format(ss_mmean))
print('Больше всего девочек в классе {}'.format(ss_wommen))
    #print(numbber[i])
#if


# ???

# Пример вывода:
# Больше всего мальчиков в классе 3c
# Больше всего девочек в классе 2a
