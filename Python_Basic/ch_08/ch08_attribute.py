
class MyClass :
    cls_attr = []
    def __init__(self):
        self.inst_attr = []

    def append_instAttr(self, a):
        self.inst_attr.append(a)

    def append_clsAttr(self, a):
        MyClass.cls_attr.append(a)


a = MyClass()
a.append_clsAttr(1)
a.append_instAttr(2)

print('instance a : cls_attr =', a.cls_attr)
print('instance a : inst_attr =', a.inst_attr)

b = MyClass()
b.append_clsAttr('a')
b.append_instAttr('b')

print('instance b : cls_attr =' , b.cls_attr)
print('instance b : inst_attr =',b.inst_attr)
