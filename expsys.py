# this code is done by fariq el-a7lam


from datetime import datetime
date = datetime.now()
month = date.month
def get_season(month):
    if 11 < month < 3:
        return "winter"
    if 2 < month < 6:
        return "spring"
    if 5 < month < 9:
        return "summer"
    if 8 < month < 12:
        return "autumn"


season = get_season(month)

# if there is switch case in python it would be better

if season == "autumn":
    from GUIs import autumnGUI
elif season == "summer":
    from GUIs import summerGUI
elif season == "winter":
    from GUIs import winterGUI
elif season == "spring":
    from GUIs import springGUI

