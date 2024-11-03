class comp:
    def __init__(self, time:int, temp:int, moisture:int):
        self.time = time*60
        self.temp = temp
        self.moisture = moisture
    def moisture1(self, limit):
        if self.moisture >= limit:
            while self.time > 0:
                self.moisture = self.moisture - (self.temp/1200)
                if self.moisture <= limit:
                    break
                self.time -= 1

class mode(comp):
    def __init__(self, time, temp, moisture):
        super().__init__(time, temp, moisture)
    def quick_heat(self):
        comp.moisture1(self, 40)
        Microwave.display2(self)
        return print(f'Selamat menikmati!!')
    def Deforst(self):
        comp.moisture1(self, 60)
        Microwave.display2(self)
        return print(f'Selamat menikmati!!')
    def Grill(self):
        comp.moisture1(self, 30)
        Microwave.display2(self)
        return print(f'Selamat menikmati!!')

class vegetable(comp):
    def __init__(self, time, temp, moisture):
        super().__init__(time, temp, moisture)
    def menu():
        print(" 1. brokoli")
        print(" 2. wortel\n 3. kembang kol\n 4. bayam")
        print(" 5. jagung manis\n 6. paprika")
        print(" 7. zucchini")
    def brokoli(self):
        comp.moisture1(self, 70)
        Microwave.display2(self)
        return print(f'Selamat menikmati!!')
    def wortel(self):
        comp.moisture1(self, 60)
        Microwave.display2(self)
        return print(f'Selamat menikmati!!')
    def kembang_kol(self):
        comp.moisture1(self, 70)
        Microwave.display2(self)
        return print(f'Selamat menikmati!!')
    def bayam(self):
        comp.moisture1(self, 80)
        Microwave.display2(self)
        return print(f'Selamat menikmati!!')
    def jagung_manis(self):
        comp.moisture1(self, 70)
        Microwave.display2(self)
        return print(f'Selamat menikmati!!')
    def paprika(self):
        comp.moisture1(self, 60)
        Microwave.display2(self)
        return print(f'Selamat menikmati!!')
    def zucchini(self):
        comp.moisture1(self, 70)
        Microwave.display2(self)
        return print(f'Selamat menikmati!!')

class seafood(comp):
    def __init__(self, time, temp, moisture):
        super().__init__(time, temp, moisture)
    def menu():
        print(" 1. Ikan fillet")
        print(" 2. Udang")
        print(" 3. Cumi-cumi")
        print(" 4. Kerang")
        print(" 5. Lobster")
    def fish(self):
        comp.moisture1(self, 70)
        Microwave.display2(self)
        return print(f'Selamat menikmati!!')
    def shrimp(self):
        comp.moisture1(self, 75)
        Microwave.display2(self)
        return print(f'Selamat menikmati!!')
    def squid(self):
        comp.moisture1(self, 70)
        Microwave.display2(self)
        return print(f'Selamat menikmati!!')
    def shellfish(self):
        comp.moisture1(self, 70)
        Microwave.display2(self)
        return print(f'Selamat menikmati!!')
    def lobster(self):
        comp.moisture1(self, 70)
        Microwave.display2(self)
        return print(f'Selamat menikmati!!')
class Microwave(comp):
    def __init__(self, time, temp, moisture):
        super().__init__(time, temp, moisture)
    def display1():
        b = 2
        print("="*(22))
        while b>=0:
            a = 20
            while a>0:
                if b == 2:
                    if a == 20 or a == 2:
                        print("||", end='')
                    elif a == 1:
                        print(' ')
                    elif a == 19:
                        print("Smart",end='')
                    elif a<16:
                        print(' ', end='')
                elif b == 1:
                    if a == 20 or a == 2:
                        print("||", end='')
                    elif a == 1:
                        print(' ')
                    elif a == 19:
                        print("Microwave",end='')
                    elif a<12:
                        print(' ', end='')
                elif b == 0:
                    if a == 20:
                        print("||", end='')
                    elif a == 1:
                        print("||")
                    else:
                        print(' ', end='')  
                a-=1
            b-=1
        print("="*(22))
    def display2(self):
        b = 2
        print("="*(22))
        while b>=0:
            a = 20
            while a>0:
                if b == 2:
                    if self.temp<10:
                        c = 12
                    elif self.temp <100:
                        c = 11
                    else:
                        c = 10
                        
                    if a == 20 or a == 2:
                        print("||", end='')
                    elif a == 1:
                        print(' ')
                    elif a == 19:
                        print(f'Suhu: {self.temp}°C', end='')
                    elif a<c:
                        print(' ', end='')
                elif b == 1:
                    if self.moisture<10:
                        c = 7
                    elif self.moisture <100:
                        c = 6
                    else:
                        c = 5
                        
                    if a == 20 or a == 2:
                        print("||", end='')
                    elif a == 1:
                        print(' ')
                    elif a == 19:
                        print(f'Kelembapan: {int(round(self.moisture, 0))}%', end='')
                    elif a<c:
                        print(' ', end='') 
                elif b == 0:
                    if self.time<600:
                        c = 5
                    else:
                        c = 4
                        
                    if a == 20 or a == 2:
                        print("||", end='')
                    elif a == 1:
                        print(' ')
                    elif a == 19:
                        print(f'Sisa Waktu: {int((self.time/60))}:00', end='')
                    elif a<c:
                        print(' ', end='')   
                a-=1
            b-=1
        print("="*(22))
    def displayover():
        b = 2
        print("="*(22))
        while b>=0:
            a = 20
            while a>0:
                if b == 1:
                    if a == 20 or a == 2:
                        print("||", end='')
                    elif a == 1:
                        print(' ')
                    elif a == 14:
                        print("Overheat",end='')
                    elif (a<20 and a>14) or a<8:
                        print(' ', end='')
                else:
                    if a == 20:
                        print("||", end='')
                    elif a == 1:
                        print("||")
                    else:
                        print(' ', end='')  
                a-=1
            b-=1
        print("="*(22))
    def displaydry():
        b = 2
        print("="*(22))
        while b>=0:
            a = 20
            while a>0:
                if b == 1:
                    if a == 20 or a == 2:
                        print("||", end='')
                    elif a == 1:
                        print(' ')
                    elif a == 15:
                        print("Kering Wak",end='')
                    elif (a<20 and a>15) or a<7:
                        print(' ', end='')
                else:
                    if a == 20:
                        print("||", end='')
                    elif a == 1:
                        print("||")
                    else:
                        print(' ', end='')  
                a-=1
            b-=1
        print("="*(22))
    def menu():
        print(" 1. Start")
        print(" 2. Quick Heat\n 3. Deforst\n 4. Grill")
        print(" 5. Vegetable\n 6. Seafood")
        print(" 7. Cleaning")
        print(" 0. Stop")
        print(" 99. Child Lock")
    def Start():
        Microwave.display1()
        while True:
            Microwave.menu()
            chioce = int(input("Pilih menu : "))
            
            if chioce == 1:
                time = int(input("Masukan waktu Memasak(menit) : "))
                temp = int(input("Masukan Temperatur(°C) : "))
                moisture = 100
                food = Microwave(time, temp, moisture)
                food.moisture1(0)
                if food.moisture < 1:
                    Microwave.displaydry()
                elif food.moisture < 40:
                    Microwave.displayover()
                food.display2()
            elif chioce == 2:
                food = mode(2, 150, 90)
                food.quick_heat()
            elif chioce == 3:
                food = mode(8, 40, 90)
                food.Deforst()
            elif chioce == 4:
                food = mode(20, 230, 100)
                food.Grill()
            elif chioce == 5:
                while True:
                    vegetable.menu()
                    sayur = int(input("Pilih Sayur : "))
                    if sayur == 1:
                        vegen = vegetable(2, 200, 100)
                        vegen.brokoli()
                        break
                    elif sayur == 2:
                        vegen = vegetable(5, 200, 100)
                        vegen.wortel()
                        break
                    elif sayur == 3:
                        vegen = vegetable(4, 200, 100)
                        vegen.kembang_kol()
                        break
                    elif sayur == 4:
                        vegen = vegetable(3, 200, 100)
                        vegen.bayam()
                        break
                    elif sayur == 5:
                        vegen = vegetable(5, 200, 100)
                        vegen.jagung_manis()
                        break
                    elif sayur == 6:
                        vegen = vegetable(4, 200, 100)
                        vegen.paprika()
                        break
                    elif sayur == 7:
                        vegen = vegetable(4, 200, 100)
                        vegen.zucchini()
                        break
            elif chioce == 6:
                while True:
                    seafood.menu()
                    seaf = int(input("Pilih Seafood : "))
                    if seaf == 1:
                        ikan = seafood(5, 90, 100)
                        ikan.fish()
                        break
                    elif seaf == 2:
                        udang = seafood(3, 80, 100)
                        udang.shrimp()
                        break
                    elif seaf == 3:
                        cumi = seafood(3, 80, 100)
                        cumi.squid()
                        break
                    elif seaf == 4:
                        kerang = seafood(4, 80, 100)
                        kerang.shellfish()
                        break
                    elif seaf == 5:
                        lobster = seafood(7, 90, 100)
                        lobster.lobster()
                        break
            elif chioce == 7:
                Microwave.display1()
                print("Microwave telah dibersikan")
            elif chioce == 0:
                break

Microwave.Start()       
        
        
    