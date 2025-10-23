import random
#קובץ כלים לשימוש



#מדמה "הטלת קוביה " פעמיים, עם מס' רנדומלי
def roll_two_d6() -> tuple[int, int]:
    roll=(random.randint(1,6), random.randint(1,6))
    return roll

def is_bust(score: int) -> bool:
    if score > 100:
        return True
    else:
        return False


def is_exact_100(score: int) -> bool:
    if score == 100:
        return True
    else:
        return False


def closer_to_target(a: int, b: int, target: int = 100) -> int |None:
    #בדיקה האם יש שוויון?
    if a == b:
        return None
    #מציאת המשתמש עם הקרבה יותר ליעד
    if (target-a)<(target-b):
        return 1
    else:
        return 2


def tie_breaker(roller) -> int:
    a = sum(roll_two_d6())
    b = sum(roll_two_d6())

    fleg=True
    while fleg:
        # זריקות קוביה של 2 השחקנים
        a = sum(roll_two_d6())
        b = sum(roll_two_d6())
        #בדיקת יציאה
        if a != b:
            fleg=False
    if a > b :
        return 1
    else:
        return 2




def turn_decision(input_fn) -> str:
    choice=input("Menu:\n Please enter your choice\n r-to roll the dice\n p-to skip the turn")
    return choice



def play_game():
    pass

