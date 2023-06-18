from datetime import datetime
def check_coupon(entered_code, correct_code, current_date, expiration_date):
    if entered_code is correct_code:
        current = datetime.strptime(current_date, "%B %d, %Y")
        expiration = datetime.strptime(expiration_date, "%B %d, %Y")
        if current <= expiration:
            return True
    return False