from machine import Pin
# Configurar o pino da chave e o pino do LED
A = Pin(13, Pin.IN)
B = Pin(12, Pin.IN)
C = Pin(27, Pin.IN)
D = Pin(32, Pin.IN)
led = Pin(2, Pin.OUT)

x = A.value()
y = B.value()
z = C.value()
w = D.value()

# Loop infinito para verificar a posição da chave e acender ou apagar o LED
while True:
    if (x == 0 and y == 0 and w == 1) or (x == 1 and y == 0 and w == 1) or (x == 1 and y == 1 and z == 0) or (x == 1 and y == 1 and z == 1 and w == 0):   # Chave na posição ON
        led.on()             # Ligar o LED
    else:                    # Chave na posição OFF
        led.off()
