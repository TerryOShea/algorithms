def reverse_words(msg): 
    msg = msg.split()
    lg = len(msg)
    for i in range(lg//2): 
        msg[i], msg[lg - i - 1] = msg[lg - i - 1], msg[i]
    return " ".join(msg)

print reverse_words("find you will pain only go you recordings security the into if")