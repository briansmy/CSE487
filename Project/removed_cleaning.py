def calculate_mpy(df):
    if df.YearSold == df.Year:
        return df.Mileage
    else:
        return df.Mileage/(df.YearSold-df.Year)

def compare_num(a, b):
    e = 1*10**-6
    return (a-b)<e

# cars = cars.assign(e=lambda df: df.Mileage if compare_num(df.YearSold,df.Year) else df.Mileage/(df.YearSold-df.Year)).rename(columns={"e":"MilesPerYear"})