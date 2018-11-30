import os
import json
from pprint import pprint 

user_first_input = 99

with open('data.json') as f:
	f.seek(0, os.SEEK_END)	
	if f.tell():
		f.seek(0)
		data = json.load(f)
	else:
		data = []

while user_first_input:
	try:
		user_first_input = int(input('Choose One: \n 1.Create New \n 2.Display All \n (Enter input as 1 OR 2)\n 0.Exit \n'))
	except:
		print("Please Provide valid Input \n")
		continue
		
	if user_first_input == 1:
		info_dict = {}
		id = 0
		obj_len = data.__len__()
		if obj_len > 0:
			existing_key = obj_len-1
			id = data[existing_key]['id']
		else:
			existing_key = 0		
				
		new_id = id+1
		
		print('Please provide below details: ')
		name = input('Your Name: \n')
		email = input('Your Email: \n')
		address = input('Your Address: \n')
		city = input('Your City: \n')
		contact = input('Your Contact: \n')
		
		info_dict = {'id': new_id, 'info': {'name': name, 'email': email, 'address': address, 'city': city, 'contact': contact}}
		data.append(info_dict)
		info_json = json.dumps(data)		
				
		with open("data.json", "w") as filerecords:
			filerecords.write(info_json)		
		
		print('Record added successfully \n')
		
	elif user_first_input == 2:
		user_second_input =	99
		pprint(data)
		while user_second_input:
			try:
				user_second_input = int(input('Select Action: \n 1.Delete \n 2.Update \n 0. Back \n '))
			except:
				print("Please Provide valid Input \n")
				continue
			
			if user_second_input == 1:
				try:
					user_third_input = int(input('Provide Valid Record Id to Delete:\n'))
				except:
					print("Please Provide valid Input \n")
					continue
				
				try:
					user_confirmation = input('Do You Want to Delete Record with Id (y/n):')
				except:
					print("Please Provide valid Input (y OR n) \n")
					continue
				
				success_flag = False
				if user_confirmation.lower() == 'y':
					for rec in data:
						if rec['id'] == user_third_input:
							data.remove(rec)
							success_flag = True
					
					if success_flag == True:
						info_json = json.dumps(data)
						with open("data.json", "w") as filerecords:
							filerecords.write(info_json)
											
						print ('Record Deleted \n')
					else:
						print ('Record Id invalid! \n')
			elif user_second_input == 2:
				try:
					user_third_input = int(input('Provide Valid Record Id to Update:\n'))
				except:
					print("Please Provide valid Input \n")
					continue
				
				success_flag = False
				updated_info = {}
				for rec in data:
					if rec['id'] == user_third_input:
						updated_info = rec['info']					
						success_flag = True
				
				if success_flag == True:
					print('Update details below (OR Skip): ')
					new_name = input("Existing Name: " + updated_info['name'] + "\n New Name: ")
					new_email = input("Existing Email: " + updated_info['email'] + "\n New Email: ")
					new_address = input("Existing Address: " + updated_info['address'] + "\n New Address: ")
					new_city = input("Existing City: " + updated_info['city'] + "\n New City: ")
					new_contact = input("Existing Contact: " + updated_info['contact'] + "\n New Contact: ")
					
					name = updated_info['name'] if new_name == '' else new_name
					email = updated_info['email'] if new_email == '' else new_email
					address = updated_info['address'] if new_address == '' else new_address
					city = updated_info['city'] if new_city == '' else new_city
					contact = updated_info['contact'] if new_contact == '' else new_contact
					
					new_info_dict = {'name': name, 'email': email, 'address': address, 'city': city, 'contact': contact}
					
					#pprint(data)
					for rec in data:
						if rec['id'] == user_third_input:
							rec['info'] = new_info_dict
					
					info_json = json.dumps(data)
					with open("data.json", "w") as filerecords:
							filerecords.write(info_json)
				
			elif user_second_input != 0:
				print('Invalid Selection \n')
		
		
	elif user_first_input != 0:
		print('Please Select from above \n')

print('Good Bye')
