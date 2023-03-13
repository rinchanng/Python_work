class Cat():
    def eat(self):
        print("小猫爱吃鱼")
    def drink(self):
        print("小猫爱喝水")


# 创建一个猫的对象
tom = Cat()
tom.eat()
tom.drink()  # 主程序中只需要调用对象和方法，不需要关心怎么实现

# 再创建一个猫对象
lazy_cat = Cat()
lazy_cat.eat()
lazy_cat.drink()
