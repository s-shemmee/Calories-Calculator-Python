def main():
    welcome()
    gender = sex()
    weight = get_weight()
    height = get_height()
    age = get_age()
    rest_bmr = calculate_bmr(gender, weight, height, age) 
    total_calculation(rest_bmr)


def welcome():
    print("Welcome to your calories python calculator!\nFind out How many calories should you eat daily.\n")


def sex():    
    sexes = ["male","female","M","F","f","m","Male","Female"]
    while True:
        sex = str(input("Do you identify as male or female? "))
        while sex not in sexes:
            sex = str(input("Please enter either 'male' or 'female' "))
        else:
            return sex
            break

def get_weight():
    weight_kg = float(input("Enter your weight in kilograms: "))
    while weight_kg <= 0:
        weight_kg = float(input("Invalid input. Please enter your weight in kilograms: "))
    else:
        return weight_kg


def get_height():
    height_cm = float(input("Enter your height in Centimeters: "))
    while height_cm <= 0:
        height_cm = float(input("Invalid input. Please enter your height in Centimeters: "))
    else:
        return height_cm


def get_age():
    age_yrs = int(input("Enter your age in years: "))
    while age_yrs <= 0:
        age_yrs = int(input("Invalid Input. Please enter your age in years: "))
    else:
        return age_yrs


def calculate_bmr(gender, weight, height, age):
    male = ["male", "M" , "m", "Male"]
    female = ["female", "F", "f", "Female"]
    if gender == female:
        women = (weight * 10) + (height * 6.25) - (age * 5) - 161
        return int(women)
    else:
        men = (weight * 10) + (height * 6.25) - (age * 5) + 5
        return int(men)



def total_calculation(rest_bmr):
    user_activity_lvl = get_user_activity()    

    maintain = {
      "sedentary" : get_sedentary(rest_bmr), 
      "light" : get_light_activity(rest_bmr), 
      "moderate" : get_moderate_activity(rest_bmr), 
      "active" : get_very_active(rest_bmr)
      }

    if user_activity_lvl == "sedentary":
        print("You need to eat " + str(maintain["sedentary"]) + " calories a day to maintain your current weight")

    if user_activity_lvl == "light":
        print("You need to eat " + str(maintain["light"]) + " calories a day to maintain your current weight")

    if user_activity_lvl == "moderate":
        print("You need to eat " + str(maintain["moderate"]) + " calories a day to maintain your current weight")

    if user_activity_lvl == "active":
        print("You need to eat " + str(maintain["active"]) + " calories a day to maintain your current weight")


   
def get_user_activity():
    activity_lvl = ["sedentary", "light", "moderate", "active"]
    while True:
        user_lvl = str(input("\nWhat is your activity level?\n\nSedentary is little to no exercise.\nLightly active is light exercise/sports 1 - 3 days/week.\nModerately active is moderate exercise/sports 3 - 5 days/week.\nVery active is hard exercise every day, or 2 xs/day 6 - 7 days/week.\n\nPlease enter: 'sedentary', 'light', 'moderate',  or 'active' "))
        
        while user_lvl not in activity_lvl:
            user_lvl = str(input( "Invalid input. Please enter: 'sedentary', 'light', 'moderate',  or 'active' "))
        else:
            return user_lvl
            break


def get_sedentary(rest_bmr):
    sedentary = rest_bmr * 1.25
    return sedentary

def get_light_activity(rest_bmr):
    light = rest_bmr * 1.375
    return light

def get_moderate_activity(rest_bmr):
    moderate = rest_bmr * 1.550
    return moderate

def get_very_active(rest_bmr):
    active = rest_bmr * 1.725
    return active

if __name__ == '__main__':
    main()