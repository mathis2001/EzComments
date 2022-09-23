import re
import requests
import sys

class bcolors:
	OK = '\033[92m'
	WARNING = '\033[93m'
	FAIL = '\033[91m'
	RESET = '\033[0m'
	INFO = '\033[94m'

def main():
	regex = r"<!--(.*?)-->"
	
	for line in sys.stdin:
		try:
			rq = requests.get(line.strip())

			comments = re.findall(regex, rq.text)
			allcomments=[]
			noduplicate=[]
			if not comments:
				print(bcolors.FAIL+"[!] "+bcolors.RESET+"No comment found for "+bcolors.INFO+line.strip()+bcolors.RESET)
			else:
				print(bcolors.INFO+"[*] "+bcolors.RESET+"Comments found for "+bcolors.INFO+line.strip()+bcolors.RESET)
				for comment in comments:

					allcomments.append(comment)

				for com in allcomments:
					if com not in noduplicate:
						noduplicate.append(com)

				for single_comment in noduplicate:
					print(bcolors.OK+"[+] "+bcolors.RESET+single_comment)

		except KeyboardInterrupt:
			print(bcolors.FAIL+"[!] "+bcolors.RESET+"Script canceled.")
			sys.exit(1)
		except:
			pass
try:
	main()
except Exception as e:
	print(bcolors.FAIL+"[!] "+bcolors.RESET+"A problem has occured.")
	print(bcolors.FAIL+"[!] "+bcolors.RESET+"No subdomain found.")
	print(bcolors.INFO+"[*] "+bcolors.RESET+"Error info:")
	print(e)
except KeyboardInterrupt:
        print(bcolors.FAIL+"[!] "+bcolors.RESET+"Script canceled.")
