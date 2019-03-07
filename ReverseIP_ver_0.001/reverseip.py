import requests
import sys

class ReverseIP():


	def IP_count(Domain):
		url = "https://domains.yougetsignal.com/domains.php"
		payload = {
			"remoteAddress": Domain,
			"key": "",
			"_": ""
		}

		res = requests.post(url, data=payload, headers={"User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36"})
		api = res.json()

		return api["domainCount"]


	def main(Domain):


		url = "https://domains.yougetsignal.com/domains.php"
		payload = {
			"remoteAddress": Domain,
			"key": "",
			"_": ""
		}

		res = requests.post(url, data=payload, headers={"User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36"})
		api = res.json()

		"""print(
		Found {} domain hosted on the same web server as {} ({}).
		.format(api["domainCount"], api["remoteAddress"], api["remoteIpAddress"]))"""
		for lst in api.get("domainArray", []):
			return lst[0]


if __name__ == "__main__":
	main()
