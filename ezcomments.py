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
	regex_html = r"<!--(.*?)-->"
	regex_js = r"\/\*[\s\S]*?\*\/|([^:]|^)\/\/.*$"

	for line in sys.stdin:
		try:
			rq = requests.get(line.strip())

			comments_html = re.findall(regex_html, rq.text)
			comments_js = re.finditer(regex_js, rq.text, re.MULTILINE)
			allcomments=[]
			noduplicate=[]
			if not comments_html:
				print(bcolors.FAIL+"[!] "+bcolors.RESET+"No HTML comment found for "+bcolors.INFO+line.strip()+bcolors.RESET)
			else:
				print(bcolors.INFO+"[*] "+bcolors.RESET+"HTML comments found for "+bcolors.INFO+line.strip()+bcolors.RESET)
				for comment in comments_html:

					allcomments.append(comment)

				for com in allcomments:
					if com not in noduplicate:
						noduplicate.append(com)

				for single_comment in noduplicate:
					print(bcolors.OK+"[+] "+bcolors.RESET+single_comment)
			if not comments_js:
				print(bcolors.FAIL+"[!] "+bcolors.RESET+"No JavaScript comment found for "+bcolors.INFO+line.strip()+bcolors.RESET)
			else:
				print(bcolors.INFO+"[*] "+bcolors.RESET+"JavaScript comments found for "+bcolors.INFO+line.strip()+bcolors.RESET)
				print(comments_js)
				for comment in comments_js:
					print(bcolors.OK+"[+] "+bcolors.RESET+comment.group().strip())

		except KeyboardInterrupt:
			print(bcolors.FAIL+"[!] "+bcolors.RESET+"Script canceled.")
			sys.exit(1)
#		except:
#			pass
try:
	main()
except Exception as e:
	print(bcolors.FAIL+"[!] "+bcolors.RESET+"A problem has occured.")
	print(bcolors.FAIL+"[!] "+bcolors.RESET+"No subdomain found.")
	print(bcolors.INFO+"[*] "+bcolors.RESET+"Error info:")
	print(e)
except KeyboardInterrupt:
        print(bcolors.FAIL+"[!] "+bcolors.RESET+"Script canceled.")
