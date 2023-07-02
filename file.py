data = ['deekshit', 'punith', 'darshan', 'ganesh', 'pavan']

for i in range(len(data)):
 item = data[i]
 file = open('data.txt','r')
 todo = file.readlines()
 file.close()
 file = open('data.txt','w')
 file.writelines(todo)
 file.close()
