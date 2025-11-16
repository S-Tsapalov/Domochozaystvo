class PriorityScore:
    #----Критерии-------------
    __energy = None
    __urgency = None
    #----Будущие критерии-----
    #непрерывность
    #кусочность(целостность)
    #временные рамки
    #длительность
    #общие временные рамки
    #геолокация
    #-------------------------

    #----Веса-----------------
    __w_energy = None
    __w_urgency = None
    #-------------------------

    #----Итоговый счет--------
    __score = None

    def __init__(self, energy, urgency, w_energy, w_urgency):
        self.__energy = energy
        self.__urgency = urgency
        self.__w_energy = w_energy
        self.__w_urgency = w_urgency
        self.__score = self.__energy * self.__w_energy + self.__urgency * self.__w_urgency

    def get_score(self):
        return self.__score

    def get_energy(self):
        return self.__energy

    def get_urgency(self):
        return self.__urgency

    def get_w_energy(self):
        return self.__w_energy

    def get_w_urgency(self):
        return self.__w_urgency

