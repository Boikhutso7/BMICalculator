
def calculate_BMI(weight_kg, height_cm):

    """this is a function that will calculate the BMI
     The BMI formula is your weight divided by your height squared.
     For metric units, use weight in kilograms (kg) and height in meters (m): BMI = weight (kg) / [height (m)]²

     args: weight_kg(float): weight in kilograms 
            height_cm(float): height in centimeters  

     Returns:
        dict: Contains 'bmi', 'category'

    """

    weight_kg = float(input("please enter your weight in kg "))
    height_cm = float(input("please your height in cm ")) 

    if weight_kg <= 0 or  height_cm <= 0:
        return {"error": "weight and height must be positive numbers and greater than zero "}
    
    if weight_kg > 1000 or height_cm > 500:
        return{"error": "please enter values that are realistic "}
    
    height_m = height_cm/ 100 # convert cm to m 

    BMI = weight_kg / (height_m ** 2)
    BMI = round(BMI, 2) # round the answer to two decimal places 

    if BMI < 18.5:
        category = "underweight"
    elif 18.5 <= BMI < 24.9:
        category = "Normal weight"
    elif  25 < BMI > 29.9:
        category = "Over weight"
    else:
        category = "Obese" 
    

    return {"bmi": BMI, "categoty": category}

