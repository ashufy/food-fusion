import requests

API_KEY = 'a906401f3c474961996f5e86a56c8dad'  # Put your Spoonacular API key here

def search_recipes(ingredients, category):
    query = ','.join(ingredients)
    if category == "veg":
        url = (
            f"https://api.spoonacular.com/recipes/complexSearch"
            f"?includeIngredients={query}&diet=vegetarian&number=15&apiKey={API_KEY}"
            f"&addRecipeInformation=true"
        )
        data = requests.get(url).json()
        return [
            {
                "name": r["title"],
                "link": f"https://spoonacular.com/recipes/{'-'.join(r['title'].lower().split())}-{r['id']}",
                "image": r.get("image")
            }
            for r in data.get("results", [])
        ]
    else:
        url = (
            f"https://api.spoonacular.com/recipes/findByIngredients"
            f"?ingredients={query}&number=15&ranking=1&ignorePantry=true&apiKey={API_KEY}"
        )
        data = requests.get(url).json()
        return [
            {
                "name": r["title"],
                "link": f"https://spoonacular.com/recipes/{'-'.join(r['title'].lower().split())}-{r['id']}",
                "image": r.get("image")
            }
            for r in data
        ] if isinstance(data, list) else []
