

a = ""

while a != "bye":
    a = input("You: ").lower()

    if a == "hello":
        print("Hi")

    elif a == "how are you":
        print("I am fine")

    elif a == "bye":
        print("Goodbye")

    else:
        print("ok")