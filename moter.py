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


def motor_speed(power: float):
    """powerを引数にとりモータを回転させる関数

    Args:
        power (float): Duty比 (-100 ~ 100 %)
    """

    duty_cycle = int(power * 4095 / 100)

    # 時計回り
    if(power > 0 and power <= 100):
        print("回転開始")
        pi.write(14, 1)
        pi.write(15, 0)
        PCA9685.set_pwm(0, 0, duty_cycle)

    # 半時計周り
    elif(power < 0 and power > -100):
        print("逆回転開始")
        pi.write(14, 0)
        pi.write(15, 1)
        power = -1 * power
        PCA9685.set_pwm(0, 0, duty_cycle)

    # vの値が大きい時
    elif(power > 100 and power < -100):
        pi.write(14, 0)
        pi.write(15, 0)
        PCA9685.set_pwm(0, 0, 0)

    else:
        pi.write(14, 0)
        pi.write(15, 0)
        PCA9685.set_pwm(0, 0, 0)


def motor_test():
    motor_speed(50)
    time.sleep(3)
    motor_speed(-50)
    time.sleep(3)
    motor_speed(25)
    time.sleep(3)
    print("終了")
    PCA9685.set_pwm(0, 0, 0)


if __name__ == "__main__":
    motor_test()
