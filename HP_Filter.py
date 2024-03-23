import numpy as np
import matplotlib.pyplot as plt

# Paramètres du signal
fréquence_signal = 5  # Hz
fréquence_échantillonnage = 50  # Hz
temps = np.arange(0, 1, 1/fréquence_échantillonnage)  # 1 seconde de signal

# Générer le signal et le bruit
signal = np.sin(2 * np.pi * fréquence_signal * temps)
bruit = 0.5 * np.random.randn(len(temps))
signal_bruité = signal + bruit

# Afficher le signal bruité
plt.plot(temps, signal_bruité)
plt.title("Signal Bruité")
plt.xlabel("Temps (s)")
plt.ylabel("Amplitude")
plt.show()

def filtre_passe_bas(signal, taille_fenêtre):
    return np.convolve(signal, np.ones(taille_fenêtre)/taille_fenêtre, mode='same')

signal_filtré = filtre_passe_bas(signal_bruité, 5)

# Afficher le signal filtré
plt.plot(temps, signal_filtré, label='Signal Filtré')
plt.plot(temps, signal, label='Signal Original', alpha=0.5)
plt.legend()
plt.title("Comparaison Signal Original et Filtré")
plt.xlabel("Temps (s)")
plt.ylabel("Amplitude")
plt.show()
