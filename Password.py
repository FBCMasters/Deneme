import random
EskiParola = ("FBCMasters+FBC-/*!&$#?=@abcdefghijklnopqrstuvwxyzABBBBBCCCDEFFFFFFFFFFGHIJKLMNOPQRSTUVWXYZ1234567890FBCParolası")
istenenParola = (int(input("Şifre kaç harfli olsun?(En az 11):")))
YeniParola = ("FBCParolası")
for i in range(istenenParola-11):
    YeniParola += random.choice(EskiParola)
print("Yeni şifren:")
print(YeniParola)
