continuar = True

while continuar:

    peso = float(input("Introduza o seu peso (em kg): "))
    altura_cm = float(input("Introduza a sua altura (em centímetros): "))

    altura_m = altura_cm / 100

    imc = peso / (altura_m * altura_m)

    print(f"\nO seu IMC é: {imc:.2f}")

    if imc < 18.5:
        print("Classificação: Fora do peso normal")
    elif imc >= 18.5 and imc < 25:
        print("Classificação: Peso normal")
    else:
        print("Classificação: Fora do peso normal")

    resposta = input("\nDeseja continuar? (s/n): ").strip().lower()
    if resposta != "s":
        continuar = False

print("\nAté logo!")