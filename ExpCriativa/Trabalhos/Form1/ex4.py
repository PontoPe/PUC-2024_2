from machine import Pin

# Configurar o pino da chave e o pino do LED
A = Pin(13, Pin.IN)
B = Pin(12, Pin.IN)
C = Pin(27, Pin.IN)
D = Pin(32, Pin.IN)
E = Pin(34, Pin.IN)
led = Pin(2, Pin.OUT)

# Loop infinito para verificar a posição da chave e acender ou apagar o LED
while True:
    if (A.value() == 1 and B.value() == 1) or (C.value() == 1 and D.value() == 1) or (D.value() == 0 and E.value()== 0):   # Chave na posição ON
        led.on()             # Ligar o LED
    else:                    # Chave na posição OFF
        led.off()     
