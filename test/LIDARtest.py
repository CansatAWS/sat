import time,board,busio,adafruit_lidarlite
i2c = busio.I2C(board.SCL,board.SDA)
sensor = adafruit_lidarlite.LIDARLite(i2c)
print(sensor.status)
while True:
#     try:
    print(sensor.distance)
#     except RuntimeError as e:
#         print(e)
    time.sleep(0.5)