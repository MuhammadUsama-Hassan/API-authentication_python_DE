import json

#***************************************************************
# Dictionary ko JSON me convert karne through json.dumps  ***********************************
Dummy_dictionary = {
    'key1': 'UsamaHassanKhan',
    'key2': 'value2',
}
type(Dummy_dictionary)    #dictionary ki type btata hai 
print(Dummy_dictionary)   #dictionary print karaega
Dummy_dictionary['key1']  #key nikalne k liye hai

usama = json.dumps(Dummy_dictionary)  # yahan dictionary to json conversion hui hai 
print(usama) 
type(usama)

#**************************************************************************
# Is code mein JSON string ko Python dictionary mein convert kiya gaya hai through json.laods  *************************************

json_Code= """{
"name": "usama",
"father_name":"riaz-ul-hassan",
"Student_id":1390,
"male": true
}"""     # triple quattion json ko show krta hai

type(json_Code) # json type bataega
print(json_Code)

new_variable= json.loads(json_Code) #json converter to dictionary
print(new_variable)
type(new_variable) # conversion k bd ab ye dictionary type show krega



#** Is code mein dummy.json file se JSON data load kiya gaya hai aur usko Python dictionary mein convert kiya gaya hai. Phir us dictionary ko print kiya gaya hai. open() function file ko read mode mein kholta hai, aur json.load() function us file ka content dictionary mein convert karta hai.***************************************************************************

file_path_json = 'dummy.json'
fp = open(file=file_path_json, mode='r')
read_data = json.load(fp=fp)
print(read_data)

# jo data file dummy.json sy uthaya th usko new file bna kr trasnfer krdya usme
with open(file='usama_dummy.json', mode='w+') as fp:
    json.dump(obj= read_data, fp=fp, indent=3) 

# ab manual data ko new file create kr k transfer kr rhe hen  
usama_variable_data = {
"name": "Roshni",
"Fname": "thripaati",
"emp_id": 13904,
"marital_status": "married"
} 
print(usama_variable_data)
type(usama_variable_data)
with open(file= 'new_dummy.json', mode='w+') as fp:
    json.dump(obj=usama_variable_data, fp=fp, indent=3)    

