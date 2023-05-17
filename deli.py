arepa_orders = ['reina pepiada', 'pabellón', 'queso', 'de tajadas', 'dominó','pelúa', 'catira', 'jamón y queso', 'queso', 'carne molida', 'queso']

finished_arepas = []

while 'queso' in arepa_orders:
      arepa_orders.remove('queso')

print("---- Orders ---")
for arepa in arepa_orders:
        print(f'The arepa {arepa} is in process.')

print('\n--- Finished orders ---')
while arepa_orders:
   arepa = arepa_orders.pop()

   finished_arepas.append(arepa)

finished_arepas.reverse()
for arepa in finished_arepas:
        print(f'The arepa {arepa} is ready to eat.')
    


    

