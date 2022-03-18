def cakes(recipe, available):
    stdout = []
    for i in recipe:
        try:
            component = available[i] // recipe[i]
        except KeyError:
            return 0
        stdout.append(component)
    return min(stdout)


# must return 2
print(cakes({"flour": 500, "sugar": 200, "eggs": 1}, {"flour": 1200, "sugar": 1200, "eggs": 5, "milk": 200}))
# must return 0
print(cakes({"apples": 3, "flour": 300, "sugar": 150, "milk": 100, "oil": 100}, {"sugar": 500, "flour": 2000, "milk": 2000}))
