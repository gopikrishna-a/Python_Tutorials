""" The following function return the equivalent Integer value for the given IPv4 Address If the given IP address is Invalid Then it will returns Invalid message"""



def Ipv4_to_integer(address):
    address = address.split(".")
    if len(address) == 4:
        result = (int(address[0]) * (256 ** 3)) + (int(address[1]) * (256 ** 2)) + (int(address[2]) * 256) + int(address[3])
        if result <= (2 ** 32):
            return result
    else:
        return False

    
if __name__ == '__main__':
    address = input("Enter IPv4 Address: ")
    res = Ipv4_to_integer(address)
    if res:
        print(f"The Integer value for {address} is: {res}")
    else:
        print("You have Entered an Invalid Ipv4 Address")
