"""
File: class_reviews.py
Name: QiaosiPan
-------------------------------
At the beginning of this program, the user is asked to input
the class name (either SC001 or SC101).
Attention: your input should be case-insensitive.
If the user input "-1" for class name, your program would show
the maximum, minimum, and average among all the inputs.
"""

def main():
    i = 0
    j = 0
    sum_001 = 0
    sum_101 = 0
    while 1 :    
        name_class_init = str(input('Which class?')) # enter class
        name_class = name_class_init.upper() # 不分大小寫
        # distinguish which class
        if name_class == str('SC001'): 
            i += 1
            name_score_001 = int(input('Score:')) # enter score
            if i == 1: # first run : MAX = MIN = current score
                sum_001 = sum_001 + name_score_001
                max_001 =name_score_001
                min_001 =name_score_001
            else: # MAX / MIN score & calculate
                sum_001 = sum_001 + name_score_001
                if name_score_001 >= max_001:
                    max_001 = name_score_001
                elif name_score_001 <= min_001:
                    min_001 = name_score_001
        elif name_class == str('SC101'):
            j += 1
            name_score_101 = int(input('Score:')) # enter score
            if j == 1: # first run : MAX = MIN = current score
                sum_101 = sum_101 + name_score_101
                max_101 =name_score_101
                min_101 =name_score_101
            else: # MAX / MIN score & calculate
                sum_101 = sum_101 + name_score_101
                if name_score_101 >= max_101:
                    max_101 = name_score_101
                elif name_score_101 <= min_101:
                    min_101 = name_score_101
        # when name_class == -1 , print result
        elif name_class == str('-1'):
            if ((i == 0) & (j==0)) :
                print('No class scores were entered')
                break
            if i != 0:
                avg_001 = sum_001/i
                print('=============SC001=============')
                print('Max (001)',max_001)
                print('Min (001)',min_001)
                print('Avg (001)',avg_001)
            else: 
                print('=============SC001=============')
                print('No score for SC001')
            if j != 0:
                avg_101 = sum_101/j
                print('=============SC101=============')
                print('Max (101)',max_101)
                print('Min (101)',min_101)
                print('Avg (101)',avg_101)
            else:
                print('=============SC101=============')
                print('No score for SC101')
            break    
    pass


# ---- DO NOT EDIT CODE BELOW THIS LINE ---- #

if __name__ == '__main__':
    main()
