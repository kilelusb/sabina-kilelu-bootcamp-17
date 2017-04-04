class Car(object):
    speed=0
    def __init__(self, name='General', model='GM', car_type='None'):
        self.name = name
        self.model = model
        self.type = car_type
        self.speed = speed

        if self.name == 'Koenigsegg' or self.name=='Porsche':
            self.num_of_doors = 2
        else:
            self.num_of_doors = 4
        if  self.type == 'trailer':
            self.num_of_wheels = 8
        else:
            self.num_of_wheels = 4

    def is_saloon(self):
         if self.type != 'saloon':
             return False
             
         else:
             return True
