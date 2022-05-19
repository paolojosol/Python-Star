import turtle
t = turtle.Pen()

t.color('red','black')
t.begin_fill()

count= 0

for x in range(1,14):
    t.forward(300)
    t.left(225)
    count = count+1
    print("Count is: " + str(count))

    if count > 7 and count < 9:
    #if count > 7:
        print("Star pattern complete")
        break







t.end_fill()
print("star born")
