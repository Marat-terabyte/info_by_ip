try:
	import requests						# It's module for work with HTTP requests
	from bs4 import BeautifulSoup		# It's module for 
	from colorama import Fore, init		# It's module for color text
except:
	print("execute command!\n pip install requests\n pip install beautifulsoup4\n pip install colorama")
	quit()
init()

def main():
	choice = str(input("1) Your ip addres; 2) Enter ip addres:"))

	if choice == "1" or choice == "1)":
		ip_addres = discover_IP()

	elif choice == "2" or choice == "2)":
		ip_addres = str(input("Enter ip addres:"))
	
	else:
		print(Fore.RED + "No such option!")
		quit()

	get_info_by_ip(ip_addres)

def get_info_by_ip(ip_addres):
	try:
		info = requests.get(f"http://ip-api.com/json/{ip_addres}").json()
	
	except:
		print(Fore.RED + "Check your connection!")
		quit()
	
	print("IP      : " + info.get("query"))
	print("Country : " + info.get("country"))
	print("Region  : " + info.get("regionName"))
	print("city    : " + info.get("city"))
	print("zip     : " + info.get("zip"))
	print("timezon : " + info.get("timezone"))
	print("Provider: " + info.get("org"))
	print("lat     : " + str(info.get("lat")))
	print("lon     : " + str(info.get("lon")))
		

def discover_IP():
	""" It's function for discover IP """
	response = requests.get("https://2ip.ru/").text
	soup 	 = BeautifulSoup(response, "lxml")
	ip 		 = soup.find("div", class_ = "ip").find("span").text
	
	print(Fore.RED + "Check your connection!")
	
	return ip


if __name__ == '__main__':
	main()
