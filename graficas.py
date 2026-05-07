import matplotlib as pl

class Graficas:
    def barras(self, data):
        data["POSICION"] = data["POSICION"].astype(int)
        fig, ax = pl.subplots()
        ax.bar(range(len(data["NOMBRE"])), data["POSICION"])
        ax.set_xlabel("NOMBRE")
        ax.set_ylabel("POSICION")
        ax.set_xticks(range(len(data["NOMBRE"])))
        ax.set_xticklabels(data["NOMBRE"], rotation=45, ha='right')
        for i, valor in enumerate(data["POSICION"]):
            ax.text(i, valor, str(valor), ha='center', va='bottom')
        ax.set_title("POSICIÓN por NOMBRE")
        pl.tight_layout()
        pl.show()