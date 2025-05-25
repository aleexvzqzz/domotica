"""𝔸𝕍𝕒𝕫𝕢𝕦𝕖𝕫 𝕀𝕘𝕝𝕖 𝕚𝕒𝕤 | 𝕄𝔸ℚ𝕌𝔼𝕋𝔸 𝕋𝔼𝕀𝕊 𝟜 | 𝔹𝕠𝕥ó𝕟 𝔸  
𝔽𝕖𝕔𝕙𝕒: 𝟝/𝟘𝟝/𝟚𝟝"""  

from microbit import *  
import music  

# Configuración de pins / Configuración dos pins  
boton_a = pin5  # *Asignar pin correcto  
led = pin14  

def accion_boton():  
    for _ in range(5):  # Parpadear 5 veces / Piscar 5 veces  
        led.write_digital(1)  
        music.play(music.RINGTONE)  
        sleep(500)  
        led.write_digital(0)  
        sleep(500)  

while True:  
    if boton_a.read_digital() == 1:  
        accion_boton()  
    sleep(100)  
