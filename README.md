![Arduino App Lab](https://img.shields.io/badge/Arduino%20App%20Lab-0.7.0-blue)
![Platform](https://img.shields.io/badge/macOS-26.3.1-lightgrey)
![Target](https://img.shields.io/badge/Board-UNO%20Q-green)
![Python](https://img.shields.io/badge/Python-3.x-yellow)
![Audio](https://img.shields.io/badge/Audio-ALSA%20%2F%20mpg123-red)



# UNO-Q-WebRadio---LCD---Modulino-BUTTONS

Voici la version 3 de mon application Web Radio sur UNO-Q, 
Ici il s'agit juste de faire un rappel des versions précécdentes et de comparer les 3 :

- Version 0 :
👉 https://github.com/philippe86220/UNO-Q--WebRadio

- Version 1 :
👉 https://github.com/philippe86220/UNO-Q-WebRadio-Modulino-LCD

- Version 2  :
👉 https://github.com/philippe86220/UNO-Q-WebRadio---LCD---Modulino-BUTTONS 👉 *celle-ci*

---

## Différences entre les versions

### V0 (WebUI HTML – App Lab)

- Interface via navigateur (HTML / WebUI)
- Interaction utilisateur côté MPU
- **MCU absent ou non utilisé**
- Contrôle via API HTTP (click → Python → service Linux)

---

### V1 (logique côté MPU)

- STATE + logique métier en Python
- MCU passif (Bridge.call + affichage uniquement)
- Retour formaté (station|volume|status)
- **Centralisation complète côté MPU**

  ---
  
### V2 (logique côté MCU)

- État + logique déplacés en C++ (MCU)
- **MCU autonome (boutons + LCD + logique)**
- MPU réduit à un proxy API
- Communication via Bridge.notify

  ---
  
### Rappel rapide
- V0 = UI Web → MPU pilote
- V1 = MCU + MPU → MPU pilote
- V2 = MCU + MPU → MCU pilote

---

### Remerciements

Ces projets ont bénéficié d’échanges techniques et de réflexions d’architecture avec ChatGPT (OpenAI), notamment sur :
- la répartition des rôles MPU / MCU
- l’utilisation du Bridge
- la structuration globale du système sur UNO Q
Ces contributions concernent l’ensemble des trois approches présentées (V0, V1, V2).
