class character:
    def __init__(self) -> None:
        pass
    class Humano:
        def __init__(self,name) ->None:
            self.name=name


        def cost(casilla):
            if casilla==0:# 0=montaña, 1 tierra, 2 agua, 3 arena, 4 bosque, 5 pantano
                return 0
            if casilla==1:
                return 2
            if casilla==2:
                return 2
            if casilla==3:
                return 3
            if casilla==4:#bosque
                return 4
            if casilla==5:
                return 5
            else:
                return -1


    class Sasquatch:
        def __init__(self,name)->None:
            self.name=name


        def cost(casilla):
            if casilla==0:# 0=montaña, 1 tierra, 2 agua, 3 arena, 4 bosque, 5 pantano
                return 15
            if casilla==1:
                return 4
            if casilla==2:
                return 0
            if casilla==3:
                return 0
            if casilla==4:#bosque
                return 4
            if casilla==5:
                return 5
            else:
                return -1

    class Monkey:
        def __init__(self,name)->None:
            self.name=name


        def cost(casilla):
            if casilla==0:# 0=montaña, 1 tierra, 2 agua, 3 arena, 4 bosque, 5 pantano
                return 0
            if casilla==1:
                return 2
            if casilla==2:
                return 4
            if casilla==3:
                return 3
            if casilla==4:#bosque
                return 1
            if casilla==5:
                return 5
            else:
                return -1

    class Octopus:
        def __init__(self,name)->None:
                self.name=name


        def cost(casilla):
            if casilla==0:# 0=montaña, 1 tierra, 2 agua, 3 arena, 4 bosque, 5 pantano
                return 0
            if casilla==1:
                return 2
            if casilla==2:
                return 1
            if casilla==3:
                return 0
            if casilla==4:#bosque
                return 3
            if casilla==5:
                return 2
            else:
                return -1