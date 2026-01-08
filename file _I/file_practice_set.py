# f=open("poem.txt")
# content=f.read()
# if("Twinkle in content"):
#     print("Twinkle is present")
# else:
#     print("word not present")
# f.close()   

import random 
def game():
    print("You are playing the game")
    score=random.randint(1,62)
    with open("hiscore.txt") as f:
        hiscore=f.read()
        if(hiscore!=""):
            hiscore=int(hiscore)
        else:
            hiscore=0
    print(f"your score:{score}")
    if(score>hiscore):
        with open("hiscore.txt","w") as f:
            f.write(str(score))
    return score                    
game()    

