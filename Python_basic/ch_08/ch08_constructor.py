
class MyClass :

    def __init__(self, init_value):
        print('class init')
        self.value_a = init_value
        self.value_b = 10

    def list_sort(self, data):
        data_list = [self.value_a,self.value_b, data]
        data_list.sort()
        return data_list

    def __del__(self):
        print('class dead')

a = MyClass(1)
print(a.list_sort(7))
print(a.list_sort(15))
