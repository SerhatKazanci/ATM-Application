def atm():

    sifre = "1234"
    hak = 3
    while True:
        hak -= 1
        girisSifre = input("Şifre giriniz = ")

        if sifre == girisSifre:
            bakiye = 5000
            while True:
                print("""İşlemler:
1 - Para çekme
2 - Para yatırma
3 - Şifre değiştirme
4 - Çıkış""")
                islem = int(input("Yapmak istediğiniz işlemi yazınız = "))
                if islem == 1:
                    # amaç diyelim 10000 çekmek istedin yetersiz bir üst listeye çıkmdan tekrar bu döngüğ aiçinde dyuryrtır
                    while True:
                        cek = int(
                            input("Çekmek istediğiniz miktarı yazınız = "))
                        if cek > bakiye:
                            print("Yetersiz bakiye..")
                            print("Lütfen Bakiyenizin Altında Giriniz!")
                        else:
                            bakiye -= cek
                            print("Güncel Bakiyeniz =", bakiye)
                            break

                elif islem == 2:
                    hesap = input("Hesap Numarası Giriniz = ")

                    if len(hesap) == 11:
                        hesap = input(
                            "Yatırılacak Para Miktarını Açılan Yere Yerleştiriniz ve ENTER Tuşuna Basınız !")
                        print("Paranız Tanımlanıyor.... ")

                        print("Paranız Tanımlandı.... ")
                        hesap = input(
                            "Para Yatırma İşleminiz Onaylıyor Musunuz =")

                        if hesap == 'Evet':
                            print("Paranız  Yatırıldı")
                            print("Güncel bakiyeniz =", bakiye)

                        elif hesap == 'Geri':
                            print("İşleminiz İptal Edildi")
                            islem = input("Yapacağınız İşlemi Seçiniz = ")

                        else:
                            print("İşlem Süreniz Dolmak Üzere Tuşlama Yapınız")
                            hesap = input(
                                "Para Yatırma İşleminiz Onaylıyor Musunuz =")

                    else:
                        print("Hesap Numarasını Eksik Girdiniz!")
                        hesap = input("Hesap Numarası Tekrar Giriniz = ")

                elif islem == 3:
                    while True:
                        yenisifre = input("4 Haneli Yeni Şifrenizi Giriniz = ")

                        if len(yenisifre) == 4:

                            if yenisifre == sifre:
                                print("Şifreniz Önceki Şifreyle Aynı Olamaz")
                                yenisifre = input(
                                    "4 Haneli Yeni Şifrenizi Giriniz = ")
                                sifre = yenisifre
                                print("Şifreniz Başarıyla Gerçekleşmiştir")
                                break

                            else:
                                yenisifre = input(
                                    "4 Haneli Yeni Şifrenizi Tekrar Giriniz = ")
                                print("Şifreniz Başarıyla Gerçekleşmiştir")
                                break
                        else:
                            yenisifre = input(
                                "Lütfen Şifrenizi 4 Haneli Olacak Şekilde Giriniz Devam Etmek İçin ENTER Basınız ")
                elif islem == 4:
                    print("Menüden çıkış yapmak için enter'a basınız")
                    print("Çıkış Yapılıyor Kartınızı Alınız")
                    print("İyi Günler Dileriz..")
                    break

        elif girisSifre == "":
            print("Çıkış yapılıyor..")
            break

        elif hak == 0:
            print("şifre bloke olmuştur Müşteri Hizmetlerini Arayınız")
            break
        else:
            print("Şifre hatalı..", hak)


atm()
