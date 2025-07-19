class Client:
    def __init__(self, name, telephone):

        self.__name = name
        self.__telephone = telephone

    #encapsulation

    #get method
    def get_name(self):
        return self.__name

    #set method
    def set_name(self, name):
        self.__name = name
