import pyautogui as pag
import FacePose as fp
# import time
# fp.main()

a, b = pag.size()
for x, y, z in fp.main():
    x = float(x)
    y = float(y)
    z = float(z)
    # print(x,y,z)
    if y > 15:
        pag.moveRel(5, 0)
    if y < -15:
        # start= time.process_time()
        pag.moveRel(-5, 0)
        # stop = time.process_time()
        # print(1000*(stop-start))
        # time.sleep(1)
