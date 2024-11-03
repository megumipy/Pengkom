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
        side_h = 2
        print("="*(22))
        while side_h>=0:
            side_v = 20
            while side_v>0:
                if side_h == 2:
                    if side_v == 20 or side_v == 2:
                        print("||", end='')
                    elif side_v == 1:
                        print(' ')
                    elif side_v == 19:
                        print("Smart",end='')
                    elif side_v<16:
                        print(' ', end='')
                elif side_h == 1:
                    if side_v == 20 or side_v == 2:
                        print("||", end='')
                    elif side_v == 1:
                        print(' ')
                    elif side_v == 19:
                        print("Microwave",end='')
                    elif side_v<12:
                        print(' ', end='')
                elif side_h == 0:
                    if side_v == 20:
                        print("||", end='')
                    elif side_v == 1:
                        print("||")
                    else:
                        print(' ', end='')  
                side_v-=1
            side_h-=1
        print("="*(22))
    def display2(self):
        side_h = 2
        print("="*(22))
        while side_h>=0:
            side_v = 20
            while side_v>0:
                if side_h == 2:
                    if self.temp<10:
                        space = 12
                    elif self.temp <100:
                        space = 11
                    else:
                        space = 10
                        
                    if side_v == 20 or side_v == 2:
                        print("||", end='')
                    elif side_v == 1:
                        print(' ')
                    elif side_v == 19:
                        print(f'Suhu: {self.temp}°C', end='')
                    elif side_v<space:
                        print(' ', end='')
                elif side_h == 1:
                    if self.moisture<10:
                        space = 7
                    elif self.moisture <100:
                        space = 6
                    else:
                        space = 5
                        
                    if side_v == 20 or side_v == 2:
                        print("||", end='')
                    elif side_v == 1:
                        print(' ')
                    elif side_v == 19:
                        print(f'Kelembapan: {int(round(self.moisture, 0))}%', end='')
                    elif side_v<space:
                        print(' ', end='') 
                elif side_h == 0:
                    if self.time<600:
                        space = 5
                    else:
                        space = 4
                        
                    if side_v == 20 or side_v == 2:
                        print("||", end='')
                    elif side_v == 1:
                        print(' ')
                    elif side_v == 19:
                        print(f'Sisa Waktu: {int((self.time/60))}:00', end='')
                    elif side_v<space:
                        print(' ', end='')   
                side_v-=1
            side_h-=1
        print("="*(22))
    def displayover():
        side_h = 2
        print("="*(22))
        while side_h>=0:
            side_v = 20
            while side_v>0:
                if side_h == 1:
                    if side_v == 20 or side_v == 2:
                        print("||", end='')
                    elif side_v == 1:
                        print(' ')
                    elif side_v == 14:
                        print("Overheat",end='')
                    elif (side_v<20 and side_v>14) or side_v<8:
                        print(' ', end='')
                else:
                    if side_v == 20:
                        print("||", end='')
                    elif side_v == 1:
                        print("||")
                    else:
                        print(' ', end='')  
                side_v-=1
            side_h-=1
        print("="*(22))
    def displaydry():
        side_h = 2
        print("="*(22))
        while side_h>=0:
            side_v = 20
            while side_v>0:
                if side_h == 1:
                    if side_v == 20 or side_v == 2:
                        print("||", end='')
                    elif side_v == 1:
                        print(' ')
                    elif side_v == 15:
                        print("Kering Wak",end='')
                    elif (side_v<20 and side_v>15) or side_v<7:
                        print(' ', end='')
                else:
                    if side_v == 20:
                        print("||", end='')
                    elif side_v == 1:
                        print("||")
                    else:
                        print(' ', end='')  
                side_v-=1
            side_h-=1
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
