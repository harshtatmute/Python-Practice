class test:
    x = 10

    @classmethod
    def change(cls):
        cls.x = 30

t1 = test()
t1.change()
print(t1.x)

