import pigpio
import time
import Adafruit_PCA9685

#設定周波数
SET_FREQ = 50

#ピンの設定
pi = pigpio.pi()
pi.set_mode(14,pigpio.OUTPUT)
pi.set_mode(15,pigpio.OUTPUT)

#PCA9685の初期化
PCA9685 = Adafruit_PCA9685.PCA9685()
PCA9685.set_pwm_freq(SET_FREQ)

#モータの回転速度を引数にする関数
def moterspeed(v):
    #時計回り
    if(v>0,v<100):
        pi.write(14,1)
        pi.write(15,0)
        PCA9685.set_pwm(0,0,v*0.01*4095)

    else(v<0,v>-100):
        pi.write(14,0)
        pi.write(15,1)
        v = -v
        PCA9685.set_pwm(0,0,v*0.01*4095)

    else(v>100,v<-100):
        pi.write(14,0)
        pi.write(15,0)
        PCA9685.set_pwm(0,0,0)

v = 50
time.sleep(3)
v = -50
time.sleep(3)
v = 1
time.sleep(3)
#停止
pi.write(14,0)
pi.write(15,0)
PCA9685.set_pwm(0,0,0)


