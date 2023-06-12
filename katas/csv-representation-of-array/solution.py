def to_csv_text(array):
    return '\n'.join(','.join(map(str, subarray)) for subarray in array)