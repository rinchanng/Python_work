class Cat():
    def eat(self):
        # 哪一个对象调用方法，则参数self就是那一个对象的引用（指向）
        print("%s 爱吃鱼" % self.name)
    def drink(self):
        print("%s 爱喝水" % self.name)


# 创建一个猫的对象
tom = Cat()
tom.name = "Tom"
tom.eat()
tom.drink()  # 主程序中只需要调用对象和方法，不需要关心怎么实现

# 再创建一个猫对象
lazy_cat = Cat()
lazy_cat.name = "大懒猫"
lazy_cat.eat()
lazy_cat.drink()
