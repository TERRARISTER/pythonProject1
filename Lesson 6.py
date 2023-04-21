try:
    print("start code")
    print(10/0)
    print("No errors")
except (NameError, ZeroDivisionError):
    print("Wehave an error")

print("code after capsule")