Это простой пакет API погоды
стэк: request, radis, ограничитель скорости

Процесс разработки:

1. Создается само АПИ
2. Навешиваем рэдис
3. Ограничиваем скорость через рэдис
4. Тесты

key: FGYALYN7QTKBHNWV5VQF7XTTH

import urllib.request
import sys

import json
                
try: 
  ResultBytes = urllib.request.urlopen("https://weather.visualcrossing.com/VisualCrossingWebServices/rest/services/timeline/Russian?unitGroup=us&key=FGYALYN7QTKBHNWV5VQF7XTTH&contentType=json")
  
  # Parse the results as JSON
  jsonData = json.load(ResultBytes)
        
except urllib.error.HTTPError  as e:
  ErrorInfo= e.read().decode() 
  print('Error code: ', e.code, ErrorInfo)
  sys.exit()
except  urllib.error.URLError as e:
  ErrorInfo= e.read().decode() 
  print('Error code: ', e.code,ErrorInfo)
  sys.exit()