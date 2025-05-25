"""𝔸�𝕖𝕛𝕒𝕟𝕕𝕣𝕠 𝕍á𝕫𝕢𝕦𝕖𝕫 𝕀𝕘𝕝𝕖𝕤𝕚𝕒𝕤 | 𝕄𝔸ℚ𝕌𝔼𝕋𝔸 𝕋𝔼𝕀𝕊 𝟜 | ℂ𝕠𝕟𝕥𝕣𝕠𝕝 𝕝𝕦𝕫
𝔽𝕖𝕔𝕙𝕒: 𝟝/𝟘𝟝/𝟚𝟝"""

import neopixel  

from microbit import *  

# Configuración de pins
sensor_luz = pin1  
led = pin14  

while True:  
    luz = sensor_luz.read_analog()  
    if luz < 50:  # Ajustar valor
        led.write_digital(1)  # Encender  
    else:  
        led.write_digital(0)  # Apagar
    sleep(500)  
