def parenthesis_finder(sent, opening_pos):
    left_parens = 1
    position = opening_pos + 1

    while position < len(sent):
        char = sent[position]

        if char == "(": left_parens += 1
        elif char == ")":
            left_parens -= 1
            if left_parens == 0: return position

        position += 1


print(parenthesis_finder("Sometimes (when I nest them (my parentheticals) too much (like this (and this))) they get confusing.", 10))
