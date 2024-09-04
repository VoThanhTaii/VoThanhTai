class Apartment:
    #class that represents an apartment for sale value in USD

    def __init__(self,_id,mts2, value):
        self._id = _id
        self.mts2 = mts2
        self.value = value
        self.sold = False

    def sell(self):
        if not self.sold:
            self.sold = True
        else:
            print(":Aparment {} was sold"
                .format(self._id))