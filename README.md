# UNO-Q-WebRadio---LCD---Modulino-BUTTONS

Voici la version 3 de mon application Web Radio sur UNO-Q
Ici il s'agit juste de faire un rappel des versions précécdentes et de comparer les 3 :

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
