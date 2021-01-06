from analizer import grammar as g
import analizer
import os





def grammarReport():
    rep = g.getRepGrammar()
    print("holaaa")
    print(rep)
    cad = ""
    for r1 in rep:
        for r2 in r1:
            if isinstance(r2, analizer.ply.lex.LexToken):
                cad += str(r2.type) + " "
            else:
                cad += "<" + str(r2) + "> "
                if r2 == r1[0]:
                    cad += "::= "
        cad += "\n"
    crearArchivo(cad)


def crearArchivo(cad):
    file = open("./reports/ReporteGramatica.bnf", "w")
    file.write(cad)
    file.close()