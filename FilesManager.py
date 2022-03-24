import os
temporaryFiles = ["TMP_thunder.txt", "TMP_in.txt", "TMP_eqP1.txt", "TMP_eqP2.txt", "TMP_p1.txt"]
resultFiles = ["P1_INSERTS.sql", "P1_WAS_THUNDER.txt", "P2_INSERTS.sql", "P2_WAS_THUNDER.txt"]

def removeTemporaryFiles():
    for file in temporaryFiles:
        if os.path.exists(file):
            os.remove(file)


def resetTemporaryFiles():
    for file in temporaryFiles:
        open(file, "w").close()


def resetResultFiles():
    if not os.path.exists('./results/'):
        os.mkdir('results')
    for file in resultFiles:
        open("./results/"+file, "w").close()