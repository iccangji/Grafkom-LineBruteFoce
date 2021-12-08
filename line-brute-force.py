""" TUGAS GRAFKOM
MEMBENTUK GARIS DENGAN ALGORITMA BRUTE FORCE
E1E120036   MUH. NUR IKSAN
E1E120012   LILY APRILYANI. S
E1E120056	AGENG ARYA KHRYSNA DWIPANGGA
E1E120074	JAKA MESA'I SAPUTRA
E1E120088	NURJALNI
E1E120104	ZALDA NINGRATI """

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import TextBox

fig, ax = plt.subplots() #membuat sublot figur dan sumbu
plt.suptitle('Membentuk Garis Dengan Algoritma Brute Force') #judul figur
plt.subplots_adjust(bottom=0.2)
x = np.array([3,9]) #array titik awal sumbu x
y = np.array([1,5]) #array titik awal sumbu y

def connect(): #function menentukan dan menapilkan titik
    ax.cla() #membersihkan grafik
    ax.grid() #menambahkan garis-garis pada grafik
    
    global x,y,l0,l1,m #membuat variabel pada function menjadi global

    xline,yline = [],[] #membuat array untuk titik penghubung
    m = 0#variabel gradien
    if x[0]==x[1]: #jika x1=x2
        p = y[0]
        if y[0]>y[1]:#jika x1>x2
            p = y[1]
        xline = np.append(x,x[0])#menambahakan titik penghubung sumbu x
        yline = np.append(y,p+1)#menambahakan titik penghubung sumbu y
    elif y[0]==y[1]:#jika y1=y2
        m = np.Infinity
        p = x[0]
        if x[0]>x[1]:
            p = y[1]
        xline = np.append(x,(x[0])+1)
        yline = np.append(y,y[1])
    else:
        if m<1:#jika gradien < 1
            m = (y[1]-y[0])/(x[1]-x[0])#gradien = (y2-y1)/(x2-x1)
            n = abs(x[1]-x[0])#n = x2-x1
            x2 = x[0]#x = x1
            i = 1
            while i <= n+1: #iterasi untuk menentukan titik penghubung
                y2 = y[0]+m*(x2-x[0])
                xline.append(x2)
                yline.append(round(y2))
                x2+=1
                i+=1
        else:#jika gradien > 1
            m = (x[1]-x[0])/(y[1]-y[0])
            n = abs(y[1]-y[0])
            y2 = y[0]
            i = 1
            while i <= n+1:
                x2 = x[0]+m*(y2-y[0])
                yline.append(y2)
                xline.append(round(x2))
                y2+=1
                i+=1
    np.array(xline) #mengubah array menjadi array numpy
    np.array(yline)
    print('Titik Koordinat: (', x[0], ',',y[0],') (',x[1],',',y[1],')')#Menampilkan titik koordinat di terminal
    print('Titik Penghubung: ',end=' ')#Menampilkan titik penghubung di terminal
    for i in range (len(xline)):#iterasi untuk menampilkan titk penghubung
        if i < len(xline)-1:
            print('(',xline[i],',', yline[i],end='),')
        else:
            print('(',xline[i],',',yline[i],end=')')
    print()
    print('Gradien = ',m)
    print()

    l0, = ax.plot(xline, yline ,'o')#Menampilkan titik penghubng
    l1, = ax.plot(x, y)#Menampilkan garis penghubung

    l0.set_label('Titik Penghubung')#Menampilkan keterangan
    l1.set_label('Garis Penghubung')
    ax.legend()
    
def submit(text):#function untuk input titik koordinat
    data = eval(text)#mengubah string menjadi tuple
    x[0],x[1] = data[0][0],data[1][0]#memasukkan input ke array
    y[0],y[1] = data[0][1],data[1][1]
    l0.set_data(x,y)#mengubah titik koordinat pada grafik
    l1.set_data(x,y)
    ax.autoscale_view()
    connect()
    
connect()

axbox = plt.axes([0.2, 0.05, 0.2, 0.05]) #letak input titik koordinat
text_box = TextBox(axbox, 'Titik Koordinat', initial='(3,1),(9,5)') #menampilkan kolom input
text_box.on_submit(submit) #trigger ke function submit

plt.show()
