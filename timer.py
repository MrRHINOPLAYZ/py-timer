import time
seconds = input("ENTER TIME IN SECONDS : ")
def countdown(seconds):
    while seconds > 0 :
    
        min = int(seconds / 60)
        sec = int(seconds % 60)
        timer =f"{min} : {sec}"
        print (timer)
        seconds -=1
        time.sleep(0.5)
    print("time up")

countdown (int (seconds))
