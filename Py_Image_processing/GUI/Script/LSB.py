from PIL import Image
import numpy as np
import matplotlib.pyplot as plt

# Charger l'image
img = np.array(Image.open("Images/treeBW.png"))

# Vérifier si l'image est en niveaux de gris ou en couleur
if len(img.shape) == 2:
    W, H = img.shape
    C = 1  # Image en niveaux de gris
else:
    W, H, C = img.shape  # Image en couleur

plt.imshow(img, cmap="gray")

# Demander le message
message = input("Entrez le message à cacher : ")
message += "[END]"
message = message.encode("ascii")

# Convertir le message en bits
message_bits = ''.join([format(byte, '08b') for byte in message])

# Aplatir l'image pour modifier les bits facilement
img_flat = img.flatten()

if len(message_bits) > len(img_flat):
    raise ValueError("Le message est trop long pour être caché dans l'image !")

# Modifier le bit de poids faible des pixels
for idx, bit in enumerate(message_bits):
    img_flat[idx] = (img_flat[idx] & 0b11111110) | int(bit)  # Remplace le LSB

# Reformater l'image
img_encoded = img_flat.reshape(img.shape)

# Afficher l'image encodée
plt.imshow(img_encoded, cmap="gray")
plt.show()

# **Décodage**
msg = ""
idx = 0

while len(msg) < len(message_bits) // 8:
    bits = ''.join(str(img_flat[i] & 1) for i in range(idx, idx + 8))
    msg += chr(int(bits, 2))
    idx += 8
    if msg.endswith("[END]"):
        break
    if idx >= img_flat.shape[0]:
        print("Aucun message caché trouvé.")
        break

# Afficher le message caché
print("Message caché extrait :", msg.replace("[END]", ""))
