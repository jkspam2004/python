import main_one

print("top-level in two.py")
main_one.func()

if __name__ == "__main__":
    print("main_two.py is being run directly")
else:
    print("main_two.py is being imported into another module")
