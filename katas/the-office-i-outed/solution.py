def outed(meet, boss):
    score = (sum(meet.values()) + meet[boss]) /  len(meet)
    return 'Nice Work Champ!'if score > 5 else 'Get Out Now!'