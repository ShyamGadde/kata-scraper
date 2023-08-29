def ip_to_int32(ip):
    return int(''.join(map(lambda x: f"{int(x):08b}",ip.split('.'))),2)