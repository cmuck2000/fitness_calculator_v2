# Global Variables
global weight_units
global height_units
global bmi_bool
global calorie_bool
global macro_bool
global gender


# Function for a 2 option selection
def a_or_b(answer, a, b):
    while True:
        choice = input(f"{answer} {a[0]}/{b[0]}: \n").lower()
        if choice in a:
            return True
        elif choice in b:
            return False
        else:
            print(f"Please respond with {a[0]} or {b[0]}\n")


def yes_no(answer):
    yes = ['yes', 'y', 'ye']
    no = ['no', 'n']
    return a_or_b(answer, yes, no)


def get_value(answer, low, high):
    while True:
        input_str = input(f"{answer}\n")
        input_int = int(input_str)
        if input_int in range(low, high):
            return input_int
        else:
            print(
                f"invalid answer. please respond with a integer in the range {low} to {high}")


def bmi_calculation_start():
    print("This bmi calculator will ask you a few simple questions and return your bmi and healthy weight range")


    if (height_units):
        height_in_ft = get_value(
            "(you will be asked to add inches in the next question) what is your height in ft?: ", 1, 9)
        height_in_ft_add_inches = get_value(
            "add inches to your current height: ", 0, 12)
        global height_in_cm
        height_in_cm = ((height_in_ft * 12) + height_in_ft_add_inches) * 2.54
    else:
        height_in_cm = get_value(
            "what is your height in cm: ", 25, 275)

    if (weight_units):
        weight_in_lb = get_value(
            "what is your weight in lb?: ", 40, 600)
        global weight_in_kg
        weight_in_kg = weight_in_lb * 0.45359237
    else:
        weight_in_kg = get_value(
            "what is your weight in kg?: ", 25, 300)

    bmi = (weight_in_kg / height_in_cm / height_in_cm) * 10000
    bmi = round(bmi, 1)

    print("""this bmi value is not to be taken as an exact science and is only an approxmation of your healthy weight range.
    if you are concerned about the value you receive consult a medical professional for further steps.\n""")
    if(bmi <= 16):
        print(f"Your bmi is {bmi}. this is considered very underweight\n")
    elif(bmi <= 18.5):
        print(f"Your bmi is {bmi}.this is considered underweight\n")
    elif(bmi <= 25):
        print(f"Your bmi is {bmi}. this is considered Healthy\n")
    elif(bmi <= 30):
        print(f"Your bmi is {bmi}. this is considered overweight\n")
    else:
        print(f"Your bmi is {bmi}. this is considered very overweight\n")

    if calorie_bool:
        calorie_calculation_start()
    elif not calorie_bool and macro_bool:
        pass  # macro_calculation_start()
    else:
        pass  # end_program


def calorie_calculation_start():
    print("this calorie will ask you a few simple questions and return your recomended daily calorie intake.\n")
    gender = a_or_b("are you male or female?", ["m", "male", "man", "ma", "mal"], [
                    "f", "female", "femal", "fema", "fem", "fe"])

    age = get_value("what is your age?: ", 18, 140)

    if gender:
        bmr = 10 * weight_in_kg + 6.25 * height_in_cm - 5 * age + 5
    else:
        bmr = 10 * weight_in_kg + 6.25 * height_in_cm - 5 * age - 161

    print(
        f"your BMR (basal metabolic rate) is {bmr}\n this is an approximation of how many calories your body burns without any additional energy expenditure apart from breathing.")

    print("""this table will demonstrate examples to help you pick an activity level multiplies to calculate your calories.\n
    LIFESTYLE & TRAINING FREQUENCY-----EXAMPLE-----ACTIVITY MULTIPLIER\n
    Sedentary + Training 3-6x/wk-----Works a desk jobvery little activity outside of lifting-----1.2 - 1.5\n
    Lightly Active + Training 3-6x/wk-----Works a desk job, takes pet for a walk most days in addition to lifting-----1.5 - 1.8\n
    Moderately Active + Training 3-6x/wk-----Works as a full-time waitress, occasionally plays tennis in addition tolifting-----1.8 - 2.0\n
    Highly Active + Training 3-6x/wk-----Works as a construction worker, regular hiking in addition to lifting-----2.0 - 2.2\n""")
    activity_level = get_value(
        "what is your estimated activity level multiplier?: ", 1, 2)
    maintance_calories = bmr * activity_level

    print(
        f"your calculated  daily calories to maintain your current weight is {maintance_calories}")


def main():
    print("Welcome to fitness_calculator v3. this calculator can be used for bmi,calories,macros and fibre using industry standard calculations.\n")

    bmi_bool = yes_no(
        "would you like to calculate your bmi and healthy weight range?")
    calorie_bool = yes_no("would you like to calculate your calories?")
    macro_bool = yes_no("would you like to calculate your macros?")

    weight_units = a_or_b("would you like to use lb or kg for weight measurements?", [
                          "lb", "l"], ["kg", "k"])
    height_units = a_or_b("would you like to use ft or cm for height measurements?", [
                          "ft", "f"], ["cm", "c"])

    bmi_calculation_start()
    calorie_calculation_start()
    # if (bmi_bool):
    #     bmi_calculation_start()
    # elif (calorie_bool):
    #     calorie_calculation_start()
    # elif (macro_bool):
    #     macro_calculation_start()
    # else:
    #     end_program()


main()
