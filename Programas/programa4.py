"""𝔸𝕍𝕒𝕫𝕢𝕦𝕖𝕫 𝕀𝕘𝕝𝕖𝕤𝕚𝕒𝕤 | 𝕄𝔸ℚ𝕌𝔼𝕋𝔸 𝕋𝔼𝕀𝕊 𝟜 | 𝕊𝕖𝕣𝕧𝕠  
𝔽𝕖𝕔𝕙𝕒: 𝟝/𝟘𝟝/𝟚𝟝"""  

from microbit import *  
import servo  

# Configuración de pins
boton_b = pin6  # *Asignar pin correcto  
servo_motor = servo.Servo(pin2)  
angulo = 0  

while True:  
    if boton_b.read_digital() == 1:  
        angulo += 10  
        if angulo > 90:  
            angulo = 0  
        servo_motor.write_angle(angulo)  
        sleep(500)  # Evitar rebotes
    sleep(100)  
