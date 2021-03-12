def email_list(domains):
    email =[]
    for users, domain in domains.items():
        for user in users:
            email.append(user + "@" + domain)
        return email
print(email_list({"gmail.com": ["clark.kent", "diana.prince", "peter.parker"], "yahoo.com": ["barbara.gordon", "jean.grey"], "hotmail.com": ["bruce.wayne"]}))