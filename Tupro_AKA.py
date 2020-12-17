from random import seed
from random import randint
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import time
import more_itertools 




#Comb Sort    
def combsort ( data ):
    length = len ( data ) #panjang list gap_value untuk comb_sort
    #shrink facktor sebenarnya bebas, tapi beberapa referensi menyebutkan angka terbaik adalah 1.3
    shrink_factor = 1.3 
    _gap = length
    angka = list ( data )
    sorted = False
    try:
        while not sorted :
            _gap /= shrink_factor
            gap = int ( _gap )
            if gap <= 1 : #Hentikan sort disaaat gap dibawah 
                sorted = True
                gap = 1
            for i in range ( length - gap ):
                sm = gap + i
                if angka [ i ] > angka [ sm ]:
                    angka [ i ], angka [ sm ] = angka [ sm ], angka [ i ]
                    sorted = False
                    nilai = list(angka)
                yield angka
            # starting time
            
    except StopIteration:
        pass
    
    
    
    
#Insertion Sort
def insertion_sort(angka):
    for i in range(1, len(angka)):
        j = i
        while j > 0 and angka[j] < angka[j - 1]:
            if j != j-1:
                angka[j], angka[j-1] = angka[j-1], angka[j]            
                j -= 1
                yield angka

def hasil_sort(angka):
    for i in range(1, len(angka)):
        j = i
        while j > 0 and angka[j] < angka[j - 1]:
            if j != j-1:
                angka[j], angka[j-1] = angka[j-1], angka[j]            
                j -= 1
    return angka

N = int(input("Jumlah Array: "))
# seed random number generator
seed(1)
angka = []
for i in range(N):
    value = randint(0, 100)
    angka.append(value) #tangkap random number dalam list
print("Angka acak adalah sebagai berikut\n : ",angka)


#Pilih algoritma
#pilih = "Pilih sorting:\n1. Comb Sort\n2. Insertion Sort\n"
#algoritma = input(pilih)
#if algoritma == "1":
#   title = "Comb sort"
#    hasil = combsort(angka)
#    print(hasil)
#elif algoritma == "2":
#   title = "Insertion sort"
#    hasil = insertion_sort(angka)
#    print(hasil)

start_time = time.time()
time.sleep(1)
title = "Comb sort"
hasil = combsort(angka)
#Visualisasi
fig, ax = plt.subplots()
ax.set_title(title)
bar_rects = ax.bar(range(len(angka)), angka, align="edge")
text = ax.text(0.02, 0.95, "", transform=ax.transAxes)
iteration = [0]

def update_fig(angka, rects, iteration):
    for rect, val in zip(rects, angka):
        rect.set_height(val)
    iteration[0] += 1
    text.set_text("# of operations: {}".format(iteration[0]))   
anim = animation.FuncAnimation(fig, func=update_fig,fargs=(bar_rects, iteration), frames=hasil,  repeat=False, )
plt.show


title1 = "Insertion sort"
hasil1 = insertion_sort(angka)
print(hasil1)
#Visualisasi
fig1, ax1 = plt.subplots()
ax1.set_title(title1)
bar_rects = ax1.bar(range(len(angka)), angka, align="edge")
text1 = ax1.text(0.02, 0.95, "", transform=ax.transAxes)
iteration = [0]
def update_fig1(angka, rects, iteration):
    for rect, val in zip(rects, angka):
        rect.set_height(val)
    iteration[0] += 1
    text1.set_text("# of operations: {}".format(iteration[0]))  
 
anim1 = animation.FuncAnimation(fig1, func=update_fig1,fargs=(bar_rects, iteration), frames=hasil1,  repeat=False, )
start_time2 = time.time()
time.sleep(1)
plt.show()




#print("Sorting Comb Sort:")
#hasil = list(hasil)
#result = next(more_itertools.islice_extended(hasil, N-2))
#print("Hasil: ",result)
hasil_akhir= hasil_sort(angka)
print("Hasil Akhir Sorting",hasil_akhir)

#print("Sorting Insertion Sort:")
#hasil1 = list(hasil1)
#result = next(more_itertools.islice_extended(hasil1, N-29))
#print("Hasil: ",result)
print("Comb Sort %s seconds: " % (time.time() - start_time))
print("Insertion Sort %s seconds: " % (time.time() - start_time2))
