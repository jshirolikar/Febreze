import speech_recognition as sr
#import http.client
from urllib2 import Request, urlopen, URLError, HTTPError
import requests
import os
import json
import subprocess
from pprint import pprint

r = sr.Recognizer()
m = sr.Microphone()

try:
    print("A moment of silence, please...")
    with m as source: r.adjust_for_ambient_noise(source)
    print("Set minimum energy threshold to {}".format(r.energy_threshold))
    while True:
        print("Say something!")
        with m as source: audio = r.listen(source)
        print("Got it! Now to recognize it...")
        try:
            # recognize speech using Google Speech Recognition
            value = r.recognize_google(audio)

         

            # we need some special handling here to correctly print unicode characters to standard output
            if str is bytes: # this version of Python uses bytes for strings (Python 2)
                print(u"You said {}".format(value).encode("utf-8"))
            else: # this version of Python uses unicode for strings (Python 3+)
                print("You said {}".format(value))
                
            res = os.system("curl --request GET   --url https://na-hackathon-api.arrayent.io:443/v3/devices/50331657   --header 'authorization: Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9.eyJjbGllbnRfaWQiOiJlMTA4NWE1MC0wMTcyLTExZTctYWU0Ni01ZmMyNDA0MmE4NTMiLCJlbnZpcm9ubWVudF9pZCI6Ijk0OGUyY2YwLWZkNTItMTFlNi1hZTQ2LTVmYzI0MDQyYTg1MyIsInVzZXJfaWQiOiI5MDAwMDgzIiwic2NvcGVzIjoie30iLCJncmFudF90eXBlIjoiYXV0aG9yaXphdGlvbl9jb2RlIiwiaWF0IjoxNDg4Njk4MTA2LCJleHAiOjE0ODk5MDc3MDZ9.UAl0KPGNXQm04KGLBLnD4x021iguFXMMLKcjhK8IBp5P1sc8CEmCEHPil_xeJwziSGblh5bKPWI5JomJTkcL5g'   --header 'cache-control: no-cache'   --header 'postman-token: 6c128c2c-6a5d-c615-8eac-d547885f2fde' >> arrayentoutput.json")
        



            with open('arrayentoutput.json') as data_file:    
                data = json.load(data_file)
                #pprint(data)
                print("Device Name : " + str(data["deviceName"]))
                print("Device ID : " + str(data["deviceId"]))
                print("Device Type Name : " + str(data["deviceTypeName"]))
                print("Presence Info :" + str(data["presenceInfo"]))
                
                if("motion" in value):
                    print("The current motion detection status is:")
                    print(data["attributes"][2])
                
                if("humidity" in value):
                    print("The current humidity status is:")
                    print(data["attributes"][24])
                
                if("temperature" in value):    
                    print("The current temperature status is:")
                    print(data["attributes"][29])
                    
                if("scene" in value):
                    print("The current scene status is:")
                    print(data["attributes"][35])
                
            os.system("rm arrayentoutput.json")
        
,
        except sr.UnknownValueError:
            print("Oops! Didn't catch that")
        except sr.RequestError as e:
            print("Uh oh! Couldn't request results from Google Speech Recognition service; {0}".format(e))
            




        
            
except KeyboardInterrupt:
    pass
