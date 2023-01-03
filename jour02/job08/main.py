def vitamines (type,saison):
    if type==("fruits"):
        if saison==("hiver"):
            return ("orange, mandarine et kiwi")
        elif saison==("ete"):
            return ("poire,fraise,cassis")
    if type==("legume"):
        if saison==("hiver"):
            return ("carotte,topinambour,endive")
        elif saison==("ete"):
            return ("artichaut,aubergine,navet")

print(vitamines("fruits","hiver"))
print(vitamines("fruits","ete"))
print(vitamines("legume","hiver"))
print(vitamines("legume","ete"))

