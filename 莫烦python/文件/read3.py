with open("new_file2.txt", "r") as f:
    while True:
        line = f.readline()
        print(line)
        if not line:
            break
