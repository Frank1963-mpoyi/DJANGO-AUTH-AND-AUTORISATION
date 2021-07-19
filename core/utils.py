import random
from datetime                                               import datetime
from string                                                 import ascii_uppercase, digits


def get_timenow():

    today   = datetime.now().strftime('%y%m%d-%H%M%S').split('-')
    date    = today[0]
    now     = today[1]

    return date, now


def randcode_gen():

    date, now   = get_timenow()

    randcode    = random.sample(digits, 4) + random.sample(ascii_uppercase, 1)
    randcode    = (''.join(randcode))
    new_code    = f"Mpoyi{date}{randcode}{now}"

    return new_code
