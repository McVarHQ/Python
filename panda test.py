
import pandas as pd
std_dict = {"Reg.No":[1,2,3],"Name":['Amuthan', 'Nithin', 'Punitha'],"English":[85, 85, 84], "Maths":[93, 91, 95], "Chemistry": [91, 89, 89], "Biology":[88, 81, 90]}
std_tab=pd.DataFrame(std_dict)
print(std_tab)