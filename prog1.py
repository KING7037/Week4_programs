def val(num):
    if 0 <= num <= 100:
        return True
    else:
        return False

value = int(input("Enter numbers"))
result = val(value)
print("Is " + str(value) + " in the range 0 to 100? " + str(result))


