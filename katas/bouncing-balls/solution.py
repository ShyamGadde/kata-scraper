def bouncing_ball(h, bounce, window):
    if h > 0 and window < h and 0 < bounce < 1:
        count = 1
        while (h := h * bounce) > window:
            count += 2
        return count
    return -1