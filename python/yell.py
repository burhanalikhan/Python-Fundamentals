def yell(*words):
    uppercased = [word.upper() for word in words]
    print(*uppercased)

def main():
    yell("This","is","CS50")

if __name__ == "__main__":
    main()