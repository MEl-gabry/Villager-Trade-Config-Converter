from sys import argv
import re

def main():
    types = ["Armorer", "Butcher", "Cartographer", "Cleric", "Farmer", "Fisherman", "Fletcher", "Leatherworker", "Librarian", "Mason", "Shepherd", "Toolsmith", "Weaponsmith"]
    with open(argv[1]) as f:
        txt = f.read()
        for i in range(len(types)):
            search = ""
            if i < len(types) - 1:
                search = types[i + 1]
            else:
                search = "$"
            match = re.search(search, txt, re.IGNORECASE)
            type_text = txt[0 : match.span()[0]]
            txt = txt[match.span()[0] : ]
            txt_creator(type_text, types[i])


def txt_creator(string, name):
    with open(f"{name}.txt", "w") as f:
        f.write("Input\tOutput\n")
        matches = list(re.finditer("Level", string))
        level = 1
        for i in range(len(matches)):
            end = matches[i + 1].span()[1] if i < len(matches) - 1 else len(string)
            temp_str = string[matches[i].span()[0] : end]
            trades = re.split("    \d:\n", temp_str)
            trades.pop(0)
            f.write(f"Level {level}\n")
            for trade in trades:
                inp_match = re.search("(?<=      Item1: ).+", trade)
                inp = trade[inp_match.span()[0] : inp_match.span()[1]]
                inp_amount_match = re.search("(?<=      Amount1: ).+", trade)
                inp_amount = trade[inp_amount_match.span()[0] : inp_amount_match.span()[1]]
                out_match = re.search("(?<=      Product: ).+", trade)
                out = trade[out_match.span()[0] : out_match.span()[1]]
                out_amount_match = re.search("(?<=      Amount3: ).+", trade)
                out_amount = trade[out_amount_match.span()[0] : out_amount_match.span()[1]]
                f.write(f"{inp} ({inp_amount})\t{out} ({out_amount})\n")
            f.write("\n")
            level += 1



if __name__ == "__main__":
    main()