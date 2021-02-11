"""функция, приводящая  дату  к  удобному  виду"""
def date_time(time: str) -> str:
    b = {'01': "January", '02': 'February', '03': 'March', '04': 'April', '05': 'May', '06': 'June',
         '07': 'July', '08': 'August', '09': 'September', '10': 'October', '11': 'November', '12': 'Drcember'}
    k = time.split('.')#разбить строку  по точкам "."
    c = k[2][5:11].split(':')# разбить остаок строки по двоеточию ":"
    chislo = int(k[0])
    if int(c[0]) == 1:#прописать вручную в переменую окончание, если час равен 1
        hours1 = str(int(c[0])) + ' hour'
    else:
        hours1 = str(int(c[0])) + ' hours'#прописать вручную окнчание к  часам, если  часов  больше ё
    if int(c[1]) == 1:
        minutes1 = str(int(c[1])) + ' minute'
    else:
        minutes1 = str(int(c[1])) + ' minutes'

    return f"{chislo} {b[k[1]]} {k[2][:4]} year {hours1} {minutes1}"


print(date_time("01.04.1812 01:01"))