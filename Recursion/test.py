def counter():
    for i in range(1, 4):
        print("Generating", i)
        yield i

gen = counter()
for x in gen:
    print("Got:", x)
