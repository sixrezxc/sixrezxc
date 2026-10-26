def words(logins):
    for login in logins:
        if login == '':
            pass
        elif len(login) >= 2:
            pass
        else:
            print(login.lower())

words([" Alex ", "bob", "", " JOHN", "al", "Kate "])