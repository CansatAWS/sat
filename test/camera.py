from picamera import PiCamera
from time import sleep

camera = PiCamera()

camera.start_preview()
sleep(60)
camera.stop_preview()