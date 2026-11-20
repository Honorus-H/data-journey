"""This program permet you to creat a list of thing you need from the grocery until you press control-d,and after that it prints the list """

def main():
    dico = {}
    dico = get_dic(dico)
    for cle in sorted(dico) :
        print(dico[cle], cle)

def get_dic(d):
    while True:
        try:
            x = input("")
            if x.upper() in d:
                d[x.upper()] += 1
            else:
                d[x.upper()] = 1
        except EOFError:
            return d

main()