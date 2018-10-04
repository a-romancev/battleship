from ship import Ship

shippy = Ship(1, 2, False, 2)
shoppy = Ship(1, 2, False, 2)

if shippy.is_dead():
    print("dead")
else:
    print("not dead")

shippy.is_dead()

if shippy.is_dead():
    print("dead")
else:
    print("not dead")

if shoppy.is_dead():
    print("dead")
else:
    print("not dead")

