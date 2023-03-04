"""
    Programme permettant de convertir une adresse IPv4 en binaire ou en décimale
"""

"""convertisseur d'addrese IPv4
__version__ = 2.0
__author__ = Mohamed Ahmed Sopio
__copyright__ = libre
"""

# Fonction pour convertir une adresse ip en binaire
def ip_to_bin(ip):
  # Séparer les octets par le point
  octets = ip.split(".")
  # Convertir chaque octet en binaire sur 8 bits
  bin_octets = [format(int(octet), "08b") for octet in octets]
  # Joindre les octets binaires par un point
  bin_ip = ".".join(bin_octets)
  return bin_ip

# Fonction pour convertir une adresse ip en décimale
def ip_to_dec(ip):
  # Séparer les octets par le point
  octets = ip.split(".")
  # Convertir chaque octet en décimal
  dec_octets = [int(octet, 2) for octet in octets]
  # Joindre les octets décimaux par un point
  dec_ip = ".".join(str(dec_octet) for dec_octet in dec_octets)
  return dec_ip

# Demander à l'utilisateur de saisir une adresse ip et le type de conversion souhaité
ip = input("Entrez une adresse IP: ")
type = input("Entrez le type de conversion (binaire ou décimale): ")

# Vérifier si le type de conversion est valide
if type == "binaire":
  # Appeler la fonction ip_to_bin et afficher le résultat
  bin_ip = ip_to_bin(ip)
  print(f"L'adresse IP {ip} en binaire est {bin_ip}.")
elif type == "décimale":
  # Appeler la fonction ip_to_dec et afficher le résultat
  dec_ip = ip_to_dec(ip)
  print(f"L'adresse IP {ip} en décimale est {dec_ip}.")
else:
  # Afficher un message d'erreur si le type de conversion est invalide
  print("Type de conversion invalide. Veuillez choisir entre binaire ou décimale.")
