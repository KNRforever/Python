"""
Задание 5.

Выполнить пинг веб-ресурсов yandex.ru, youtube.com и
преобразовать результаты из байтовового в строковый тип на кириллице.

Подсказки:
--- используйте модуль chardet, иначе задание не засчитается!!!
"""
import subprocess
import chardet

ARGS = ['ping', 'yandex.ru']
YA_PING = subprocess.Popen(ARGS, stdout=subprocess.PIPE)
for line1 in YA_PING.stdout:
    result = chardet.detect(line1)
    line = line1.decode(result['encoding']).encode('utf-8')
    print (line1)


AS = ['ping', 'youtube.com']
Y_PING = subprocess.Popen(AS, stdout=subprocess.PIPE)
for line2 in Y_PING.stdout:
    result = chardet.detect(line2)
    line = line2.decode(result['encoding']).encode('utf-8')
    print(line2)

