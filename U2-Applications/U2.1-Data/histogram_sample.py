import matplotlib.pyplot as plt

someList = [.5,1,1.5,2,2.5,3,3.5,4,4.5,5,5.5]
plt.hist(someList, bins=[-1, -0.8,-0.5 0.0, 0.5,0.8,1])
plt.xlabel('average of tweets')
plt.ylabel('Number of Items')
plt.title('Histogram of Numbers')
plt.axis([-1.1, 1.1, 0,,50])
plt.grid(True)
plt.show()