import pygame
import sys
import random
#Teclas de control
#D = derecha , A= izquierda , W= arriba , S=abajo , Tabulador =Saltar
#F=correr , R=lanzar Bomba , M = Lanazar manotazoa
#Iniciación de Pygame
#Iniciación de Pygame
pygame.init()

#Pantalla - ventana
W, H = 800, 600
PANTALLA = pygame.display.set_mode((W, H))
pygame.display.set_caption('Sonic-Bean')
icono=pygame.image.load('imagenes/1.png')
pygame.display.set_icon(icono)

b=pygame.sprite.Sprite()
b.image=pygame.image.load("imagenes/Bean1.png").convert_alpha()
E=pygame.sprite.Sprite()
E.image=pygame.image.load("imagenes/eneminos.png").convert_alpha()
B=pygame.sprite.Sprite()
#Lansar bomba

y10=b.image.subsurface((177 ,55 , 42 , 47))
y20=b.image.subsurface((66 , 256 ,38 ,45))
y30=b.image.subsurface((105 ,256, 41,  46))
y40=b.image.subsurface((151, 266, 24,  24))
y50=b.image.subsurface((176, 267, 17,  23))
y60=b.image.subsurface((176, 267, 17,  23))
y70=b.image.subsurface((176, 267, 17,  23))
y80=b.image.subsurface((176, 267, 17,  23))
BeanB = []
BeanB.append(y10)
BeanB.append(y20)
BeanB.append(y30)
BeanB.append(y40)
BeanB.append(y50)
BeanB.append(y60)
BeanB.append(y70)
BeanB.append(y80)
#Lansar manotazo
284, 156, 40,  50
214, 205, 40,  50
239, 157, 40 , 47
162, 206, 42,  46
182, 155, 40,  47
y11=b.image.subsurface((284, 156, 40,  50))
y21=b.image.subsurface((214, 205, 40,  50))
y31=b.image.subsurface((239, 157, 40 , 47))
y41=b.image.subsurface((162, 206, 42,  46))
y51=b.image.subsurface((182, 155, 40,  47))
y61=b.image.subsurface((182, 155, 40,  47))
y71=b.image.subsurface((182, 155, 40,  47))
y81=b.image.subsurface((182, 155, 40,  47))
BeanB1 = []
BeanB1.append(y11)
BeanB1.append(y21)
BeanB1.append(y31)
BeanB1.append(y41)
BeanB1.append(y51)
BeanB1.append(y61)
BeanB1.append(y71)
BeanB1.append(y81)


#enemigo



z1=E.image.subsurface((112 ,1262   ,60 , 32))
z2=E.image.subsurface((177 ,1263   ,46 , 30))
z3=E.image.subsurface((28  ,1300    ,53 , 36))
z4=E.image.subsurface((85  ,1301   , 56,  39))
z5=E.image.subsurface((147 ,1295   , 57 , 47))
z6=E.image.subsurface((211 ,1302   , 56 , 36))
z7=E.image.subsurface((269 ,1304   , 54 , 34))
z8=E.image.subsurface((325 ,1304   , 52 , 41))
Enem = []
Enem.append(z1)
Enem.append(z2)
Enem.append(z3)
Enem.append(z4)
Enem.append(z5)
Enem.append(z6)
Enem.append(z7)
Enem.append(z8)


z10=E.image.subsurface((318, 744, 60,  51))
z20=E.image.subsurface((380, 743, 54,  52))
z30=E.image.subsurface((436, 737, 45,  58))
Enem1 = []
Enem1.append(z10)
Enem1.append(z20)
Enem1.append(z30)

#Caminar
y1=b.image.subsurface((2  , 8  , 33 , 52))
y2=b.image.subsurface((40 , 8  , 34 , 52))
y3=b.image.subsurface((82 , 8  , 32 , 52))
y4=b.image.subsurface((123, 8  , 35 , 52))
y5=b.image.subsurface((163, 8  , 44 , 52))
y6=b.image.subsurface((211, 8  , 26 , 52))
y7=b.image.subsurface((252, 8  , 33 , 52))
y8=b.image.subsurface((295, 8 ,  45 , 52))
BeanC = []
BeanC.append(y1)
BeanC.append(y2)
BeanC.append(y3)
BeanC.append(y4)
BeanC.append(y5)
BeanC.append(y6)
BeanC.append(y7)
BeanC.append(y8)
#correr

y01=b.image.subsurface((300, 5 ,  37,  47))
y02=b.image.subsurface((6  , 57  ,36,  45))
y03=b.image.subsurface((49 , 55 , 39 , 47))
y04=b.image.subsurface((223, 54 , 42 , 50))
y05=b.image.subsurface((223, 54 , 42 , 50))
y06=b.image.subsurface((223, 54 , 42 , 50))
y07=b.image.subsurface((223, 54 , 42 , 50))
y08=b.image.subsurface((223, 54 , 42 , 50))
BeanR = []
BeanR.append(y01)
BeanR.append(y02)
BeanR.append(y03)
BeanR.append(y04)
BeanR.append(y05)
BeanR.append(y06)
BeanR.append(y07)
BeanR.append(y08)




#Fondo del juego
fondo = pygame.image.load('imagenes/fondos/41.png')

#Música de fondo
pygame.mixer.music.load('sonido/sonic-sth.mp3')
pygame.mixer.music.play(-1)






#Personaje
quieto = pygame.image.load('imagenes/1.png')
daño = pygame.image.load('imagenes/daño.png')
gameover = pygame.image.load('imagenes/gameover.png')



x=0
px = 50
py = 500
ancho = 40
velocidad = 10

#Control de FPS
reloj = pygame.time.Clock()

#Variables salto
salto = False
#Contador de salto
cuentaSalto = 10

#Variables dirección
izquierda = False
derecha = False
correr = False
bomba = False
manotazo = False
#Pasos
cuentaPasos = 0
k=1
m=1
yy=450
Bon=0
M=0
ref=0
ref2=0
aumento=0
fondoUlt=0
#Movimiento
def recargaPantalla():
    #Variables globales
    global cuentaPasos
    global x
    global k,m
    global yy
    global Bon
    global M,ref,ref2,aumento,fondoUlt

     

    #Fondo en movimiento
    if derecha == True or correr == True or izquierda == True:
        x_relativa = x % fondo.get_rect().width
    
        PANTALLA.blit(fondo, (x_relativa - fondo.get_rect().width, 0))
        if x_relativa <= W :
            PANTALLA.blit(fondo, (x_relativa, 0))
            fondoUlt=x_relativa
        x -= 2
    else:
        x_relativa = x % fondo.get_rect().width
        PANTALLA.blit(fondo, (x_relativa - fondo.get_rect().width, 0))
        if x_relativa <= W :
            PANTALLA.blit(fondo, (fondoUlt, 0))
        



    #Enemigo
    k=k+1
    m=m+1

    salida=random.randint(200,300)

    if k%1==0 and m>24:

        PANTALLA.blit(Enem[k%8], (800-m-24, yy))

        if m==800:
            m=random.randint(10,20)
            yy=random.randint(200,600)

    if k%1==0 :
        if k%3==0:
            
            PANTALLA.blit(Enem1[0], (800-k*2, 500))
        elif k%3==1:
            
            PANTALLA.blit(Enem1[1], (800-k*2, 500))
        elif k%3==2:
            
            PANTALLA.blit(Enem1[2], (800-k*2, 500))

        if k==400:
            k=0


            

    #Bomba
    if bomba == True :
        PANTALLA.blit(BeanB [7], (int(px)+10, int(py)))
        ref=int(py)
        ref2=int(px)
        M=1
    elif M==1 and bomba == False and ref2+aumento< 800:
        aumento+=5
        PANTALLA.blit(BeanB [7], (ref2+aumento, ref))
    else:
        aumento=0
        M=0
    
        


    #Contador de pasos
    if cuentaPasos + 1 >= 8:
        cuentaPasos = 0
    

    #Movimiento a la izquierda
    

    if izquierda:
        inv=pygame.transform.flip(BeanC[cuentaPasos//1], True, False)
        PANTALLA.blit(inv, (int(px), int(py)))
        
        cuentaPasos += 1

        # Movimiento a la derecha
    elif derecha:
        PANTALLA.blit(BeanC[cuentaPasos//1], (int(px), int(py)))
        cuentaPasos += 1
        #Movimiento corriendo
    elif correr :
        
        PANTALLA.blit(BeanR[cuentaPasos//1], (int(px), int(py)))
        cuentaPasos += 1
        #Movimiento Bomba
    elif bomba :
        PANTALLA.blit(BeanB[cuentaPasos//1], (int(px), int(py)))
        cuentaPasos += 1
        #Movimiento manotazo
    elif manotazo :

        PANTALLA.blit(BeanB1[cuentaPasos//1], (int(px), int(py)))
        cuentaPasos += 1

    elif salto + 1 >= 2:
        PANTALLA.blit(BeanC[cuentaPasos//1] , (int(px), int(py)))
        cuentaPasos += 1

    else:
        PANTALLA.blit(quieto,(int(px), int(py)))

    #Game over 42 113

    if int(px)==800-k*2 and int(py)== 500:
        PANTALLA.blit(daño,(int(px), int(py)))
        PANTALLA.blit(gameover,(200, 200))
        cuentaPasos = 0
    
    

    elif int(px)==800-m-24 and int(py)== yy:
        PANTALLA.blit(daño,(int(px), int(py)))
        PANTALLA.blit(gameover,(200, 200))
        cuentaPasos = 0
    
      
        



ejecuta = True


#Bucle de acciones y controles
while ejecuta:
    

    if correr:
        FPS=100
    else:
        FPS =18



    reloj.tick(FPS)


    #Bucle del juego
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            ejecuta = False

    #Opción tecla pulsada
    keys = pygame.key.get_pressed()

    #Tecla A - Moviemiento a la izquierda
    if keys[pygame.K_a] and px > velocidad:
        px -= velocidad
        izquierda = True
        derecha = False
        correr = False
        bomba = False
        manotazo = False

    #Tecla D - Moviemiento a la derecha
    elif keys[pygame.K_d] and px < 900 - velocidad - ancho:
        px += velocidad
        izquierda = False
        derecha = True
        correr = False
        bomba = False
        manotazo = False
    #Tecla F - Moviemiento corriendo
    elif keys[pygame.K_f] and px < 900 - velocidad - ancho:
        
        px += velocidad
        izquierda = False
        derecha = False
        correr = True
        bomba = False
        manotazo = False
    #Tecla R - Moviemiento corriendo
    elif keys[pygame.K_r] and px < 900 - velocidad - ancho:
        
        px += velocidad
        izquierda = False
        derecha = False
        correr = False
        bomba = True
        manotazo = False
    # Tecla M - manotazo
    elif keys[pygame.K_m] and px < 900 - velocidad - ancho:
        
        px += velocidad
        izquierda = False
        derecha = False
        correr = False
        bomba = False
        manotazo = True


    #Personaje quieto
    else:
        izquierda = False
        derecha = False
        correr = False
        bomba = False
        cuentaPasos = 0

    #Tecla W - Moviemiento hacia arriba
    if keys[pygame.K_w] and py > 440:
        py -= velocidad

    #Tecla S - Moviemiento hacia abajo
    if keys[pygame.K_s] and py < 520:
        py += velocidad
    #Tecla SPACE - Salto
    if not (salto):
        if keys[pygame.K_SPACE]:
            salto = True
            izquierda = False
            derecha = False
            cuentaPasos = 0
    else:
        if cuentaSalto >= -10:
            py -= (cuentaSalto * abs(cuentaSalto)) * 0.5
            cuentaSalto -= 1
        else:
            cuentaSalto = 10
            salto = False

  

    # Actualización de la ventana
    pygame.display.update()
    #Llamada a la función de actualización de la ventana
    recargaPantalla()

#Salida del juego
pygame.quit()
