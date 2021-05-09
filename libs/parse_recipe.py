def clean_ingredients(ingredients_str):

    """
    convert a newline separated string of ingredients into a list of
    ingredients

    each element of the output list will follow a [quantity, unit, name]
    convention
    """

    valid_units = ['TBSP', 'TSP', 'OZ', 'CUP', 'CLOVE', 'LARGE', 'MEDIUM']
    superfluous_terms = ['CHOPPED', 'FRESH']

    ingredients = ingredients_str.upper().split('\n')

    # pass 1: the first character in the string must be numeric
    ingredients = [i for i in ingredients if i[0].isnumeric()]

    # pass 2: drop comments from the string. Comments must be separated
    # by a comma
    ingredients = [i.split(',')[0] for i in ingredients]

    # pass 3: split ingredients into [quantity, unit, name] format
    ingredients = [parse_ingredient_str(i, valid_units) for i in ingredients]

    # pass 4: drop elements that are not a list with three elements
    # and if the first element is not a float
    ingredients = [i for i in ingredients if (isinstance(i, list)) & (isinstance(i[0], float))]

    # pass 5: drop superflous terms from the ingredient column
    ingredients = [drop_superfluous(i, superfluous_terms) for i in ingredients]

    return ingredients
    
def convert_to_float(frac_str):

    """
    convert a fraction stored in a string into a float
    Credit: https://stackoverflow.com/a/30629776
    """

    try:
        
        return float(frac_str)

    except ValueError:
        
        num, denom = frac_str.split('/')
        
        try:
            
            leading, num = num.split(' ')
            
            whole = float(leading)
        
        except ValueError:
            
            whole = 0
        
        frac = float(num) / float(denom)
        
        return whole - frac if whole < 0 else whole + frac

def parse_ingredient_str(item, units):
    
    """ 
    split an ingredient string into [quantity, unit, ingredient] format
    by splitting the string on a valid unit of measurement
    """
   
    output = None

    for unit in units:
        
        if unit in item:
        
            unit_positon = item.find(unit)
            
            output = [
                convert_to_float(item[:unit_positon-1]), 
                unit, 
                item[unit_positon+len(unit)+1:]
            ]
            
            return output
            exit
            
    return output

def drop_superfluous(ingredient, slist):

    """
    remove terms that describe the ingredient or an action performed on
    and ingredient that does not affect the weight
    """

    output = ingredient
    
    for s in slist:
        
        output[2] = output[2].replace(s, '').strip()
        
    return output
