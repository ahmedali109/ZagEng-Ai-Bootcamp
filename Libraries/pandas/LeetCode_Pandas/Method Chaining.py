import pandas as pd
def findHeavyAnimals(animals: pd.DataFrame) -> pd.DataFrame:
    animalsOver = animals[animals['weight'] > 100]
    animalsInAsc = animalsOver.sort_values(['weight'] , ascending = False)
    return animalsInAsc[['name']]