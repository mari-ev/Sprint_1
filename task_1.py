time = ['1h 45m,360s,25m,30m 120s,2h 60s']

summary_minutes = sum(
    int(part.replace('h', '').replace('m', '').replace('s', '')) * 60 if 'h' in part else
    int(part.replace('h', '').replace('m', '').replace('s', '')) if 'm' in part else
    int(part.replace('h', '').replace('m', '').replace('s', '')) / 60
    for element in time
    for part in element.replace(',', ' ').split()
)

print(f"{int(summary_minutes)} минут")