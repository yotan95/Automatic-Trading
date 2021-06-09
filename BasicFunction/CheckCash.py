import pyupbit as ub

access = "??"   # private key
secret = "??"   # private key
upbit = ub.Upbit(access, secret)

print(upbit.get_balance("KRW"))  #check your chsh
