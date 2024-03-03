# Argument & Keyword Argument (Args,Kwargs,*args)
""" This function prints name, age,city
from an argument provided to the function."""
def user_info(name, age=0, city="Chaingmai"):

    print("{} is {} years old, from {}".format(name, age, city))
# Set all 
user_info("Greg", 27, "Bangkok")
user_info("John")
user_info(age=33, name="Kate")

def application(fname, lname, email, company, *args, **kwargs):
    salary = args[0] if args else None
    hire_date = kwargs.get("hire_date", None)
    print("{} {} works at {}. Email is {}. Salary is {}. Hire date is {}.".format(
        fname, lname, company, email, salary, hire_date))

application("Greg", "Chou", "gergchouu@gmail.com", "TeachCode.org", 40000, hire_date="April 2024")

