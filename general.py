file = open("C:\\Users\\hp\\OneDrive\\Documents\\Belajar Pemrograman\\JAVA PBO\\TBO\\FP TBO\\Real TBO Deva\\word\\verb.txt", "r")
kata_kerja = file.read().split("\n")
file.close()
file = open("C:\\Users\\hp\\OneDrive\\Documents\\Belajar Pemrograman\\JAVA PBO\\TBO\\FP TBO\\Real TBO Deva\\word\\noun.txt", "r")
kata_benda = file.read().split("\n")
file.close()
file = open("C:\\Users\\hp\\OneDrive\\Documents\\Belajar Pemrograman\\JAVA PBO\\TBO\\FP TBO\\Real TBO Deva\\word\\adj.txt", "r")
kata_sifat = file.read().split("\n")
file.close()
file = open("C:\\Users\\hp\\OneDrive\\Documents\\Belajar Pemrograman\\JAVA PBO\\TBO\\FP TBO\\Real TBO Deva\\word\\adv.txt", "r")
kata_keterangan = file.read().split("\n")
file.close()
file = open("C:\\Users\\hp\\OneDrive\\Documents\\Belajar Pemrograman\\JAVA PBO\\TBO\\FP TBO\\Real TBO Deva\\word\\num.txt", "r")
numeralia = file.read().split("\n")
file.close()
file = open("C:\\Users\\hp\\OneDrive\\Documents\\Belajar Pemrograman\\JAVA PBO\\TBO\\FP TBO\\Real TBO Deva\\word\\prep.txt", "r")
preposisi = file.read().split("\n")
file.close()
file = open("C:\\Users\\hp\\OneDrive\\Documents\\Belajar Pemrograman\\JAVA PBO\\TBO\\FP TBO\\Real TBO Deva\\word\\prop_noun.txt", "r")
proper_noun = file.read().split("\n")
file.close()
file = open("C:\\Users\\hp\\OneDrive\\Documents\\Belajar Pemrograman\\JAVA PBO\\TBO\\FP TBO\\Real TBO Deva\\word\\pronoun.txt", "r")
kata_ganti = file.read().split("\n")

file.close()

alphabet = kata_kerja + kata_benda + kata_sifat + kata_keterangan + numeralia + preposisi + proper_noun + kata_ganti

def check_alphabet(array): # Ngecek apakah setiap kata dari string yang diinput ada atau tidak di alphabet
    for i in array:
        if i not in alphabet:
            print(i)
            return False
    return True
