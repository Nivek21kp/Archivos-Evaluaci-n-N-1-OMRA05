#Script indicadora de rango VLAN
vlan=int(input("Ingresa numero de vlan: "))

if 1 <= vlan <= 99:
    print=("Vlan se encuentra en rango normal")
elif 100 <= vlan <= 199:
    print=("Vlan se encuentra en rango extendido")
else:
    print=("El numero de vlan no esta en los rangos")