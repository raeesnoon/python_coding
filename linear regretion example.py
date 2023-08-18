import scipy.stats as stdistance = [1 , 2 , 3 , 4 , 5]temperature = [60 , 58 , 56, 54 ,52]slope, intercept, r, p, se = st.linregress(distance,temperature)
print("Slope is ",slope)
print("Intercept is" , intercept)
print("Equation of temperature profile")equation="T(x) = "+ str(slope) + "X + " + str(intercept)
print(equation)
