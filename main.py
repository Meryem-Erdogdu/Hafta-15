import threading

def coder(number, number2, number3, number4):
    print(f'Coder ID: {number} , {number2} , {number3} , {number4}')

threads = []
for l in range(5):
    for k in range(5):
        for m in range(5):
            for n in range(5):
                t = threading.Thread(target=coder, args=(l,k,m,n))
                threads.append(t)
                t.start()
