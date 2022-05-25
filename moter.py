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
def motor_speed(power_ratio: float):
    """power ratioを引数にとりモータを回転させる関数
    Args:
        power (float): Duty比 (-100 ~ 100 %)
        power_ratio (float): パワー (-100 ~ 100 %)
    """

    duty_cycle = int(power * 4095 / 100)
    # MEMO: 条件外の値は前もってはじくというアーリーリターンの考え方を使うとコードがシンプルになる
    # 今回は範囲外と0の時を前もってはじくようにした

    # パワーが範囲外の場合
    if abs(power_ratio) > 100:
        print("パワーは100%以下にしてください")
        # パワーが範囲外であり正の値であれば100%に、負の値であれば-100%にする
        power_ratio = 100 if power_ratio > 0 else -100
        """
        もしくは
        raise ValueError("power ratio must be -100 ~ 100")
        不正な値が入力された場合に例外を発生させるか、値を直して続行させるかは設計思想次第
        """

    # パワーが0の場合
    if power_ratio == 0:
        pi.write(14, 0)
        pi.write(15, 0)
        PCA9685.set_pwm(0, 0, 0)
        return

    duty_cycle = int(power_ratio * 4095 / 100)

    # 時計回り
    if(power > 0 and power <= 100):
    # if (0 < power_ratio < 100): でもいいが、この上で100以上は弾いており来ないことが保証されるので下で良い
    if(power_ratio > 0):
        print("回転開始")
        pi.write(14, 1)
        pi.write(15, 0)
        PCA9685.set_pwm(0, 0, duty_cycle)

    # 半時計周り
    elif(power < 0 and power > -100):
    # if(-100 < power_ratio < 0): 同上
    elif(power_ratio < 0):
        print("逆回転開始")
        pi.write(14, 0)
        pi.write(15, 1)
        power = -1 * power
        power_ratio = -1 * power_ratio
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
