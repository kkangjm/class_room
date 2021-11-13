
class parent_class:
    def parent_print(self):
        print('parent_class_method')

    def add(self, a, b):
        print('{0} + {1} = {2}'.format(a, b, a + b))


class child_class(parent_class):
    def child_print(self):
        print('child_class_method')


class child2_class(parent_class):
    # Method overriding
    def add(self, a, b):
        print('{0} x {1} = {2}'.format(a, b, a * b))


# create instance
test = child_class()

# class method
test.child_print()

# method inheritance
test.parent_print()
test.add(3, 4)

# create instance
test2 = child2_class()
# overriding method
test2.add(3, 4)

