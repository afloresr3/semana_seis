class Ordenador:
    def __init__(self,dato):
        self.lista=dato
        pass

    def ordenarAsc(self):
        for pos in range(len(self.lista)-1):
            for sig in range(pos+1,len(self.lista)):
                if self.lista[pos] > self.lista[sig]:
                    aux= self.lista[pos]
                    self.lista[pos]=self.lista[sig]
                    self.lista[sig]=aux


    def ordenarDes(self):
        for pos in range(len(self.lista)-1):
            for sig in range(pos+1,len(self.lista)):
                if self.lista[pos] < self.lista[sig]:
                    aux= self.lista[pos]
                    self.lista[pos]=self.lista[sig]
                    self.lista[sig]=aux


    def primer(self):
        return self.lista[0]


    def primerEliminado(self):
        primero=self.lista[0]
        self.lista = self.lista[1:]
        return primero


    def primerEliminado2(self):
        primero=self.lista[0]
        auxlista=[]
        for pos in range(1,len(self.lista)):
            auxlista.append(self.lista[pos])
        self.lista=auxlista
        return primero

    def ultimo(self):
        return self.lista[-1]


    def ultimoEliminado(self):
        ultimo=self.lista[-1]
        self.lista = self.lista[:-1]
        return ultimo


    def ultimoEliminado2(self):
        ultimo=self.lista[-1]
        auxlista=[]
        for pos in range(0,len(self.lista)-1):
            auxlista.append(self.lista[pos])
        self.lista=auxlista
        return ultimo

    


datos = [25,15,20,10]
ord = Ordenador(datos)
print(ord.lista)
# ord.ordenarAsc()
# print(ord.lista)
# ord.ordenarDes()
# print(ord.lista)
# print(ord.ultimo())
# print("Primer elemento: {} lista restante: {}".format(ord.primerEliminado(),ord.lista))
# print("Ultimo elemento: {} lista restante: {}".format(ord.ultimoEliminado2(),ord.lista))

