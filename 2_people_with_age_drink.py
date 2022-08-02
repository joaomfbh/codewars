# kata link
# https://www.codewars.com/kata/56170e844da7c6f647000063

# Drink about

def people_with_age_drink(age):
  value = ""

  if age < 14:
    value = "drink toddy"
  elif age < 18:
    value = "drink coke"
  elif age < 21:
    value = "drink beer"
  else:
    value = "drink whisky"

  return value

