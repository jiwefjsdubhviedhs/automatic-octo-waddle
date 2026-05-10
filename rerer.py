import math


insurance_deals = {
    "SecureFuture Fixed Annuity": {
        "type": "Fixed Annuity",
        "risk_level": "Low",
        "min_payment": 5000,
        "max_payment": 100000,
        "min_periods": 5,
        "max_periods": 30,
        "interest_rate": 0.045,  # 4.5%
        "early_withdrawal_penalty": 0.10,  # 10%
        "features": ["Guaranteed returns", "Principal protection", "Tax-deferred growth"],
        "target_customer": "Conservative investors, near-retirement"
    },
    "GrowthPlus Indexed Annuity": {
        "type": "Indexed Annuity",
        "risk_level": "Low-Medium",
        "min_payment": 10000,
        "max_payment": 250000,
        "min_periods": 7,
        "max_periods": 20,
        "interest_rate": 0.0625,  # 6.25% (capped)
        "early_withdrawal_penalty": 0.12,
        "features": ["Market-linked growth", "Downside protection", "Participation rate: 80%"],
        "target_customer": "Moderate risk tolerance, longer time horizon"
    },
    "PremierChoice Variable Annuity": {
        "type": "Variable Annuity",
        "risk_level": "Medium-High",
        "min_payment": 25000,
        "max_payment": 500000,
        "min_periods": 10,
        "max_periods": 40,
        "interest_rate": 0.085,  # 8.5% (variable)
        "early_withdrawal_penalty": 0.07,
        "features": ["Investment options", "Death benefit", "Rider options available"],
        "target_customer": "Growth-oriented, younger investors"
    },
    "RetirementSecure SPIA": {
        "type": "Immediate Annuity",
        "risk_level": "Low",
        "min_payment": 50000,
        "max_payment": None,  # No maximum
        "min_periods": 10,
        "max_periods": 0,  # Lifetime
        "interest_rate": 0.053,  # 5.3%
        "early_withdrawal_penalty": 0.15,
        "features": ["Lifetime income", "Inflation protection option", "Joint life option"],
        "target_customer": "Retirees needing guaranteed income"
    },
    "FlexSave Deferred Annuity": {
        "type": "Deferred Annuity",
        "risk_level": "Low-Medium",
        "min_payment": 3000,
        "max_payment": 150000,
        "min_periods": 3,
        "max_periods": 25,
        "interest_rate": 0.055,  # 5.5%
        "early_withdrawal_penalty": 0.08,
        "features": ["Flexible payments", "Withdrawal benefits", "Free partial withdrawals"],
        "target_customer": "Long-term savers, pre-retirement"
    },
    "HighYield Senior Annuity": {
        "type": "Fixed Annuity",
        "risk_level": "Low",
        "min_payment": 15000,
        "max_payment": 300000,
        "min_periods": 3,
        "max_periods": 10,
        "interest_rate": 0.058,  # 5.8%
        "early_withdrawal_penalty": 0.09,
        "features": ["Higher rate for seniors", "Shorter terms", "Guaranteed minimum"],
        "target_customer": "Age 60+, shorter-term savers"
    },
    "MaxGain Equity-Linked Annuity": {
        "type": "Equity-Indexed",
        "risk_level": "Medium",
        "min_payment": 20000,
        "max_payment": 400000,
        "min_periods": 8,
        "max_periods": 35,
        "interest_rate": 0.0725,  # 7.25%
        "early_withdrawal_penalty": 0.11,
        "features": ["100% participation rate", "Floor: 0%", "Cap: 12%"],
        "target_customer": "Aggressive growth with some protection"
    },
    "LegacyBuilder Wealth Annuity": {
        "type": "Variable Annuity",
        "risk_level": "Medium-High",
        "min_payment": 50000,
        "max_payment": 1000000,
        "min_periods": 15,
        "max_periods": 50,
        "interest_rate": 0.095,  # 9.5%
        "early_withdrawal_penalty": 0.07,
        "features": ["Estate planning focus", "Enhanced death benefit", "Long-term care rider"],
        "target_customer": "High net worth, legacy planning"
    },
    "Corporate Executive Elite Annuity": {
        "type": "Fixed Indexed Annuity",
        "risk_level": "Low",
        "min_payment": 100000,
        "max_payment": 2000000,
        "min_periods": 10,
        "max_periods": 25,
        "interest_rate": 0.065,
        "early_withdrawal_penalty": 0.05,
        "features": ["Bonus: 5% first year", "Nursing home waiver", "Enhanced death benefit"],
        "target_customer": "Corporate executives, high net worth"
    },
    "Millennial Wealth Builder": {
        "type": "Variable Annuity",
        "risk_level": "High",
        "min_payment": 2000,
        "max_payment": 50000,
        "min_periods": 20,
        "max_periods": 45,
        "interest_rate": 0.105,
        "early_withdrawal_penalty": 0.09,
        "features": ["Low fees (0.8%)", "Robo-advisory", "Socially responsible investing options"],
        "target_customer": "Young professionals (25-40 years old)"
    },
    "Educator's Guaranteed Plan": {
        "type": "Fixed Annuity",
        "risk_level": "Low",
        "min_payment": 5000,
        "max_payment": 75000,
        "min_periods": 12,
        "max_periods": 30,
        "interest_rate": 0.048,
        "early_withdrawal_penalty": 0.06,
        "features": ["No surrender charges after 7 years", "School tuition payment option", "403(b) compatible"],
        "target_customer": "Teachers, public sector employees"
    }
}
def recommend_insurance_deal(periods, payment, required_future_value=None, computed_rate=None):
    """
    Recommends the best insurance deal based on user inputs
    """
    suitable_deals = []
    
    for deal_name, deal_info in insurance_deals.items():
        max_payment_check = deal_info["max_payment"] if deal_info["max_payment"] is not None else float('inf')
        max_periods_check = deal_info["max_periods"] if deal_info["max_periods"] > 0 else float('inf')
        
        if (deal_info["min_payment"] <= payment <= max_payment_check and
            deal_info["min_periods"] <= periods <= max_periods_check):
            
            r = deal_info["interest_rate"]
            projected_fv = payment * (((1 + r) ** periods - 1) / r)
            
            if required_future_value and required_future_value > 0:
                efficiency = (projected_fv / required_future_value) * 100
            else:
                efficiency = (deal_info["interest_rate"] / (computed_rate or 0.05)) * 100
            
            # Calculate risk-adjusted score
            risk_score = {"Low": 100, "Low-Medium": 85, "Medium": 70, "Medium-High": 55, "High": 40}.get(deal_info["risk_level"], 50)
            
            match_score = (efficiency * 0.5) + (risk_score * 0.3)
            if required_future_value and projected_fv >= required_future_value:
                match_score += 50  # Bonus for meeting the goal
            
            suitable_deals.append({
                "name": deal_name,
                "type": deal_info["type"],
                "projected_fv": projected_fv,
                "interest_rate": r * 100,
                "risk_level": deal_info["risk_level"],
                "efficiency": efficiency,
                "risk_score": risk_score,
                "match_score": match_score,
                "features": deal_info["features"],
                "target": deal_info["target_customer"],
                "penalty": deal_info["early_withdrawal_penalty"] * 100
            })
    
    
    suitable_deals.sort(key=lambda x: x["match_score"], reverse=True)
    
    return suitable_deals[:3]  # Return top 3 recommendations

def show_recommendations(periods, payment, required_fv, computed_rate, annuity_type):
    print("\n" + "="*70)
    print("🏆 INSURANCE DEAL RECOMMENDATIONS")
    print("="*70)
    print(f"Based on your profile: {periods:.1f} periods, ₱{payment:,.2f} payment, Target: ₱{required_fv:,.2f}")
    print(f"Annuity Type: {'Annuity Due' if annuity_type == 'B' else 'Annuity Immediate'}")
    print("-"*70)
    
    recommendations = recommend_insurance_deal(periods, payment, required_fv, computed_rate)
    
    if recommendations:
        for i, deal in enumerate(recommendations, 1):
            print(f"\n📌 RECOMMENDATION #{i}: {deal['name']}")
            print(f"   ├─ Type: {deal['type']}")
            print(f"   ├─ Risk Level: {deal['risk_level']}")
            print(f"   ├─ Interest Rate: {deal['interest_rate']:.2f}%")
            print(f"   ├─ Projected Future Value: ₱{deal['projected_fv']:,.2f}")
            print(f"   ├─ Early Withdrawal Penalty: {deal['penalty']:.1f}%")
            print(f"   ├─ Target Customer: {deal['target']}")
            print(f"   └─ Key Features: {', '.join(deal['features'][:2])}")
            
            # Performance indicator
            if deal['projected_fv'] >= required_fv:
                print(f"\n   ✅ MEETS YOUR GOAL! (Efficiency: {min(deal['efficiency'], 100):.1f}%)")
                surplus = deal['projected_fv'] - required_fv
                print(f"   📈 Surplus: ₱{surplus:,.2f} above your target")
            else:
                print(f"\n   ⚠️  APPROACHING YOUR GOAL (Efficiency: {deal['efficiency']:.1f}%)")
                shortfall = required_fv - deal['projected_fv']
                print(f"   📉 Shortfall: ₱{shortfall:,.2f} below your target")
            
            
            if i == 1:
                print("   🏅 BEST MATCH FOR YOUR NEEDS!")
    else:
        print("\n❌ No suitable insurance deals found for your parameters.")
        print("   Consider adjusting your payment amount or investment period.")
        print("\n   Suggestions:")
        if payment < 5000:
            print("   • Increase your regular payment to at least ₱5,000 per period")
        if periods < 3:
            print("   • Extend your investment period to at least 3 years")
    
    print("\n" + "="*70)

def Required_Period(x,y):
    if x == '1' and y == "A":
        print("You have chosen to compute the Required Period for Annuity Immediate.")
        FV = float(input("Future Value goal (₱): "))
        PMT = float(input("Regular Payment per period (₱): "))
        r = float(input("Interest Rate (in decimals): "))
        n = math.log(1 + (FV * r / PMT)) / math.log(1 + r)
        print()
        print(f"You need {math.ceil(n)} periods to reach ₱{FV:,.2f} with ₱{PMT:,.2f} payments at the end of each period.")
        
        # Show insurance recommendations
        show_recommendations(n, PMT, FV, r, y)
        
    elif x == '1' and y == "B":
        print("You have chosen to compute the Required Period for Annuity Due.")
        FV = float(input("Future Value goal (₱): "))
        PMT = float(input("Regular Payment per period (₱): "))
        r = float(input("Interest Rate (in decimals): "))
        n = math.log(1 + (FV * r) / (PMT * (1 + r))) / math.log(1 + r)
        print()
        print(f"You need {math.ceil(n)} periods to reach ₱{FV:,.2f} with ₱{PMT:,.2f} payments at the beginning of each period.")
        
        
        show_recommendations(n, PMT, FV, r, y)

def required_payment(x,y):
    if x == '2' and y == 'A':
        print("You have chosen to compute the Required Payment for Annuity Immediate.")
        FV = float(input("Future Value goal (₱): "))
        r = float(input("Interest Rate (in decimals): "))
        n = float(input("Number of Periods (in years): "))
        # PMT = FV / [((1+r)^n - 1)/r]
        PMT = FV / (((1 + r) ** n - 1) / r)
        print()
        print(f"You need to save ₱{PMT:,.2f} for {math.ceil(n)} periods to reach ₱{FV:,.2f} at {r*100}% interest")
        
        # Show insurance recommendations
        show_recommendations(n, PMT, FV, r, y)
        
    elif x == '2' and y == 'B':
        print("You have chosen to compute the Required Payment for Annuity Due.")
        FV = float(input("Future Value goal (₱): "))
        r = float(input("Interest Rate (in decimals): "))
        n = float(input("Number of Periods (in years): "))
        PMT = FV / ((((1 + r) ** n - 1) / r) * (1 + r))
        print()
        print(f"You need to save ₱{PMT:,.2f} for {math.ceil(n)} periods to reach ₱{FV:,.2f} at {r*100}% interest")
        
        # Show insurance recommendations
        show_recommendations(n, PMT, FV, r, y)

def Required_Interest_Rate(x,y):
    if x == '3' and y == 'A':
        print("You have chosen to compute the Required Interest Rate for Annuity Immediate.")
        FV = float(input("Future Value goal (₱): "))
        PMT = float(input("Regular Payment per period (₱): "))
        n = float(input("Number of Periods: "))
        
        # Using binary search to find interest rate since it cannot be solved directly
        low, high = 0.0001, 1.0  # 0.01% to 100% interest rate range
        tolerance = 1e-10
        iterations = 0
        
        while high - low > tolerance and iterations < 1000:
            mid = (low + high) / 2
            # FV = PMT * [((1+r)^n - 1)/r]
            future_value = PMT * (((1 + mid) ** n - 1) / mid)
            
            if future_value > FV:
                high = mid
            else:
                low = mid
            iterations += 1
        
        r = (low + high) / 2
        print()
        print(f"You need an interest rate of {r*100:.4f}% to reach ₱{FV:,.2f} with ₱{PMT:,.2f} payments at the end of each period.")
        
        # Show insurance recommendations
        show_recommendations(n, PMT, FV, r, y)
        
    elif x == '3' and y == 'B':
        print("You have chosen to compute the Required Interest Rate for Annuity Due.")
        FV = float(input("Future Value goal (₱): "))
        PMT = float(input("Regular Payment per period (₱): "))
        n = float(input("Number of Periods: "))
        
        # Using binary search for Annuity Due: FV = PMT * [((1+r)^n - 1)/r] * (1+r)
        low, high = 0.0001, 1.0
        tolerance = 1e-10
        iterations = 0
        
        while high - low > tolerance and iterations < 1000:
            mid = (low + high) / 2
            future_value = PMT * (((1 + mid) ** n - 1) / mid) * (1 + mid)
            
            if future_value > FV:
                high = mid
            else:
                low = mid
            iterations += 1
        
        r = (low + high) / 2
        print()
        print(f"You need an interest rate of {r*100:.4f}% to reach ₱{FV:,.2f} with ₱{PMT:,.2f} payments at the beginning of each period.")
        
        
        show_recommendations(n, PMT, FV, r, y)

print('='*70)
print('           ANNUITY CALCULATOR WITH INSURANCE RECOMMENDATIONS')
print('='*70)
print()
print('What do you want to compute?')
print("1 - Compute Required Period")
print("2 - Compute Required Payment Amount")
print("3 - Compute Required Interest Rate")
Y = input("Type the corresponding number of the option you want to compute: ")

while Y not in ['1', '2', '3']:
    print()
    print("Invalid choice! Please enter 1, 2, or 3.")
    Y = input("Type the corresponding number of the option you want to compute: ")
print()

print('What is your Annuity Type?')
print('A – Annuity Immediate (payment at end of period)')
print('B – Annuity Due (payment at beginning of period)')
Z = input("Type the corresponding letter of the option that corresponds to your Annuity Type: ")

while Z not in ['A', 'B']:
    print()
    print("Invalid choice! Please enter A or B.")
    Z = input("Type the corresponding letter of the option that corresponds to your Annuity Type: ")

print()

if Y == '1':
    Required_Period(Y, Z)  
elif Y == '2':
    required_payment(Y, Z)
elif Y == '3':
    Required_Interest_Rate(Y, Z)

print("\nThank you for using the Annuity Calculator with Insurance Recommendations!")
