# Author: Reem Abdou rpa5285@psu.edu
# Collaborator: Purushottam Shulka pps5338@psu.edu
# Collaborator: Tristan Zanowic tsz5030@psu.edu
# Collaborator: Andrew Torri abt5506@psu.edu

temperature = float(input("Enter temperature: "))
unit = input("Enter unit in F/f or C/c: ")
if unit == "F" or unit == "f":
   tcelsius = float((temperature - 32) * (5/9))
   print (f"{temperature}° in Fahrenheit is equivalent to{tcelsius}° Celsius.")
elif unit == "C" or unit == "c":
   tfahrenheit = float(temperature * 9/5 + 32)
   print (f"{temperature}° in Celsius is equivalent to {tfahrenheit}° Fahrenheit.")
else:
  print(f"Invalid unit({unit}).")