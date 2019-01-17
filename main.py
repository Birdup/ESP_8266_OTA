from ota_update.main.ota_updater import OTAUpdater
from machine import Pin, PWM, ADC
from time import sleep

 def download_and_install_update_if_available():
     o = OTAUpdater('url-to-your-github-project')
     o.download_and_install_update_if_available('wifi-ssid', 'wifi-password')


 def start():
     frequency = 5000
     led = PWM(Pin(5), frequency)
     pot = ADC(0)

      while True:
        pot_value = pot.read()
        print(pot_value)

        if pot_value < 15:
          led.duty(0)
        else:
        led.duty(pot_value)
      sleep(0.1)

 def boot():
     download_and_install_update_if_available()
     start()
 boot()
