visit_file = open('visit_log.csv')
funnel_file = open('funnel.csv')

funnel_file.write('user_id,source,category\n')

for line in visit_file:
    parts = line.strip().split(',')

    if len(parts) >= 3 and parts[2].strip():
        user_id = parts[0]
        source = parts[1]
        category = parts[2]

        funnel_file.write(f'{user_id},{source},{category}\n')
