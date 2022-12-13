Fil = open("Mac.txt", 'w')
Mac = "00:00:00:"
rng_mac = int(input("Number Mac Address: "))

print("Start...")
for num in range(rng_mac):
    hex_num = hex(num)[2:].zfill(6)
    mac_t = "{}{}{}:{}{}:{}{}".format(Mac, *hex_num)
    print(mac_t)
    Fil.write(mac_t+"\n")

print("End!")
Fil.close
