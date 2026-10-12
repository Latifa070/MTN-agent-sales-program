
from restaurant import Restaurant as r

my_res = r("Buka Restaurant", "Traditional West African cuisine")
restaurant1 = my_res("Buka Restaurant", "Traditional West African cuisine")
my_res.describe_restaurant()
print(" ")


restaurant2 = my_res(" Santoku", "Japanese cuisine ")
restaurant2.describe_restaurant()

print(" ")
restaurant2 = my_res("Asanka Local Restaurant", "Traditional Ghanaian cuisine")
restaurant2.describe_restaurant()