import GarageServo
import pi_servo_hat
import time
import sys


class GarageServoController:

    servos = [GarageServo]
    servo_hat = pi_servo_hat.PiServoHat()
    servo_hat.restart()
    servo_hat.set_pwm_frequency(50)

    def __init__(self, servos):
        self.servos = sorted(servos, key=lambda x: x.park_pos)

    def mov_to_park_pos(self):
        for servo in self.servos:
            self.servo_hat.set_duty_cycle(servo.channel, servo.up_dc)
            time.sleep(.001)

        last_sleep = 0
        for servo in self.servos:
            min_sleep = servo.park_pos - last_sleep
            for i in range(0, min_sleep):
                time.sleep(1)
            self.servo_hat.set_duty_cycle(servo.channel, servo.stop_dc)
            last_sleep = servo.park_pos

        self.servo_hat.restart()


    def move_to_home(self):
        for servo in self.servos:
            self.servo_hat.set_duty_cycle(servo.channel, servo.down_dc)
            time.sleep(.001)

        last_sleep = 0
        for servo in self.servos:
            min_sleep = servo.park_pos - last_sleep
            for i in range(0, min_sleep):
                #offset to account for more force required for up than down. shit
                time.sleep(1.03)
            self.servo_hat.set_duty_cycle(servo.channel, servo.stop_dc)
            last_sleep = servo.park_pos

        self.servo_hat.restart()

    #WIP
    def calibrate_park_pos(self):

        servo_index_to_cal = input("Enter index of servo to calibrate:")

        for servo in self.servos:
            if servo.channel == servo_index_to_cal:
                break
        else:
            print("Servo with index not found")

        servo_to_cal = servo

        input("Begin calibration upon hitting enter, press enter to stop")
        self.servo_hat.set_duty_cycle(servo_to_cal.channel, servo_to_cal.up_dc)
        sleep = 0

        while True:
            try:
                stdin = sys.stdin.read()
                if "\n" in stdin or "\r" in stdin:
                    break
            except IOError:
                pass
            time.sleep(.2)
            sleep = sleep + .2
            self.servo_hat.restart()

        while True:
            fine_adj = float(input("Enter fine adjustment or type ok to finish"))
            if fine_adj < 0:
                self.servo_hat.set_duty_cycle(servo.channel, servo_to_cal.down_dc)
            else:
                self.servo_hat.set_duty_cycle(servo.channel, servo_to_cal.up_dc)

            sleep = sleep + fine_adj
            try:
                stdin = sys.stdin.read()
                if "ok" in stdin:
                    break
            except IOError:
                pass
            time.sleep(fine_adj)
            self.servo_hat.restart()

        cnt = 0
        for servo in self.servos:
            if servo.channel == servo_index_to_cal:
                self.servos[cnt].set_park_pos(sleep)
                break
            cnt = cnt + 1

