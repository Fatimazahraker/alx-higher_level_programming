#!usr/usr/bin/python3
if __name == "__main__":
    import hidden_4
    for i in range(len(dir(hidden))):
        if (dir(hidden_4)[i][:2] == "__"):
            continue
        print(dir(hidden_4)[i])
