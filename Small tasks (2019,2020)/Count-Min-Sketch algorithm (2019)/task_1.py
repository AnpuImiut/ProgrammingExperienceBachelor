import CountMinSketchTree as CMKT
import bruteforce as BT


T = CMKT.CMK_Tree(2/3,1/8)
filename = input("Filename plssss\n")
T.read_data("data/"+filename)
# T.ausgabe()
T.run()
# T.ausgabe()

B = BT.bruteforce()
B.read_data("data/"+filename)
B.run()
# B.ausgabe()
