def faktorial(n):
    if n == 0:     #Bu algoritm 0dam berilgan songa qadar natijani o'zidan keyingi songa
        return 1   #ko'paytirib boradi va yeg'indini print qiladi
    return n * faktorial(n - 1)
print(faktorial(5))

# Fibonacci sonlar ketma ketligi: navbatdagi son o'zidan oldingi
#ikki sonning yeg'indisidan kelib chiqqan sonlar ketma ketligidir 1,1,2,3,5,8,13,21,34,45
def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)

print(fibonacci(4)) # 1,1,2,3 natija  3

def quick_sort(lst):
    if len(lst) <= 1:
        return lst
    else:
        pivot = lst[0]
    left = [x for x in lst[1:] if x <= pivot]
    right = [x for x in lst[1:] if x > pivot]
    return quick_sort(left) + [pivot] + quick_sort(right)
print(quick_sort([4, 7, 1, 2, 5, 6, 3]))


n = 3
src = 'A'
des = 'B'
aux = 'C'

def move_disks(n, src, des, aux):
    if n == 1:
        print(f"Move disk 1 from {src} to {des}")
        return
    move_disks(n - 1, src, aux, des)
    print(f"Move disk {n} from {src} to {des}")
    move_disks(n - 1, aux, des, src)

move_disks(n, src, des, aux)







