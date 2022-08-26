import os

print("Per vedere i nomi delle reti vicino a te lancia questo comando da cmd -> netsh wlan show profiles ")

net=input("Inserisci il nome della rete -> ")
print("L'output della rete "+net+ " è disponibile di seguito per la password cerca la voce 'Contenuto chiave' :} -> \n")
os.system('cmd /k netsh wlan show profile name='+net+' key=clear')
