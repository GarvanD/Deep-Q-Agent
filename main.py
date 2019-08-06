import enviroment
import time
from agent import agent
if __name__ == "__main__":
    #enviroment.load_game()
    #time.sleep(10)
    hero = agent()
    print(enviroment.get_score())
    print("Ran")
    