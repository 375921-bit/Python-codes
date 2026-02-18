#Introduce the user to the guide
print("Welcome to the information guide for the three cities: Phoenix or Las Vegas\n")

#Create yes list
yes_answers = ["Yes","yes","Ye","ye","Y","y","Yea","yea","Yeah","yeah"]

enter = input("Would you like to learn about the cities?\n\n")

if enter in yes_answers:
  city = input("\nWhat city would you like to learn about? (Phoenix or Las Vegas)\n\n")

  if city == "Phoenix":

    #Housing in Phoenix
    print("\nPhoenix, Arizona, is the U.S.'s fifth-largest city, known as the 'Valley of the Sun' for its hot, sunny desert climate, rich Hohokam history, and modern sprawl in the Sonoran Desert. It offers a diverse economy (tech, healthcare, tourism), abundant outdoor recreation (hiking, golf), vibrant arts and culture, and a blend of suburban and urban living with a strong Mexican-American influence. Key features include its extensive canal system, diverse population, thriving job market, and unique desert landscape, though it faces challenges like extreme summer heat. \n")
    housing_phx = input("\nWould you like to see the average housing cost?\n\n")
    if housing_phx in yes_answers:
      print("\nThe average home price in Phoenix, AZ, varies slightly by source but generally hovers around the mid-$400,000s, with recent data suggesting median sale prices around $466K-$490K and average home values around $400K-$420K as of late 2025/early 2026, though the market has seen recent downward trends after significant growth. \n")
    
    #Taxes in Phoenix
    taxes_phx = input("\nWould you like to see the income, property, and sales taxes?\n\n")
    if taxes_phx in yes_answers:
      print("\nThe income tax is at a flat 2.5%, the property tax is about .56%, and the sales tax is 9.1%")
    
    #Computer Science in Phoenix
    computer_science_phx = input("\nWould you like to see the computer science salary in Phoenix?\n\n")
    if computer_science_phx in yes_answers:
      print("\nThe overall salary for computer science is around $80,000. Entry level jobs offer $60,000 to $75,000 while more experienced jobs offer $90,000 to $130,000+\n")
    
    #Cyber Security in Phoenix
    cyber_security_phx = input("\nWould you like to see the cyber security salary in Phoenix?\n\n")
    if cyber_security_phx in yes_answers:
      print("\nThe overall salary for cyber security is around $120,000 to $130,000. Entry level jobs offer $110,000 to $140,000 while more experienced jobs offer $170,000+\n\n")
    
    
  elif city == "Las Vegas":

    #Housing in Las Vegas
    print("\nLas Vegas is a world-famous desert city in Nevada, renowned as a major resort and entertainment hub known for its 24/7 gambling, vibrant nightlife, extravagant themed hotels, celebrity shows, fine dining, and shopping, centered around the iconic, flashy Las Vegas Strip, but also offering art, outdoor adventures, and a growing cultural scene beyond the casinos, serving as a global tourist destination.")
    housing_lv = input("\nWould you like to see the average housing cost?\n\n")
    if housing_lv in yes_answers:
      print("\nIn early 2026, the average home price in Las Vegas hovers around the low to mid-$400,000s, with the median sale price recently reported near $470,000 for existing homes, though values fluctuate, with some sources showing medians around $430k-$440k and average home values slightly lower. Housing costs are generally higher than the national average, and prices can vary significantly by neighborhood, with typical single-family homes ranging from $300k to over $1 million. ")
    
    #Taxes in Las Vegas
    taxes_lv = input("\nWould you like to see the income, property, and sales taxes?\n\n")
    if taxes_lv in yes_answers:
      print("\nThere is no income tax, the property tax is around .49% to .53%, and the sales tax is 8.38%")
    
    #Computer Science in Las Vegas
    computer_science_lv = input("\nWould you like to see the computer science salary in Las Vegas\n\n")
    if computer_science_lv in yes_answers:
      print("\nThe average salary for computer science is around $80,000 to $100,000. Entry level jobs offer $50,000 to $90,000 while more experienced jobs offer $100,000 to $140,000+")
    
    #Cyber Security in Las Vegas
    cyber_security_lv = input("\nWould you like to see the cyber security salary in Las Vegas\n\n")
    if computer_science_lv in yes_answers:
      print("\nThe average salary for cyber security is $126,000. Entry level jobs offer $60,000 to $80,000 while more experienced jobs offer $100,000 to $170,000+\n\n")
    

  else:
    print("\nInvalid city")