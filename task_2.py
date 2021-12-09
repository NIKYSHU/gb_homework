with open('users.csv', 'r', encoding='utf-8') as users:
    with open('hobby.csv', 'r', encoding='utf-8') as hobby:
        with open('result.csv', 'w+', encoding='utf-8') as result:
            for user in users:
                line = '{}: {}'.format(user.rstrip('\n'), str(next(hobby, None)).rstrip('\n'))
                result.writelines(line + '\n')