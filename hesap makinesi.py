import time
print("*"*30,"\n")
print("[1] Toplama")
print("[2] Çıkarma")
print("[3] Çarpma")
print("[4] Bölme")
print("[5] Üs alma")
print("[6] Karekök hesaplama")
print("[7] Karekökün hangi sayıya ait olduğunu bulma")
print("[Q] Uygulamayı kapat")
print()
print("*"*30)

#input komutu ile başlangıçta belirttiğimiz rakamlardan birini seçmesini istiyoruz.
giris = input("Lütfen 7 işlemden birini seçiniz: ") 
while True:
	if giris =="1":
		print("\nToplama işlemi seçildi")
		x = input("Birinci sayı: ")
		x = float(x)
		y = input("İkinci sayı: ")
		y = float(y)
		print("İşlem sonucu: ", x + y , "\n")
		continue
		time.sleep(5)
#Hesap makinesini kullanacak kişiler ondalıklı sayı (3,14) kullanmak isteyebilir. Bu yüzden değişkenlerimizi float olarak belirliyoruz.

	elif giris =="2":
		print("\n Çıkarma işlemi seçildi")
		x = input("Birinci sayı: ")
		x = float(x)
		y = input("İkinci sayı: ")
		y = float(y)
		print("İşlem sonucu", x - y, "\n")
		continue
		time.sleep(5)

	elif giris =="3":
		print("\n Çarpma işlemi seçildi")
		x = input("Birinci sayı: ")
		x = float(x)
		y = input("İkinci sayı: ")
		y = float(y)
		print("İşlem sonucu", x * y, "\n")
		continue
		time.sleep(5)

	elif giris =="4":
		print("\n Bölme işlemi seçildi")
		x = input("Birinci sayı: ")
		x = float(x)
		y = input("İkinci sayı: ")
		y = float(y)
		print("İşlem sonucu", x / y, "\n")
		continue
		time.sleep(5)

	elif giris =="5":
		print("\n Üs alma işlemi seçildi")
		x = input("Birinci sayı: ")
		x = float(x)
		y = input("İkinci sayı: ")
		y = float(y)
		print("İşlem sonucu", x ** y, "\n")
		continue
		time.sleep(5)

	elif giris =="6":
		print("\n Karekök hesaplama işlemi seçildi")
		x = input("Taban sayısı: ")
		x = float(x)
		print("İşlem sonucu: ", x*x)
		continue
		time.sleep(5)

	elif giris =="7":
		print("\n Karekökün hangi  sayıya ait olduğunu bulma işlemi seçildi")
		x = input("Karekök sayısı: ")
		x = int(x)
		print("İşlem sonucu: ", x**0.5)
		continue
		time.sleep(5)

	elif giris =="q" or giris == "Q":
		print("Hesap makinesi kapanıyor...")
		time.sleep(1)
		quit()

	else:
		print("Yanlış giriş yaptınız")
		time.sleep(1)
		print("Hesap makinesi kapanıyor...")
		time.sleep(1.5)
		break
