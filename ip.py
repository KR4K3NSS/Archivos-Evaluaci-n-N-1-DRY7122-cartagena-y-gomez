import ipaddress

def calcular_segmento(ip, mascara):
    red = ipaddress.IPv4Network(ip + '/' + mascara, strict=False)
    primera_ip_seg = red.network_address + 1
    ultima_ip_seg = red.broadcast_address - 1
    broadcast = red.broadcast_address
    return primera_ip_seg, ultima_ip_seg, broadcast

def main():
    segmentos = {}
    
    ip = input("Ingrese la dirección IP de red: ")
    mascara = input("Ingrese la máscara de red (por ejemplo, 24): ")

    primera_ip_seg, ultima_ip_seg, broadcast = calcular_segmento(ip, mascara)

    dg = input("¿Cuál dirección del segmento será asignada al Default Gateway? ")

    segmentos[dg] = {
        "Primera IP válida": str(primera_ip_seg),
        "Última IP válida": str(ultima_ip_seg),
        "IP de broadcast": str(broadcast)
    }

    print("\nInformación guardada con éxito")

    while True:
        opcion = input("\n¿Desea buscar la información según la dirección IP del Default Gateway (DG)? (s/n): ").lower()
        if opcion != 's':
            break
        dg_buscar = input("Ingrese la dirección IP del DG a buscar: ")
        if dg_buscar in segmentos:
            print("\nInformación del segmento:")
            for clave, valor in segmentos[dg_buscar].items():
                print(clave + ": " + valor)
        else:
            print("\nLa dirección IP del DG no se encuentra en el diccionario.")

if __name__ == "__main__":
    main()
