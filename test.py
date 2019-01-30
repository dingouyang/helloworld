# -- coding: utf-8 --


import oop_objvar

droid = []
for i in range(0, 7):
    Robotname = "R-D" + str(i)
    droid.append(oop_objvar.Robot(Robotname))
    droid[i].say_hi()

oop_objvar.Robot.how_many()
