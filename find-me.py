import requests
from colorama import Fore
import os
from googlesearch import *


req = requests.session()


try:
    os.system('cls')
    os.system('clear')
except:
    pass

print(Fore.RED+'''


███████╗██╗███╗   ██╗██████╗       ███╗   ███╗███████╗
██╔════╝██║████╗  ██║██╔══██╗      ████╗ ████║██╔════╝
█████╗  ██║██╔██╗ ██║██║  ██║█████╗██╔████╔██║█████╗  
██╔══╝  ██║██║╚██╗██║██║  ██║╚════╝██║╚██╔╝██║██╔══╝  
██║     ██║██║ ╚████║██████╔╝      ██║ ╚═╝ ██║███████╗
╚═╝     ╚═╝╚═╝  ╚═══╝╚═════╝       ╚═╝     ╚═╝╚══════╝

            MAKE BY ---> @D_5TR
            TEAM ---> @ZER0ONE_01 

''')


user = input(Fore.GREEN+'[#] ENTER USER NAME :')

# tik tok search :

url_tik = 'https://www.tiktok.com/@{}?lang=en'.format(user)

req_tik = requests.get(url_tik).status_code

if req_tik == 200:
    print(Fore.RED+'[+] Found in tik tok >>>', user)

elif req_tik == 404:
    print(Fore.RED+'[!] Not found in tik tok !')

# git hub search :

url_git = 'https://github.com/{}'.format(user)

req_git = requests.get(url_git).status_code

if req_git == 200:
    print(Fore.WHITE+'[+] Found in github >>>', user)

elif req_git == 404:
    print(Fore.WHITE+'[!] Not found in github !')

# instagram search :

url_insta = 'https://www.instagram.com/accounts/login/ajax/'

header_insta =  {
    'Host': 'www.instagram.com',
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:78.0) Gecko/20100101 Firefox/78.0',
    'Accept': '*/*',
    'Accept-Language': 'en-US,en;q=0.5',
    'Accept-Encoding': 'gzip, deflate, br',
    'X-CSRFToken': 'exINrXLQ1BDfCXifnuf6EcABRbSG90rx',
    'X-Instagram-AJAX': '3c8826838272',
    'X-IG-App-ID': '936619743392459',
    'X-IG-WWW-Claim': '0',
    'Content-Type': 'application/x-www-form-urlencoded',
    'X-Requested-With': 'XMLHttpRequest',
    'Content-Length': '266',
    'Origin': 'https://www.instagram.com',
    'Connection': 'keep-alive',
    'Referer': 'https://www.instagram.com/accounts/login/',
    'Cookie': 'csrftoken=exINrXLQ1BDfCXifnuf6EcABRbSG90rx; mid=YHGphAAEAAGNc8DOkyoalodRtWTT; ig_did=1ACE336F-1748-4DD7-9E25-25B0191B9467; ig_nrcb=1',
    'TE': 'Trailers',

}

data_insta = {
    'username': user,
    'enc_password': '#PWD_INSTAGRAM_BROWSER:10:1618061720:AeZQAE0i5FZFh/6BiPkWOnqmt4K4ad7EBOv6k4dzL+5iOHFo6cDa6VEU5XAaWRZPHwIl3bmc3xCsR/WRhWTDH6CGSZ7+GQbvVH7QPJN7ylWHSuFDHjzB70buLzlKrhoxaIf1izk7g5nsSgk=',
    'queryParams': '{}',
    'optIntoOneTap': 'false',
}

req_insta = requests.post(url_insta, headers=header_insta, data=data_insta).status_code

if req_insta == 200 :
    print(Fore.MAGENTA+'[+] Found in instagram >>>',user)

elif req_insta == 404 :
    print(Fore.BLUE+'[!] Not Found in instagram !')

# snapchat search :

url_sanp = 'https://accounts.snapchat.com/accounts/login'


header_snap = {
    'Host': 'accounts.snapchat.com',
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:78.0) Gecko/20100101 Firefox/78.0',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
    'Accept-Language': 'en-US,en;q=0.5',
    'Accept-Encoding': 'gzip, deflate, br',
    'Referer': 'https://accounts.snapchat.com/',
    'Content-Type': 'application/x-www-form-urlencoded',
    'Content-Length': '3070',
    'Origin': 'https://accounts.snapchat.com',
    'Connection': 'keep-alive',
    'Cookie': 'xsrf_token=yT5wDFqV8fFOf4H_DHwClg; web_client_id=291e1535-4411-4e1d-a7eb-5cbf01098100; _sca={%22cid%22:%22329dddfc-849b-49f2-9d11-d0c06515c71d%22%2C%22token%22:%22v1.key.2021-03-06_0mryaaW4.iv.G5G85EtkpUGZtvxS.PwHGAwx92PIB+rfReHOkL3KqZblbAeKW4Wfo46xoXmLQSBVlibXu9lXGLNe+GoQaeVlA/OG1Xh13ONIRf9WavNGlv66gaeDo8U0Y9PEyJUUmJg6K%22}; _ga=GA1.2.1998040131.1618067757; _gid=GA1.2.509483225.1618067757; sc-cookies-accepted=true; Preferences=true; Performance=true; Marketing=true; _gat_UA-41740027-4=1; _scid=dd6929ce-6b4c-4cb4-9a19-cd44cc8d17f4; sc_at=v2|H4sIAAAAAAAAAE3GwRGAMAgEwIqYOQhwxG40wSpSvF/3tdsaD3oJdLziMUuqkbLag0beRhx1XJpaSDLq/IoPy7NlrkAAAAA=; _sctr=1|1618027200000; _gali=login_form',
    'Upgrade-Insecure-Requests': '1',
    'TE': 'Trailers',
}

data_snap = {
    "username":user,
    "password":"qswqswqsqsqw23",
    "xsrf_token":"yT5wDFqV8fFOf4H_DHwClg",
    "continue":"https://accounts.snapchat.com/accounts/welcome",
}

req_snap = requests.post(url_sanp, headers=header_snap, data=data_snap).status_code

if req_snap == 200 :
    print(Fore.LIGHTYELLOW_EX+'[+] Found in snapchat >>>',user)

elif req_snap == 404 :
    print(Fore.LIGHTYELLOW_EX+'[!] Not Found in snapchat !')

# tellonyom search :

url_tel = 'https://tellonym.me/{}'.format(user)

req_tel = requests.get(url_tel).status_code

if req_tel == 200 :
    print(Fore.MAGENTA+'[+] Found in tellonym >>>',user)

elif req_tel == 404 :
    print(Fore.MAGENTA+'[!] Not Found in tellonym !')

# twitter search :

def twitter():
    urltwit = 'https://tweeterid.com/ajax.php'
    headertwit = {
        'Accept': '/',
        'Accept-Encoding': 'gzip, deflate, br',
        'Accept-Language': 'ar',
        'Connection': 'keep-alive',
        'Content-Length': '9',
        'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
        'Cookie': '__utma=116903043.1318232014.1614775995.1614775995.1614775995.1; __utmc=116903043; __utmz=116903043.1614775995.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none); __utmt=1; __utmb=116903043.1.10.1614775995; __gads=ID=d7647a854bea65be-22c04e79f1a600a4:T=1614776057:RT=1614776057:S=ALNI_Mbf9fK4B3inAKAT1xrr-qkaEx5NEA',
        'Host': 'tweeterid.com',
        'Origin': 'https://tweeterid.com',
        'Referer': 'https://tweeterid.com/',
        'sec-ch-ua': '"Google Chrome";v="89", "Chromium";v="89", ";Not A Brand";v="99"',
        'sec-ch-ua-mobile': '?0',
        'Sec-Fetch-Dest': 'empty',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'same-origin',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.72 Safari/537.36',
        'X-Requested-With': 'XMLHttpRequest'
    }
    datatwit = {
        'input': f'{user}'
    }
    req_twitter = req.post(urltwit, headers=headertwit, data=datatwit).status_code
    if req_twitter == 200 :
        print(Fore.BLUE+'[+} Found in twitter >>>',user)

    elif req_twitter == 404 :
        print(Fore.BLUE+'[!] Not found in twitter !')

twitter()

# tellonym search :

def tellonym():
    urltell = f'https://tellonym.me/{user}'
    headertell = {
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,/;q=0.8,application/signed-exchange;v=b3;q=0.9',
        'accept-encoding': 'gzip, deflate, br',
        'accept-language': 'en-US,en;q=0.9',
        'cache-control': 'max-age=0',
        'cookie': '__cfduid=d9a45d5a0d1610e2a1abf30dac99aa7681613198934; _ga=GA1.2.1551905763.1613198948; _gid=GA1.2.767379040.1613198948; __cf_bm=ee7ac75044152eb1d2ad2f130402990e23eb0cda-1613232593-1800-AQ08xpweTVOHARq3LOG08YITD6T71cgZNqq41jhl8gtsnAg3eEVY5jwwMSOZloDO+EAv3V2SX2xaOSJKBnM5cBEPYNza54sWGauQeMsRKPnrnKMf2jKcta+uoo5ZWQV9ag==; _gat=1; __rtgt_sid=kl3x176qgjlsv2',
        'sec-ch-ua': '"Chromium";v="88", "Google Chrome";v="88", ";Not A Brand";v="99"',
        'sec-ch-ua-mobile': '?0',
        'sec-fetch-dest': 'document',
        'sec-fetch-mode': 'navigate',
        'sec-fetch-site': 'none',
        'sec-fetch-user': '?1',
        'upgrade-insecure-requests': '1',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.150 Safari/537.36',
    }
    req_tel = req.get(urltell, headers=headertell).status_code

    if req_tel == 200:
        print(Fore.MAGENTA+'[+] Found in telllonym >>>',user)
    elif req_tel == 404:
        print(Fore.MAGENTA+'[!] Not found in tellonym !')

tellonym()

# zoomerang search :

def zoomerang():
    urlzoomer = f'https://us-central1-zoomerang-dcf49.cloudfunctions.net/apiv2/v2/user/short?username={user}'
    headerzoomer = {
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        'accept-encoding': 'gzip, deflate, br',
        'accept-language': 'en-US,en;q=0.9',
        'cache-control': 'max-age=0',
        'if-none-match': 'W/"f8-Y4OTW9r4NK14xQ+V9hO/LQ9dyFY"',
        'sec-ch-ua': '"Google Chrome";v="89", "Chromium";v="89", ";Not A Brand";v="99"',
        'sec-ch-ua-mobile': '?0',
        'sec-fetch-dest': 'document',
        'sec-fetch-mode': 'navigate',
        'sec-fetch-site': 'none',
        'sec-fetch-user': '?1',
        'upgrade-insecure-requests': '1',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.72 Safari/537.36'
    }
    send = req.get(urlzoomer, headers=headerzoomer)
    if ('"message":"user not found"') in send.text:
        print(Fore.WHITE+'[!] Not Found in zoomerang !')
    else:
        print(Fore.WHITE+'[+] Found in zoomerang >>>',user)

zoomerang()

# google search :

user_plus = 'inurl:'+user

user_plus2 = 'intext:'+user

num = 1

for google in search(user_plus, stop=10) :

    print(num,'-',google)

    num = num + 1
for googles in search(user_plus2, stop=10):
    print(num,'-',googles)

    num = num + 1





