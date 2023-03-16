class Workcenter:
    number = 123
    capacity = []

    def __init__(self, num_operator, num_machines):
        self.data = []
        self.nw = num_operator
        self.nm = num_machines

    def get_name(self):
        return 'Workcenter Name'
    def add_capacity(self, cap):
        self.capacity.append(cap)
    def update_array(self, array):
        for item in array:
            self.data.append(item)
    


class Product:
    attr_1 = 'new'
    attr_2 = 'out-dated'

    def __init__(self, build, is_manufacturable):
        self.isManu = is_manufacturable

    def design(self):
        print('I am desigining a new product')
    def check_manufacturable(self):
        print('The product manufacturability status: ', self.isManu)


top_ender = Product(1998,False)

top_ender.check_manufacturable()




def generate_square():
    i=1
    while True:
        yield i*i
        i +=1

for num in generate_square():
    if num > 100000:
        break
    print(num)