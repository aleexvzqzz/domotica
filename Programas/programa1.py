"""𝔸 𝕖𝕛𝕒𝕟𝕕𝕣𝕠 𝕍á𝕫𝕢𝕦𝕖𝕫 𝕀𝕘𝕝𝕖𝕤𝕚𝕒𝕤 | 𝕄𝔸ℚ𝕌𝔼𝕋𝔸 𝕋𝔼𝕀𝕊 𝟜 |
𝔽𝕖𝕔𝕙𝕒: 25/𝟘𝟝/𝟚𝟝"""  

from microbit import *  
import neopixel  

# Configuración de pins
np = neopixel.NeoPixel(pin13, 1)  # 1 LED Neopixel  
rele_ventilador = pin16  
sensor_temp = pin0  # *Pin analógico asignado (ajustar según maqueta)  

def actualizar_led(temp):  
    if temp < 20:  
        np[0] = (0, 0, 255)     # Azul 
    elif 20 <= temp < 22:  
        np[0] = (0, 255, 0)     # Verde  
    elif 22 <= temp < 24:  
        np[0] = (255, 165, 0)  # Naranja 
    else:  
        np[0] = (255, 0, 0)    # Rojo 
        rele_ventilador.write_digital(1)  # Ventilador ON
    np.show()  

while True:  
    temp_value = sensor_temp.read_analog()  
    temp_celsius = (temp_value * 3.3 / 1024) * 100 
    actualizar_led(temp_celsius)  
    if temp_celsius < 24:  
        rele_ventilador.write_digital(0)  # Ventilador APAGADO  
    sleep(1000)  
