# Anais Medina NC 0099 fecha 27 octubre 2026
import matplotlib.pyplot as plt
import numpy as mo

cant_productos=[100, 150, 200, 300, 500]
precio=[4000, 7000, 9000, 12000, 18000]

#plt.plot(cant_productos)
#plt.show()

# personaliza grafica
plt.plot(cant_productos, precio, color="green", marker="o", linestyle="dashed", linewidth=2, markersize=12) 
plt.title("Ventas de walmart NC 0099")
plt.xlabel("can product")
plt.ylabel("presios")
plt.show()


print("Anais Medina NC 0099")