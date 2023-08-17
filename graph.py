import matplotlib.pyplot as plt

distance = [1 , 2 , 3 , 4 , 5]

temperature = [60 , 58 , 56, 54 ,52]
                

plt.xlabel("Distance")

plt.ylabel("Temperature")

plt.title("Plot of temperature over distance")

plt.grid(True)

plt.plot(distance , temperature , marker="o" , c = "red" )

plt.show()

