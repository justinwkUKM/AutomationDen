#__author__ = "waqasmcbookair"

#import os to access files and folders
import os
#import re simplify strings and names using regex
import re

#use the directory where your files are located
os.chdir('/Users/twaqas/Desktop/trialFolder2')

#access each file in the folder
for f in os.listdir():
    if '.DS_Store' not in f:
    	#divide into name and extention
        f_name, f_extension = os.path.splitext(f)
        #simplify name by removing text after a specific pattern
        simplified_f_name = re.sub(r"Slide.*$", "", f_name)
        #divide the name into parts
       	f_comapny, f_title, f_number = simplified_f_name.split('-')
       	#simplify number by removing non digits
       	simplified_f_number = re.sub(r"\D+", "", f_number)
      	#simplify title by removing spaces
       	simplified_f_title =  re.sub(r"\s", "", f_title)

       	simplified_f_title = simplified_f_title.strip()
       	f_comapny = f_comapny.strip()
       	simplified_f_number = simplified_f_number.strip().zfill(2)
       	
       	print('{}-{}-{}{}'.format(simplified_f_number, f_comapny, simplified_f_title, f_extension))
       	
       	#save name as you like using string formatter
       	new_name = '{}-{}-{}{}'.format(simplified_f_number, f_comapny, simplified_f_title, f_extension)

       	#set the name of the files
       	# os.rename(f, new_name)
