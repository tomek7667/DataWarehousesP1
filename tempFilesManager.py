import os
temporaryFiles = ["TMP_thunder.txt", "TMP_in.txt", "TMP_eqP1.txt", "TMP_eqP2.txt", "TMP_p1.txt"]


def removeTemporaryFiles():
    for file in temporaryFiles:
        print('usuwam', file)
        if os.path.exists(file):
            os.remove(file)


def resetTemporaryFiles():
    for file in temporaryFiles:
        open(file, "w").close()
