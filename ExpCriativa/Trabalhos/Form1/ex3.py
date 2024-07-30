from machine import Pin

# Configurar o pino da chave e o pino do LED
chave = Pin(27, Pin.IN)
chaveD = Pin(32, Pin.IN)
chaveT = Pin(34, Pin.IN)
led = Pin(2, Pin.OUT)

# Loop infinito para verificar a posição da chave e acender ou apagar o LED
while True:
    if (chave.value() == 1 and chaveT.value() == 1) or (chaveT.value() == 0 and chave.value() == 0):   # Chave na posição ON
        led.on()             # Ligar o LED
    else:                    # Chave na posição OFF
        led.off()
