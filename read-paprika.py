import pandas as pd
import numpy as np
import sqlite3
import os

from libs.config import get_config
from libs.parse_recipe import clean_ingredients

config = get_config()
paprika_db_path = os.path.expandvars(config['paprika-db-path'])

# Establish a read-only connection to Paprika data
paprika_db = sqlite3.connect(f'file:{paprika_db_path}?mode=ro', uri=True)

paprika_df = pd.read_sql_query("SELECT * FROM recipes", paprika_db)

recipe_id = 'B8A461D8-0169-4179-B060-82D1742449B1'

sample_recipe = paprika_df[paprika_df.uid == recipe_id]

sample_ingredients = sample_recipe.ingredients.values[0]

sample_ingredients = clean_ingredients(sample_ingredients)

print(pd.DataFrame(sample_ingredients))
