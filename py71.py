def lbs_to_kg(weight):
    return weight*0.45

def kg_to_lbs(weight):
    return weight / 0.45

## hover your mouse onto the file that contains the orginal big file i.e. that contains the py71.py file,
# which is "Python 2023" #then right click it or click on the new file icon, then call the new file "converters.py"
# then go back to the original py71.py file, copy all the code in it, then paste the code onto the converter.py file7

### now we can delete all the code in py71.py file:
# a module should contain al relatted functions and classes

# now we want the converter into the py71.py file
# to do this write the code below at the top of py71.py file:
import converters # here do not include the extension "py" of the file "converter", also "converter" is a file.

# now to get a function from the "converter.py" file, we do:
print(converters.lbs_to_kg(70))

