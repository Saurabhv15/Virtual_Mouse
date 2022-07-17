# Virtual Mouse
Virtual Mouse that will soon to be introduced to replace the physical computer
mouse to promote convenience while still able to accurately interact and control
the computer system. To do that, the software requires to be fast enough to capture
and process every image, in order to successfully track the user's gesture.
Therefore, this project will develop a software application with the aid of the latest
software coding technique and the open-source computer vision library also
known as the OpenCV. The scope of the project is as below:

 Real time application.

 User friendly application.

 Removes the requirement of having a physical mouse.


## Documentation
## Pyautogui
To install with pip, run pip install pyautogui

Code :

import pyautogui #move our curser

screen_width, screen_height = pyautogui.size()

pyautogui.moveTo(index_x, index_y)

pyautogui.click()

pyautogui.sleep(1)


## Mediapipe
To install with pip, run pip install Mediapipe

## Most important step


                    index_x = screen_width/frame_width*x      #to cover the hole screen in x direction
                    index_y = screen_height/frame_height*y             #to cover the y direction



## Screenshot
<img width="960" alt="2022-07-17 (1)" src="https://user-images.githubusercontent.com/75581812/179388072-453cb4fb-85cf-4fb9-9a7c-58a482b1dddc.png">
<img width="960" alt="2022-07-17" src="https://user-images.githubusercontent.com/75581812/179388089-4b72acbb-8e60-4a44-978e-da7075f0e39a.png">
