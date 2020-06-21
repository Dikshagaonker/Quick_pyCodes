def checkDriver(age = 0):
    '''
    Info : This function is created to test the age of the driver.

    '''
    #age = input('What is your age?:    ')
    
    if int(age) < 18:
        print('Sorry, you are too young to drive this car.Powering off')
        
    elif int(age)== 18:
        print('Congratulation on your first year of driving.Enjoy the ride.')
        
    elif int(age)> 18:
        print('Powering on. Enjoy the ride')
        
        
        
checkDriver()
