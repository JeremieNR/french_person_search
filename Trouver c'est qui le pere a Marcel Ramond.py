import os
import re



directory = r'C:\Users\jerem\Downloads\deces'


for filename in os.listdir(directory):
    with open(filename, 'r') as myfile:
        
        try:
            for line in myfile:
                try:
                    full_name = re.search("^(RAMOND\*.*)\/ ", line)
                    male_female = re.search(" ([0-9])1\d{3}", line)
                    birth_year = re.search(" [0-9](1\d{3})", line)
                    birth_month = re.search(" [0-9]1\d{3}(\d{2})", line)
                    birth_day = re.search(" [0-9]1\d{5}(\d{2})", line)
                    birth_place_code = re.search(" [0-9]1\d{7}(\d{5})", line)
                    birth_place_village = re.search(" [0-9]1\d{12}([A-Z].*.[A-Z]).*[0-9]", line)
                    death_year = re.search(" [0-9]1\d{12}[A-Z].*.[A-Z].*[0-9]*\s(\d{4}).*[0-9] ", line)
                    if bool(re.search("^(RAMOND)\*.*\/ ", line)) == True:
                        try:
                            if (male_female.group(1) == "1") and (int(birth_year.group(1)) <= int(1910)) and (int(death_year.group(1)) <= int(1980)):
                                print(full_name.group(1)+" est un Homme née en "+birth_year.group(1)+"/"+birth_month.group(1)+"/"+birth_day.group(1)+" à "+birth_place_village.group(1)+", "+birth_place_code.group(1)+". Ils a donne naissance a Marcel Ramond a l'age de "+str(int(1926)-int(birth_year.group(1)))+" Ans. Ils est mort en "+death_year.group(1))
                            elif male_female.group(1) == "2":
                                next
                        except AttributeError:
                            print(line)
                except (IndexError):
                    next
        except UnicodeDecodeError:
            print("UnicodeDecodeError: " + str(myfile) + ", in file " + filename)
