def get_size(w,h,d):
    return [
        2 * (d * w + d * h + w * h),
        d * w * h
    ]