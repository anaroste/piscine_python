from os import system
from sys import stdout
from time import sleep

# def create_generator():
#     mylist = range(3)
#     for i in mylist:
#         yield i*i
#         print('Oui')

# mygenerator = create_generator()
# for i in mygenerator:
#     print(i)

# for i in range(100):
#     print('-'*i)
#     sleep(0.1)
#     system('clear')


def arrow(p):
    ret = 50 * ' '
    ret = list(ret)
    for i in range(50):
        if i <= p / 2:
            ret[i] = '='
    ret[int(p / 2 + 1)] = '>'
    return ''.join(ret)


def ft_progress(lst):
    # toolbar_width = 40
    # stdout.write("[%s]" % (" " * toolbar_width))
    # stdout.flush()
    # stdout.write("\b" * (toolbar_width+1))
    # for i in lst:
    #     stdout.write("->")
    #     stdout.flush()
    #     yield i
    # stdout.write("]\n")
    time = float(10)
    len_lst = len(lst)
    for i in lst:
        p = i * len_lst / 100
        a = arrow(p)
        r = round(i * time / len_lst, 1)
        s = round(time - r, 1)
        ss = '0' + str(s) if s < 10 else s
        ii = '0' + str(i) if i < 10 else i
        print("\b" * 95, flush=True, end='')
        print(f"ETA: {ss}s [{p}%][{a}] {ii}/{len_lst} | elapsed time {r}s", flush=True, end='')
        yield i

listy = range(40)
ret = 0
for elem in ft_progress(listy):
    ret += (elem + 3) % 5
    sleep(0.8)
print()
print(ret)