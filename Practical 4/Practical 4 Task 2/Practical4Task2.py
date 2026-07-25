# Probability of Blue taxi
P_Blue = 0.15
# Probability of Green taxi
P_Green = 0.85
# Probability that witness says Blue if taxi is actually Blue
P_SaysBlue_Blue = 0.80
# Probability that witness says Blue if taxi is actually Green
P_SaysBlue_Green = 0.20
# Bayes Rule
P_Blue_SaysBlue = (P_SaysBlue_Blue * P_Blue) / (
    (P_SaysBlue_Blue * P_Blue) + (P_SaysBlue_Green * P_Green)
)
print("Probability that taxi is actually Blue :")
print(round(P_Blue_SaysBlue * 100, 2), "%")
print("Saqlain Khan T013")
