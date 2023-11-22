a = [1, 'b', 3, 4, 5]
b = int (input("xou: "))
match b:
    case 1:
        print(a[0])
    case 2:
        print(a[1])
    case other:
        print(a)