def validar_ip(ip):
    partes = ip.split(".")

    if len(partes) != 4:
        return False

    for parte in partes:
        if not parte.isdigit():
            return False

        numero = int(parte)
        if numero < 0 or numero > 255:
            return False

    return True


def classe_ip(ip):
    primeiro_octeto = int(ip.split(".")[0])

    if 1 <= primeiro_octeto <= 126:
        return "A", "255.0.0.0"
    elif 128 <= primeiro_octeto <= 191:
        return "B", "255.255.0.0"
    elif 192 <= primeiro_octeto <= 223:
        return "C", "255.255.255.0"
    elif 224 <= primeiro_octeto <= 239:
        return "D (Multicast)", "N/A"
    elif 240 <= primeiro_octeto <= 255:
        return "E (Reservado)", "N/A"
    else:
        return "Desconhecida", "N/A"


def main():
    print("=== VALIDADOR DE IP (IPv4) ===")
    ip = input("Digite um endereço IP: ")

    if validar_ip(ip):
        classe, mascara = classe_ip(ip)
        print("\nIP válido!")
        print(f"Classe do IP: {classe}")
        print(f"Máscara padrão: {mascara}")
    else:
        print("\nIP inválido!")


main()
