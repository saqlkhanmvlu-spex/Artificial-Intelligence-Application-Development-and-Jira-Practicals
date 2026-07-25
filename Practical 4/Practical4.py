# Probability of Having Disease
P_D = 0.01
# Probability of Positive test if disease exists
P_Pos_D = 0.99
# Probability of positive test if disease does not exist
P_Pos_NotD = 0.05
# Probability of not having disease
P_NotD = 1 - P_D
# Bayes Rules
P_D_Pos = (P_Pos_D * P_D) / ((P_Pos_D * P_D) + (P_Pos_NotD * P_NotD))
print("Probability that person actually has disease : ")
print(round(P_D_Pos * 100,2), "%")
print("Saqlain Khan T013")
