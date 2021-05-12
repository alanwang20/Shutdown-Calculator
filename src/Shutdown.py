from __future__ import division
from sympy import *

class Shutdown :
    
    x, y, z = symbols('x y z')
    
   
    #create profit funciton
    cost_string = "((1/3) * q**3 + 50*q +2000)"
    p, q = symbols('p q')
    cost_expr = sympify(cost_string)
    # print(cost_expr)
    
    # multiply cost_expr by -1 
    cost_expr = Mul(-1, cost_expr)

    cost_exp = "p*q -"
    profit_function = cost_exp + cost_string
    
    profit_expr = sympify(profit_function)
    profit_expr = simplify(profit_expr)
    print(profit_function)

    # take first order conditions, calculate partial derivative of q
    
    foc_expr = diff(profit_expr, q)
    print("partical derivative: " )
    print (foc_expr)


    # find firm supply function
    results = solve(foc_expr,q) #this will give a pos and neg function
    firm_supply = results[1] #this isolates positive function
    print(firm_supply)

    # calculate ATC

    #calculate averagetotal cost function
    atc = diff(cost_expr, q)
    print("ATC")
    print (firm_supply)

    #substitute "q" value in atc for firm_supply
    adjusted_atc = atc.replace(firm_supply,p)
    print("Adjusted ATC")
    print(adjusted_atc)