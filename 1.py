x=int(input())
#это переменна И с которой мы будем работать в цикле
i = 1
while i <= x:
#все делители меньше самого числа
    i += 1
    if x % i == 0:
#собственно тут если Х не кратно к переменной И добавляется еще одна еденичка, если кратно то выводится на принт
        print(i)
        break
#ставим эту чудесную команду БРЭАК или что это и тем самым выводим только первое НАИМЕНЬШЕЕ ЗНАЧЕНИЕ

