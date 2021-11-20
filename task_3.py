print(1, "процент")
for i in range(2, 5):
    print(i, "процента")
for i in range(5, 20):
    print(i, "процентов")
for i in range(20, 101):
    if i % 10 == 1:
        print(i, "процент")
    elif i % 10 == 2 or i % 10 == 3 or i % 10 == 4:
        print(i, "процента")
    else:
        print(i, "процентов")