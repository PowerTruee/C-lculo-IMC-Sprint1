def calcular_imc(peso: float, altura_cm: float) -> float:
    """Calcula o IMC a partir do peso (kg) e altura (cm)."""
    altura_m = altura_cm / 100
    return peso / (altura_m * altura_m)
 
 
def classificar_imc(imc: float) -> str:
    """Classifica o IMC de acordo com as categorias da OMS."""
    if imc < 18.5:
        return "Abaixo do peso"
    elif imc < 25:
        return "Peso normal"
    elif imc < 30:
        return "Excesso de peso"
    else:
        return "Obesidade"
 
 
def apresentar_resultado(imc: float, classificacao: str):
    """Apresenta o resultado do IMC e a classificação."""
    print(f"\nO seu IMC é: {imc:.2f}")
    print(f"Classificação: {classificacao}")
 
 
def main():
    """Bloco principal do programa."""
    continuar = True
 
    while continuar:
        # Solicitar dados ao utilizador
        peso = float(input("\nIntroduza o seu peso (em kg): "))
        altura_cm = float(input("Introduza a sua altura (em centímetros): "))
 
        # Calcular e classificar
        imc = calcular_imc(peso, altura_cm)
        classificacao = classificar_imc(imc)
 
        # Apresentar resultado
        apresentar_resultado(imc, classificacao)
 
        # Perguntar se deseja continuar
        resposta = input("\nDeseja continuar? (s/n): ").strip().lower()
        if resposta != "s":
            continuar = False
 
    print("\nAté logo!")
 
 
# ============================================================
if __name__ == "__main__":
    main()