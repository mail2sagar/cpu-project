import matplotlib.pyplot as plt
import psutil as p

app_name_list = []
app_name_percentage_list = []
count = 0

for process in p.process_iter():
    count = count+1

    if count <= 2:
        name = process.name()
        cpu_percentage = p.cpu_percent()
        print("Name- ",name," CPU percentage- ",cpu_percentage)

        app_name_list.append(name)
        app_name_percentage_list.append(cpu_percentage)


plt.figure(figsize=(15,7))
plt.xlabel("Min-Max CPU Comsumption")
plt.ylabel("Usage")
plt.bar(app_name_list,app_name_percentage_list,width=0.6,color=("lightblue","lightgreen"))
plt.show()