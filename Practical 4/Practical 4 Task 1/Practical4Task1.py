# Probability of knowing Python
P_Python = 0.20
# Probability of knowing Java
P_Java = 0.80
# Probability of getting placed if student knows Python
P_Placed_Python = 0.90
# Probability of getting placed if student knows Java
P_Placed_Java = 0.40
# Probability that a placed student knows Python (Bayes Rule)
P_Python_Placed = (P_Placed_Python * P_Python) / ((P_Placed_Python * P_Python) + (P_Placed_Java * P_Java))
print("Probability that the student knows Python :")
print(P_Python)
print("Probability that the student knows Java :")
print(P_Java)
print("Probability that a placed student knows Python :")
print(round(P_Python_Placed * 100, 2), "%")
print("Saqlain Khan T013")
