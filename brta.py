import random

class BRTA:

    def __init__(self) -> None:
        self.__license = {}
        

    def take_driving_test(self,email):
        score = random.randint(0, 100)
        if score >= 33:
            # print('Congress! You have Passed, Your Score:',score)
            license_number = random.randint(5000, 9999)
            self.__license[email] = license_number
            return license_number

        else:
            # print('Sorry! You Have Filed! Your Score:',score)
            return False

    
    def validate_license(self,email,license):

        for valid_mail,valid_license in self.__license.items():
            if valid_mail == email and valid_license == license:
                return True
                
        return False
