def calculate_age(year_of_birth, current_year):
    diff = current_year-year_of_birth
    if diff > 0:
        return f"You are {diff} year{'s' if diff>1 else ''} old."
    elif diff < 0:
        return f"You will be born in {-diff} year{'s' if -diff>1 else ''}."
    else:
        return "You were born this very year!"