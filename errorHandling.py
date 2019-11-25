x = 42
y = 0

print()
try:
    print(x/y)
except ZeroDivisionError as e:
    print("Not allowed to divide by 0")
else:
    print("Somethinh else went wrong")
finally:
    print("This is our cleanup code")
print()
