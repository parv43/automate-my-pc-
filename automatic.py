import pyautogui
import time
# this sleep library is help us to slow down the running of our progrm to our given time 
# time.sleep(4)
# this is the line that find the size of your screen 
# print(pyautogui.size())



# find the position of your cursor 
# print(pyautogui.position())



# move the courser of our mouse
# pyautogui.moveTo(500,700,5)
# pyautogui.moveTo(1000,1000,5)
# pyautogui.moveTo(100,20,5)


# this line is used to give the coordinates to the cursor and click it 
# pyautogui.click(100,20,duration=5)



# this line of code is help us to scroll the mouse 
# pyautogui.scroll(400)


# Now we are making the project of writing in notepad 
# pyautogui.click(730,1051,duration=3)
# time.sleep(2)
# pyautogui.write("notepad")
# pyautogui.press("enter")
# time.sleep(1)
# pyautogui.write("Hello")
# time.sleep(2)
# pyautogui.click(1434,45)



# count=10
app=input("enter which app you want to open\t")
if(app=='whatsapp'):
    name=input("Enter name which you want to do message \t")
    message=input("what message you want to do \t")
    pyautogui.click(730,1051,duration=1)
    time.sleep(1)
    pyautogui.write("whatsapp")
    pyautogui.press("enter")
    pyautogui.click(209,147,duration=4)
    pyautogui.write(name)
    pyautogui.press("enter")
    pyautogui.click(207,218,duration=1)
    pyautogui.click(764,975,duration=1)
    time.sleep(0)
    pyautogui.write(message)
    # time.sleep(0)
    pyautogui.press("enter")
elif(app=='chrome'):
    id=input("Enter id name which you want to open\t")
    web=input("enter name of website you want to open\t")
    videoname=input("Enter video name ")
    pyautogui.click(1231,1046,duration=1)
    pyautogui.click(1509,29,duration=1)
    if(id=='parv'):
        pyautogui.click(718,712,duration=1)
        if(web=='youtube'):
            pyautogui.click(718,712,duration=1)
            pyautogui.click(686,155,duration=1)
            pyautogui.write(videoname)
            time.sleep(3)
            pyautogui.press("enter")
            pyautogui.click(664,437,duration=2)




