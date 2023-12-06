import time
import pvporcupine
from pvrecorder import PvRecorder
import keyboard
from utils.time import sleep
import sys
import os

porcupine = pvporcupine.create(

    access_key = 'cF4xMp7r9WbL8zuwtJy4J6zabU6f7SlDHfv6rfYMuy4JLlYAwDUHyw==',

    keyword_paths = [
                    "./custom_keywords/aloha-mora_en_windows_v3_0_0.ppn",
                    "./custom_keywords/ava-da-ce-dau-ra_en_windows_v3_0_0.ppn",
                    "./custom_keywords/Bomb-arda_en_windows_v3_0_0.ppn",
                    "./custom_keywords/Can-finger_en_windows_v3_0_0.ppn",
                    "./custom_keywords/cru-cio_en_windows_v3_0_0.ppn",
                    "./custom_keywords/def-indo_en_windows_v3_0_0.ppn",
                    "./custom_keywords/Disillusion_en_windows_v3_0_0.ppn",
                    "./custom_keywords/Expellee-aramus_en_windows_v3_0_0.ppn",
                    "./custom_keywords/imperio_en_windows_v3_0_0.ppn",
                    "./custom_keywords/In-send-io_en_windows_v3_0_0.ppn",
                    "./custom_keywords/Lady-also_en_windows_v3_0_0.ppn",
                    "./custom_keywords/Lumas_en_windows_v3_0_0.ppn",
                    "./custom_keywords/Proud-to-go_en_windows_v3_0_0.ppn",
                    "./custom_keywords/R-Vail-leo_en_windows_v3_0_0.ppn",
                    "./custom_keywords/terrifical-status_en_windows_v3_0_0.ppn",
                    "./custom_keywords/The-pool-so_en_windows_v3_0_0.ppn"
                    ],
    sensitivities=[1] * 16
)

recorder = PvRecorder(device_index=0, frame_length=porcupine.frame_length)
recorder.start()
print('Using device: %s' % recorder.selected_device)

while True:
    pcm = recorder.read()
    keyword_index = porcupine.process(pcm)
    
    if keyword_index == 0:
        keyboard.press_and_release("f")
        sleep(0.05)
        
    elif keyword_index == 1:
        keyboard.press_and_release("F1")
        sleep(0.05)
        keyboard.press_and_release("3")

    elif keyword_index == 2:
        keyboard.press_and_release("F1")
        sleep(0.05)
        keyboard.press_and_release("4")

    elif keyword_index == 3:
        keyboard.press_and_release("F4")
        sleep(0.05)
        keyboard.press_and_release("4")

    elif keyword_index == 4:
        keyboard.press_and_release("F1")
        sleep(0.05)
        keyboard.press_and_release("1")

    elif keyword_index == 5:
        keyboard.press_and_release("F4")
        sleep(0.05)
        keyboard.press_and_release("2")

    elif keyword_index == 6:   
        keyboard.press_and_release("F3")
        sleep(0.05)
        keyboard.press_and_release("4")

    elif keyword_index == 7:
        keyboard.press_and_release("F2")
        sleep(0.05)
        keyboard.press_and_release("3")

    elif keyword_index == 8:
        keyboard.press_and_release("F1")
        sleep(0.05)
        keyboard.press_and_release("2")

    elif keyword_index == 9:
        keyboard.press_and_release("F2")
        sleep(0.05)
        keyboard.press_and_release("4")

    elif keyword_index == 10:
        keyboard.press_and_release("F2")
        sleep(0.05)
        keyboard.press_and_release("1")

    elif keyword_index == 11:
        keyboard.press_and_release("F3")
        sleep(0.05)
        keyboard.press_and_release("1")

    elif keyword_index == 12:
        keyboard.press_and_release("q")
        sleep(0.05)

    elif keyword_index == 13:
        keyboard.press_and_release("r")
        sleep(0.05)
        
    elif keyword_index == 14:
        keyboard.press_and_release("f")
        sleep(0.05)
        
    elif keyword_index == 15:
        keyboard.press_and_release("F4")
        sleep(0.05)
        keyboard.press_and_release("2")

porcupine.delete()








         



    
    
 
    
    
    
    
    
    
    
    
    
        
    
    
    





	