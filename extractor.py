import requests
from bs4 import BeautifulSoup
import re

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}


def extract_recipe_data(url1):
    # Send a GET request to the webpage
    
    response = requests.get(url1, headers=headers)
    # Check if the request was successful
    if response.status_code == 200:
        # Parse the HTML content of the webpage
        soup = BeautifulSoup(response.content, 'html.parser')

        # Find the title of the recipe
        title = soup.find('h1').text.strip()

        # Find the ingredients
        ingredients = []
        var = soup.find_all(class_=re.compile(r'ingredients'))
        for tag in var[0]:
            if hasattr(tag, 'find_all'):
                for ul in tag.find_all('ul'):
                    for li in ul.find_all('li'):
                        ingredients.append(li.text.strip())

        # Find the preparation steps
        steps = []
        for ol in soup.find_all('ol'):
            for li in ol.find_all('li'):
                step_text = li.text.strip().replace("Serious Eats / Lorena Masso", "").replace("\n", " ")
                steps.append(step_text)

        # print("Title:", title)
        # print("Ingredients:")
        # for ingredient in ingredients:
        #     print(ingredient)
        # print("Preparation Steps:")
        # for i, step in enumerate(steps):
        #     print(f"{i+1}. {step}")

        return {
            "title": title,
            "ingredients": ingredients,
            "steps": steps,
        }
    else:
        return None

# finalll
# def show_steps(recipe_data2, counter):
#     print(f"Step {counter + 1}: {recipe_data2['steps'][counter]}")
#     next = input("1. Next Step \n 2. Previous\n")
#     return next

# finalll
# def navigate_steps(model, option, counter):
#     if option == "1":
#         if counter < len(model['steps']) - 1:
#             counter += 1
#             # show_steps(model,counter)
#         else:
#             print("You're at the last step.")
#     elif option == "2":
#         if counter > 0:
#             counter -= 1
#             # show_steps(model,counter)
#         else:
#             print("You're at the first step.")
#     return counter

# def respond(model, option):
#     if option == "1":
#         print("Ingredients:")
#         for ingredient in model['ingredients']:
#             print(ingredient)
#     elif option == "2":
#         counter = 0
#         while True:
#             next = show_steps(model, counter)
#             counter = navigate_steps(model, next, counter)
#             if next not in ["1", "2"]:
#                 break
#     elif option == "3":
#         print("More option selected. We will configure this later.")
#     else:
#         print("Invalid option. Please select a valid option.")


# finallll
# def process_input(user_input, recipe_data):
#     if user_input == "1":
#         print("Ingredients:")
#         for ingredient in recipe_data['ingredients']:
#             print(ingredient)
#     elif user_input == "2":
#         counter = 0
#         while True:
#             next = show_steps(recipe_data, counter)
#             counter = navigate_steps(recipe_data, next, counter)
#             if next not in ["1", "2"]:
#                 break
#     elif user_input == "3":
#         query = input("Enter your query")
#         query = user_input.replace(" ", "+")
#         google_search_link = f"https://www.google.com/search?q={query}"
#         youtube_search_link = f"https://www.youtube.com/results?search_query={query}"
#         print (
#             f"I found some resources that might help you with '{user_input}':\n"
#             f"* Google Search: {google_search_link}\n"
#             f"* YouTube Search: {youtube_search_link}\n"
#             # f"* Enter 'bye' to close the chat"
#         )
#     else:
#         print("Invalid option. Please select a valid option.")



# def process_input(user_input, recipe_data):
#     # Use the extracted recipe data to respond to user inputs

#     if user_input == "1":
#         print(recipe_data["ingredients"])
#         return recipe_data["ingredients"]
#     elif user_input == "2":
#         print("Preparation Steps:")
#         counter = 0
#         step1 = show_steps(recipe_data)
#         navigate_steps(recipe_data, step1)
#         return recipe_data["steps"]
#     elif user_input == "What's the next step?":
#         current_step = recipe_data["current_step"]
#         next_step = recipe_data["steps"][current_step + 1]
#         current_step+=1
#         print(next_step)
#         return next_step
    




# # model['steps'][model['current_step']]}")
# def show_steps(recipe_data2, counter1):
#     print(f"Step {recipe_data2[counter1] + 1}: {recipe_data2["steps"][counter1]}")
#     next = input("1. Next Step \n 2. Previous")
#     print(next)
#     return next
    


# def navigate_steps(model, option):
#     if option == "1":
#         if model['current_step'] < len(model['steps']) - 1:
#             model['current_step'] += 1
#             show_steps(model)
#         else:
#             print("You're at the last step.")
#     elif option == "2":
#         if model['current_step'] > 0:
#             model['current_step'] -= 1
#             show_steps(model)
#         else:
#             print("You're at the first step.")
#     # elif option == "3":
#     #     query = input("Enter your how-to query: ")
#     #     # Integrate with YouTube or online content search API
#     #     print(f"Searching for '{query}'...")
#     #     # For now, just print a placeholder message
#     #     print("Here's a tutorial on how to do that:")
#     else:
#         print("Invalid option. Please select a valid option.")







    # elif user_input == "How much of {} do I need?".format(ingredient):
    #     ingredient_quantity = recipe_data["ingredients"][ingredient]
    #     return ingredient_quantity

# user = "What are the ingredients?"
# url = "https://www.seriouseats.com/beef-braciole-recipe-7561806"

# recipe_data1 = extract_recipe_data(url)
# process_input(user,recipe_data1)


# def main():
#     user_input_url = input("Hello there, please enter the link to your address")
#     receipedata = extract_recipe_data(user_input_url)
#     user_query = input("how do you want me to help you: ingredients, preparations or more")
#     process_input(user_query,receipedata)

# if __name__ == "_main_":
#     main()