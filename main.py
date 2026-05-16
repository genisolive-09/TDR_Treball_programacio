"""
Codi de simulació per al Treball de Recerca: 
Veles rígides i consum de combustible.
Autor: Genís Olivé Fernández
"""

def calcular_estalvi(consum_base, percentatge_estalvi, dies_navegacio):
    """
    Calcula l'estalvi de combustible anual estimat.
    """
    consum_total_sense_veles = consum_base * dies_navegacio
    estalvi_estimat = consum_total_sense_veles * (percentatge_estalvi / 100)
    consum_final = consum_total_sense_veles - estalvi_estimat
    
    return consum_total_sense_veles, estalvi_estimat, consum_final

# Paràmetres de la simulació (valors reals de mercants de gran eslora)
CONSUM_DIARI_TONES = 50       # Tones de fuel al dia
PERCENTATGE_EFICIENCIA = 20    # Estalvi estimat amb veles rígides (10-30%)
DIES_ANY = 250                 # Dies de navegació efectiva a l'any

def main():
    print("-" * 40)
    print("SIMULACIÓ D'ESTALVI ENERGÈTIC")
    print("-" * 40)
    
    total, estalvi, final = calcular_estalvi(CONSUM_DIARI_TONES, PERCENTATGE_EFICIENCIA, DIES_ANY)
    
    print(f"Consum base anual: {total:>10} tones")
    print(f"Estalvi amb veles: {estalvi:>10} tones")
    print(f"Consum final:      {final:>10} tones")
    print("-" * 40)
    
    preu_fuel_tona = 600 # Euros per tona
    estalvi_economic = estalvi * preu_fuel_tona
    
    print(f"Estalvi econòmic: {estalvi_economic:,.2f} €/any")
    print("-" * 40)

if __name__ == "__main__":
    main()
