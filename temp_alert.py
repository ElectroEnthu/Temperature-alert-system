import time,json,conf
from boltiot import Bolt
mybolt = Bolt(conf.api_key, conf.device_id)
while True:
       response = mybolt.analogRead('A0')
       data = json.loads(response)
       sensor_value = int(data['value'])
       temperature = (100*sensor_value)/1024
       print ("Current temperature value is:" + str(temperature) + " ℃")

       if temperature > 50:
           on = mybolt.digitalWrite('0', 'HIGH')
           print(on)
           time.sleep(10)
       elif temperature < 50:
           off = mybolt.digitalWrite('0', 'LOW')
           print(off)
           time.sleep(10)
