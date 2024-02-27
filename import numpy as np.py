import numpy as np
import matplotlib.pyplot as plt

N = 100  # Longueur de la séquence
n = np.arange(N)
nu_values = np.linspace(-1, 2, 1000)  # Valeurs de nu pour l'intervalle donné

# Calcul de la TFD pour chaque valeur de nu
X = np.zeros_like(nu_values, dtype=np.complex128)
for i, nu in enumerate(nu_values):
    X[i] = np.sum(np.exp(1j * 2 * np.pi * 0.2 * n) * np.exp(-1j * 2 * np.pi * nu * n / N))

# Tracer le module de la TFD
plt.figure(figsize=(10, 6))
plt.plot(nu_values, np.abs(X))
plt.title('Module de la TFD de x(n)')
plt.xlabel('Fréquence (nu)')
plt.ylabel('|X(nu)|')
plt.grid(True)
plt.show()
