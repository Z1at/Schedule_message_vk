import time


# dt = input("Введите дату отправки в формате mm:dd")
tm = [int(i) for i in input("Введите время отправки в формате hh:mm:ss: ").split(":")]
message = input("Введите сообщение: ")


while True:
    if tm[0] == time.localtime().tm_hour and tm[1] == time.localtime().tm_min and tm[2] == time.localtime().tm_sec:
        print(1)
    print(time.localtime())
    time.sleep(1)
