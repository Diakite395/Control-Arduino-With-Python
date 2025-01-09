# pip install pyserial

import serial.tools.list_ports # type: ignore
import time

# # Fonction pour lire les données envoyées par l'Arduino
def read_from_arduino():
    try:
        if arduino.in_waiting > 0:  # Vérifier s'il y a des données disponibles
            data = arduino.readline().decode().strip()  # Lire une ligne de données
            return data
    except Exception as e:
        print(f"Erreur lors de la lecture : {e}")
    return None


ports = serial.tools.list_ports.comports()
arduino = serial.Serial()

portsList = []

# for i in ports:
#   portsList.append(str(i))
#   print(str(i))

# com = input("Select COM Port Number for Arduin #: ")

# for i in range(len(portsList)):
#   if portsList[i].startswith("COM" + str(com)):
#     use = "COM" + str(com)
#     print(use)


arduino.baudrate = 9600
arduino.port = "COM3"

arduino.open()

command = ""

while True:
    
  command = input("Arduino Command (ON/OFF/exit) #: ")
  arduino.write(command.encode('utf-8'))

  if command == "exit":
    # close arduino conneion
    arduino.close() 
    break

  reponse = read_from_arduino()

  if reponse:
    print(reponse)
      



# # Remplacez 'COM3' par le port série utilisé par votre Arduino (exemple : 'COM4' sous Windows, '/dev/ttyUSB0' sous Linux/Mac)
# arduino_port = "COM3"
# baud_rate = 9600  # Le même que dans le code Arduino

# # Initialiser la communication série
# try:
#     arduino = serial.Serial(arduino_port, baud_rate, timeout=1)
#     time.sleep(2)  # Attendre que la connexion soit stable
#     print("Connexion à l'Arduino réussie")
# except Exception as e:
#     print(f"Erreur : {e}")
#     exit()

# # Fonction pour envoyer une commande à l'Arduino
# def send_command(command):
#     try:
#         arduino.write((command + '\n').encode())  # Envoyer la commande
#         time.sleep(0.1)  # Attendre un peu pour la réponse
#         print(f"Commande envoyée : {command}")
#     except Exception as e:
#         print(f"Erreur lors de l'envoi de la commande : {e}")

# # Exemple de commandes
# send_command("ON")  # Allumer le pin 2
# time.sleep(2)       # Attendre 2 secondes
# send_command("OFF") # Éteindre le pin 2
# time.sleep(2)
# send_command("BLINK") # Faire clignoter le pin 4

# # Fermer la connexion
# arduino.close()
# print("Connexion fermée")
