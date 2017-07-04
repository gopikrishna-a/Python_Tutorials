def get_gender(sex="Unknown"):
    if sex is 'M':
        sex = "Male"
    elif sex is 'F':
        sex = "Female"
    print sex

get_gender('M')
