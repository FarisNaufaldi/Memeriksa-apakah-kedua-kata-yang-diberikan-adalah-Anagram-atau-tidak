def anagram(x,y):
    x = x.lower()
    y = y.lower()
    if set(x) == set(y):
        print("Ini adalah anagram")
    else:
        print("Ini bukanlah anagram")

kata_pertama = input("Masukkan kata pertama yang anda inginkan = ")
kata_kedua = input("Masukkan kata kedua yang anda inginkan = ")
anagram(kata_pertama,kata_kedua)