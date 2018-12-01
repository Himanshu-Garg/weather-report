'''
name - himanshu garg
roll no. - 2018337
sec - B
grp - 2
'''






# function to get weather response
def weather_response(location, API_key='cf382a27205f5270517df284a025cd4d'):
	
	import urllib.request
	from urllib.request import urlopen

	urll='http://api.openweathermap.org/data/2.5/forecast?q=' + 	location + '&APPID='+ API_key;

	
	with urllib.request.urlopen(urll, data=None) as response:
		for line in response:
			return line	




# function to check for valid response 
def has_error(location,json):
		
	#for making 1st letter of location capital

	firstletter=location[0]
	rest=location[1::]
	location=firstletter.upper() + rest


	search_string=',"name":"' + location + '",'
	
	json=str(json)
	jsonn=json[-100::+1]

	if search_string in jsonn:
		return False
	else:
		return True	






def get_temperature (json, n=0, t="03:00:00"):
	# write your code 
	import datetime
	
	date = datetime.date.today() + datetime.timedelta(days=n)
	date=str(date)
	
	str_to_find='"dt_txt":"' + date + ' ' + t +'"'

	json=str(json)

	
	indexx=json.index(str_to_find)
	string=json[indexx::-1]
	
	indexxx=string.index(':"td"{')
	
	string=string[indexxx::-1]
	
	what_to_find1 = ':{"temp":'
	what_to_find2 = ',"temp_min":'
	a=string.index(what_to_find1)
	b=string.index(what_to_find2)
	
	
	ans=string[a+9:b]
	return float(ans)









def get_humidity(json, n=0, t="03:00:00"):
	# write your code 
	import datetime
	
	date = datetime.date.today() + datetime.timedelta(days=n)
	date=str(date)
	
	str_to_find='"dt_txt":"' + date + ' ' + t +'"}'

	json=str(json)

	
	indexx=json.index(str_to_find)
	string=json[indexx::-1]
	
	indexxx=string.index(':"td"{')
	
	string=string[indexxx::-1]
	
	what_to_find1 = ',"humidity":'
	what_to_find2 = ',"temp_kf":'
	a=string.index(what_to_find1)
	b=string.index(what_to_find2)
	
	
	ans=string[a+12:b]
	return float(ans)



	





def get_pressure(json, n=0, t="03:00:00"):
	# write your code 
	import datetime
	
	date = datetime.date.today() + datetime.timedelta(days=n)
	date=str(date)
	
	str_to_find='"dt_txt":"' + date + ' ' + t +'"}'

	json=str(json)

	
	indexx=json.index(str_to_find)
	string=json[indexx::-1]
	
	indexxx=string.index(':"td"{')
	
	string=string[indexxx::-1]
	
	what_to_find1 = ',"pressure":'
	what_to_find2 = ',"sea_level":'
	a=string.index(what_to_find1)
	b=string.index(what_to_find2)
	
	
	ans=string[a+12:b]
	return float(ans)





def get_wind(json, n=0, t="03:00:00"):
	# write your code 
	import datetime
	
	date = datetime.date.today() + datetime.timedelta(days=n)
	date=str(date)
	
	str_to_find='"dt_txt":"' + date + ' ' + t +'"}'

	json=str(json)

	
	indexx=json.index(str_to_find)
	string=json[indexx::-1]
	
	indexxx=string.index(':"td"{')
	
	string=string[indexxx::-1]
	
	what_to_find1 = '"wind":{"speed":'
	what_to_find2 = ',"deg'
	a=string.index(what_to_find1)
	b=string.index(what_to_find2)
	
	
	ans=string[a+16:b]
	return float(ans)
 






def get_sealevel(json, n=0, t="03:00:00"):
	# write your code
	import datetime
	
	date = datetime.date.today() + datetime.timedelta(days=n)
	date=str(date)
	
	str_to_find='"dt_txt":"' + date + ' ' + t +'"}'

	json=str(json)

	
	indexx=json.index(str_to_find)
	string=json[indexx::-1]
	
	indexxx=string.index(':"td"{')
	
	string=string[indexxx::-1]
	
	what_to_find1 = ',"sea_level":'
	what_to_find2 = ',"grnd_level'
	a=string.index(what_to_find1)
	b=string.index(what_to_find2)
	
	
	ans=string[a+13:b]
	return float(ans)

'''

loc = input('Enter the location : ')
json = weather_response(loc)
days = int(input('enter no. of days : '))
temp = get_temperature(json,days)
print(temp)
humidity = get_humidity(json,days)
print(humidity)
pressure = get_pressure(json,days)
print(pressure)
wind = get_wind(json,days)
print(wind)
sealevel = get_sealevel(json,days)
print(sealevel)

'''
