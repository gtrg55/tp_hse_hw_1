import time


def Start():



    print("Добро пожаловать в базу данных с телефонными номерами и именами")
    print("Введите 1 если хотите добавить номер, 2 если хоите что-то найти, 3 если хотите прочитать файл")
    x = int(input())
    if x == 1:
        file_name = "file.txt"

        with open(file_name, "a") as text_file:
            print("что добавить ?")
            time.sleep(0.25)
            print("Введите Имя")
            name_enter = str(input())
            print("Введите Фамилию")
            surname_enter = str(input())
            print("Введите Отчество")
            otchestvo_enter = str(input())
            print("Введите Номер телефона")
            telephon_enter = str(input())
            print("Введите Почту")
            email_enter = str(input())
            class Contact():
                """Ввод данных"""

                def __init__(self, name, surname, otchestvo, email, telephone_num, ):

                    self.name = name

                    self.surname = surname

                    self.otchestvo = otchestvo

                    self.telephone_num = telephone_num

                    self.email = email


                def print_pablic_inf(self):
                    print("Вы ввели")
                    return (self.name, self.surname, self.otchestvo, self.email, self.telephone_num)



            Data_enter = Contact(
                name = name_enter,

                surname = surname_enter,

                otchestvo = otchestvo_enter,

                telephone_num = telephon_enter,

                email = email_enter,



            )
            chto = str(Data_enter.print_pablic_inf())
            chto = str(chto) + '\n'
            print(chto)
            text_file.write(chto)
            time.sleep(0.25)
            print("Данные включены в базу данных")
            print("")
            #print(Data_enter.print_pablic_inf())
            text_file.close()
            Start()



            exit()
    if x == 2:

        print("Введите то, что хотите найти")
        findd = str(input())
        cnt = 0
        if ' ' in findd:
            mas = ""
            mas2 = ""
            mas3 = ""
            cnt = findd.count(' ')
            print("cnt",cnt)
            if cnt == 1:
                lenn = len(findd)
                flag = 0
                for x in range(lenn):
                    a = findd[x]
                    if flag == 0:


                        if a != ' ':

                            mas = mas + str(a)

                        else:
                            flag = 1
                    else:
                        mas2 = mas2 + str(a)
            if cnt == 2:
                lenn = len(findd)
                flag = 0
                flag2 = 0
                stopp = 0
                for x in range(lenn):
                    a = findd[x]
                    if flag2 == 1:
                        mas3 = mas3 +str(a)
                        stopp = 1
                        continue
                    if flag == 0 and stopp == 0:

                        if a != ' ':

                            mas = mas + str(a)

                        else:
                            flag = 1
                            continue
                    else:





                        if a != ' ' :
                            mas2 = mas2 + str(a)
                        else:
                            flag2 = 1




        with open("file.txt", 'r') as text_file:
            for line in text_file:
                a = text_file.readline()
                a = str(a)
                if cnt == 2:

                    if mas in a and mas2 in a  and mas3 in a:
                        print("Найдено!!!")
                        print(a)
                if cnt == 1:
                    if mas in a and mas2 in a:
                        print("Найдено!!!")
                        print(a)
                if cnt == 0:

                    if findd in a:
                        print("Найдено!!!")
                        print(a)


        Start()
    if x == 3:
        with open("file.txt", 'r') as text_file:
            for line in text_file:
                a = text_file.readline()

                print(a)
            Start()











Start()