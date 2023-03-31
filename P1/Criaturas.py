
def humano(casilla):
    if casilla=='0':# 0=montaña, 1 tierra, 2 agua, 3 arena, 4 bosque, 5 pantano
                return 0
    if casilla=='1':
                return 1
    if casilla=='2':
                return 2
    if casilla=='3':
                return 3
    if casilla=='4':#bosque
                return 4
    if casilla=='5':
                return 5
    else:
                return -1
def Sasquatch(casilla):
            if casilla=='0':# 0=montaña, 1 tierra, 2 agua, 3 arena, 4 bosque, 5 pantano
                return 15
            if casilla=='1':
                return 4
            if casilla=='2':
                return 0
            if casilla=='3':
                return 0
            if casilla=='4':#bosque
                return 4
            if casilla=='5':
                return 5
            else:
                return -1
def Monkey(casilla):
            if casilla=='0':# 0=montaña, 1 tierra, 2 agua, 3 arena, 4 bosque, 5 pantano
                return 0
            if casilla=='1':
                return 2
            if casilla=='2':
                return 4
            if casilla=='3':
                return 3
            if casilla=='4':#bosque
                return 1
            if casilla=='5':
                return 5
            else:
                return -1
def Octopus(casilla):
            if casilla=='0':# 0=montaña, 1 tierra, 2 agua, 3 arena, 4 bosque, 5 pantano
                return 0
            if casilla=='1':
                return 2
            if casilla=='2':
                return 1
            if casilla=='3':
                return 0
            if casilla=='4':#bosque
                return 3
            if casilla=='5':
                return 2
            else:
                return -1

switch={'1':humano,
        '2':Sasquatch,
        '3':Monkey,
        '4':Octopus

}