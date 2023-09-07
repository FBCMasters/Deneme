import random

def MakePassword(istenenParola):
    EskiParola = "FBCMasters+FBC-/*!&$#?=@abcdefghijklnopqrstuvwxyzABBBBBCCCDEFFFFFFFFFFGHIJKLMNOPQRSTUVWXYZ1234567890FBCParolası"
#    istenenParola = (int(input("Şifre kaç harfli olsun?(En az 11):")))
    YeniParola = "HackedPassword"
#                "FBCParolası"
    for i in range(istenenParola-14):
        YeniParola += random.choice(EskiParola)
    return YeniParola

def RandomEmoji():
    Emojiler = [":slight_smile:", " :slight_frown:", ":rage:", ":neutral_face:", ":open_mouth:"]
    return random.choice(Emojiler)

def SecretEmoji():
    SecretEms = [":smiling_imp:", " :imp:", ":rage:", ":dizzy_face:", ":face_with_symbols_over_mouth:", ":japanese_ogre:", ":japanese_goblin:", ":ghost:", ":skull:", ":skull_crossbones:", ":alien:"]
    return random.choice(SecretEms)

def YazıTura(Fiyat):
    Para = ["Yazı", "Tura"]
    Cevap = random.choice(Para)
    if Fiyat == Cevap:
        return (Cevap+" Kazandın!"+":slight_smile:")
    elif Fiyat != Cevap:
        return (Cevap+" Kaybettin"+":slight_frown:")

def TaşKağıtMakas(İlkEl):
    El = ["Taş", "Kağıt", "Makas"]
    SonEl = random.choice(El)
    if SonEl == "Taş":
        if İlkEl == "Kağıt":
            return (SonEl+" Kazandın!"+":slight_smile:")
        elif İlkEl == "Makas":
            return (SonEl+" Kaybettin"+":slight_frown:")
    elif SonEl == "Kağıt":
        if İlkEl == "Makas":
            return (SonEl+" Kazandın!"+":slight_smile:")
        elif İlkEl == "Taş":
            return (SonEl+" Kaybettin"+":slight_frown:")
    elif SonEl == "Makas":
        if İlkEl == "Taş":
            return (SonEl+" Kazandın!"+":slight_smile:")
        elif İlkEl == "Kağıt":
            return (SonEl+" Kaybettin"+":slight_frown:")
    elif SonEl == İlkEl:
        return (SonEl+"Berabere"+":neutral_face:")
    else:
        return("Örnek:"+SonEl+"   <-- Böyle Yapmalıydın!"+":rage:")

def double(str):
    # Sonuç
    result = ''
    for letter in str:
        result += letter * 2
    return result

def secret_command(a, b):
    if a == 1:
        a = 10
    elif a == 2:
        a = 20
    elif a == 3:
        a = 30
    elif a == 5:
        a = 50
    elif a == 6:
        a = 60
    elif a == 7:
        a = 70
    elif a == 8:
        a = 80
    elif a == 9:
        a = 90
    return a+b

#def random_AmongUs():
#    Amugus = ['Images/AmongUs/Amogus.gif', 'Images/AmongUs/aMUGus.jpg', 'Images/AmongUs/SUSs.gif']
#    return random.choice(Amugus)
