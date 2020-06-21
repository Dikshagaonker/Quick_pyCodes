# PROGRAM FOR THE PASSWORD CHECKER

user_name =input('Enter the USER NAME :    ')

#print(user_name)
password = input('Enter the PASSWORD :   ')

#print(type(password))
password_length = len(password)

hidden_password ='*' * password_length

print(user_name +',' +'  your password,  '+ hidden_password + '  is  ' +  str(password_length) + '  letters long.')
