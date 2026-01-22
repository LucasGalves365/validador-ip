def validar_ip(ip):
    partes = ip.split(".")

    if len(partes) != 4:
        return False

    try:
        for parte in partes:
            numero = int(parte)
            if numero < 0 or numero > 255:
                return False
    except ValueError:
        return False

    return True


def classe_ip(primeiro_octeto):
    if 1 <= primeiro_octeto <= 126:
        return "A", "255.0.0.0", 16777214
    elif 128 <= primeiro_octeto <= 191:
        return "B", "255.255.0.0", 65534
    elif 192 <= primeiro_octeto <= 223:
        return "C", "255.255.255.0", 254
    elif 224 <= primeiro_octeto <= 239:
        return "D (Multicast)", "N/A", "N/A"
    elif 240 <= primeiro_octeto <= 255:
        return "E (Reservado)", "N/A", "N/A"
    else:
        return "Desconhecida", "N/A", "N/A"


def ip_privado(primeiro, segundo):
    if primeiro == 10:
        return True
    if primeiro == 172 and 16 <= segundo <= 31:
        return True
    if primeiro == 192 and segundo == 168:
        return True
    return False


def analisar_ip(ip):
    partes = ip.split(".")
    primeiro = int(partes[0])
    segundo = int(partes[1])

    classe, mascara, hosts = classe_ip(primeiro)
    privado = ip_privado(primeiro, segundo)

    print("\n--- RESULTADO DA ANÁLISE ---")
    print(f"IP: {ip}")
    print(f"Classe: {classe}")
    print(f"Máscara padrão: {mascara}")
    print(f"Hosts possíveis: {hosts}")
    print(f"Tipo: {'Privado' if privado else 'Público'}")


def menu():
    print("\n=== VALIDADOR DE IP (IPv4) ===")
    print("1 - Validar e analisar IP")
    print("0 - Sair")


def main():
    while True:
        menu()
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            ip = input("Digite o endereço IP: ")

            if validar_ip(ip):
                analisar_ip(ip)
            else:
                print("\nIP inválido!")
        elif opcao == "0":
            print("Encerrando o sistema...")
            break
        else:
            print("Opção inválida!")


main()
