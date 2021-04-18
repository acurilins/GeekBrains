first_name = input('Enter your First Name - ')
last_name = input('Enter your Last Name - ')
birthday = input('Enter your D.O.B. - ')
city = input('Enter your current city - ')
email = input('Enter your e-mail address - ')
phone = input('Enter your phone number - ')


def data(first_name, last_name, birthday, city, email, phone):
    return f"First Name : {first_name};\nLast Name : {last_name};\nD.O.B. : {birthday};\n" \
           f"City : {city};\ne-mail : {email};\nPhone number : {phone};"


print(data(first_name, last_name, birthday, city, email, phone))


