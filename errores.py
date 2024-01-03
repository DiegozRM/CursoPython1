try: 
    a=1
    b=2

    c=(a+b)/0

    print(x)
except ZeroDivisionError:
    print("Error de division")
except Exception as e:
    print(e)