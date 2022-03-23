try:
	import socket						# It's module for work with Network
	import requests						# It's module for work with HTTP requests
	from bs4 import BeautifulSoup		# It's module for parsing HTML
	from colorama import Fore, init		# It's module for color text

except ModuleNotFoundError as error:
	print(error)
	print("execute command!\n pip install requests\n pip install beautifulsoup4\n pip install colorama")
	quit()

init()

def main():
	try:
		print("1) Your ip addres; 2) Enter ip addres; 3) Get ip addres from domain")
		print("1) Твой ip addres; 2) Ввести ip addres; 3) ip addres сайта")
		choice = str(input(">>>"))

		if choice == "1" or choice == "1)":
			ip_addres = discover_IP()

		elif choice == "2" or choice == "2)":
			ip_addres = str(input("Enter ip addres:"))
	
		elif choice == "3" or choice == "3)":
			domain = str(input("Enter site's domain (Домен сайта):"))
			ip_addres = str(socket.gethostbyname(domain))

		else:
			print(Fore.RED + "No such option!(Нет такой опции!)")
			quit()

		get_info_by_ip(ip_addres)

	except KeyboardInterrupt:
		pass

def get_info_by_ip(ip_addres):
	""" Get data from site """
	try:
		info = requests.get(f"http://ip-api.com/json/{ip_addres}").json()
	except:
		print(Fore.RED + "Check your connection!(Проверьте подключение к сети Интернет!)")
		quit()
	try:
		print("IP      : " + info.get("query"))
		print("Country : " + info.get("country"))
		print("Region  : " + info.get("regionName"))
		print("city    : " + info.get("city"))
		print("zip     : " + info.get("zip"))
		print("timezon : " + info.get("timezone"))
		print("org     : " + info.get("org"))
		print("as      : " + info.get("as"))
		print("lat     : " + str(info.get("lat")))
		print("lon     : " + str(info.get("lon")))
	except TypeError:
		print(Fore.RED + "ip address does not exist!(ip addres не существует!)")

def discover_IP():
	""" It's function for discover IP """
	try:
		response = requests.get("https://2ip.ru/").text
		soup 	 = BeautifulSoup(response, "html.parser")
		ip 		 = soup.find("div", class_ = "ip").find("span").text
	except:
		print(Fore.RED + "Check your connection!(Проверьте подключение к сети Интернет!)")
	
	return ip


if __name__ == '__main__':
	main()
