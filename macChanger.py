import subprocess

def changeMACAddress(interface, macAddr):
    subprocess.call(["ifconfig",interface,"down"])
    subprocess.call(["ifconfig",interface,"hw","ether",macAddr])
    subprocess.call(["ifconfig",interface,"up"])

def main():
    interface = str(input('Ingrese a la interfaz para cambiar la dirección MAC de: '))
    newMACAddr = input('Ingrese la dirección MAC para cambiar a: ')

    before = subprocess.check_output(["ifconfig",interface])
    changeMACAddress(interface, newMACAddr)
    after = subprocess.check_output(["ifconfig",interface])

    if(before == after):
        print("[-] MAC Address Change Fallo")
    else:
        print('[+] Cambio de dirección MAC con éxito')

main()
