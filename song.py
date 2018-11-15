# Main functino calls sing function if condiiton is true. Since the condition will always be true, it will be called forever.
def main():
    while True:
        sing()


# sing function prints song lyrics, no longer recursive.
def sing():
    print("This is the song that doesn't end.")
    print("Yes, it goes on and on my friend.")
    print("Some people started singing it not knowing what it was,")
    print("And they'll continue singing it forever just because...")


if __name__ == "__main__":
    main()