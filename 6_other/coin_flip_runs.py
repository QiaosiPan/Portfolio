"""
File: coin_flip_runs.py
Name: QiaosiPan
-----------------------
This program should simulate coin flip(s)
with the number of runs input by users.
A 'run' is defined as consecutive results
on either 'H' or 'T'. For example, 'HHHHHTHTT'
is regarded as a 2-run result.
Your program should stop immediately after your
coin flip results reach the number of runs!
"""

import random as r


def main():
    print("Let's flip a coin!")
    i = int(input('Number of runs : '))
    coin_old = ""
    coin_str = ""
    for x in range(1,i+1):
        ## final run (i), stop until the same result shows up
        if x == i: 
            while 1:
                coin = r.choice('HT')
                coin_str += coin
                if coin == coin_old: 
                    break
                else: 
                    coin_old = coin
        else:
            ## before final run, stop loop until the end of continous result
            while 1:  
                coin = r.choice('HT')
                coin_str += coin
                if coin == coin_old:
                    ## when same result shows up, stop until the opposite result comes out
                    while 1: 
                        coin = r.choice('HT')
                        coin_str += coin
                        if coin != coin_old:
                            coin_old = coin
                            break                        
                    break
                else: 
                    coin_old = coin
    print(coin_str)
    pass


# ---- DO NOT EDIT CODE BELOW THIS LINE ---- #

if __name__ == "__main__":
	main()
