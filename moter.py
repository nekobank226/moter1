import pigpio
import time
import Adafruit_PCA9685

# 設定周波数
SET_FREQ = 50

# ピンの設定
pi = pigpio.pi()
pi.set_mode(14, pigpio.OUTPUT)
pi.set_mode(15, pigpio.OUTPUT)

# PCA9685の初期化
PCA9685 = Adafruit_PCA9685.PCA9685()
PCA9685.set_pwm_freq(SET_FREQ)


def moterspeed(v):
    # モータの回転速度を引数にする関数

    # 時計回り
    if(v > 0 and v <= 100):
        print("回転開始")
        pi.write(14, 1)
        pi.write(15, 0)
        a = v * 40
        PCA9685.set_pwm(0, 0, a)

    # 半時計周り
    elif(v < 0 and v > -100):
        print("逆回転開始")
        pi.write(14, 0)
        pi.write(15, 1)
        v = -1 * v
        a = v * 40
        PCA9685.set_pwm(0, 0, a)

    # vの値が大きい時
    elif(v > 100 and v < -100):
        pi.write(14, 0)
        pi.write(15, 0)
        PCA9685.set_pwm(0, 0, 0)


moterspeed(50)
time.sleep(3)
moterspeed(-50)
time.sleep(3)
moterspeed(25)
time.sleep(3)
print("終了")
PCA9685.set_pwm(0, 0, 0)
