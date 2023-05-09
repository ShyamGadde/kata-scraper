def data_reverse(data):
    return [item 
            for segment in [data[i:i + 8] for i in range(0, len(data), 8)][::-1] 
            for item in segment]