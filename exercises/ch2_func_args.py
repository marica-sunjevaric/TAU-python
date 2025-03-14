def user_info(name, age=0, city="Tucson"):
    '''
    this function prints name, age, and city
    from an argument provided to the function.
    :param name:
    :param age:
    :param city:
    :return:
    '''
    print("{} is {} years old, from {}.".format(name, age, city))


user_info("Janet", 58, "Oklahoma City")
user_info("Micah")
user_info(age=56, name="Kadeem")

def application(fname, lname, email, company, *args, **kwargs):
    print("{} {} works at {}. Her email is {}.".format(fname, lname, company, email))

    for arg in args:
        print(arg)

    for key, value in kwargs.items():
        print(f"{key}: {value}")

application("Marica", "Sunjevaric",
            "maricasunjevaric@gmail.com",
            "SHG",
            80000, 76000, hire_date= "February 2021", hire_day = "Monday")