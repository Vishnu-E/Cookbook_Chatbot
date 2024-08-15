def process_input(user_input, recipe_data):
    if user_input == "1":
        print("Ingredients:")
        for ingredient in recipe_data['ingredients']:
            print(ingredient)
        ingredients11 = recipe_data.get('ingredients', [])
        return ingredients11
        
    elif user_input == "2":
        counter = 0
        while True:
            next = show_steps(recipe_data, counter)
            counter = navigate_steps(recipe_data, next, counter)
            if next not in ["1", "2"]:
                break
    elif user_input == "3":
        print("All Preparation Steps:")
        for i, step in enumerate(recipe_data['steps']):
            print(f"{i+1}. {step}")
            # return(f"{i+1}. {step}")
        preps = recipe_data.get('steps', [])
        return preps
    elif user_input == "4":
        query = input("Enter your query")
        query = query.replace(" ", "+")
        print(query)
        google_search_link = f"https://www.google.com/search?q={query}"
        youtube_search_link = f"https://www.youtube.com/results?search_query={query}"
        print (
            f"I found some resources that might help you with '{user_input}':\n"
            f"* Google Search: {google_search_link}\n"
            f"* YouTube Search: {youtube_search_link}\n"
            # f"* Enter 'bye' to close the chat"
        )
    else:
        print("Invalid option. Please select a valid option.")


def show_steps(recipe_data2, counter):
    print(f"Step {counter + 1}: {recipe_data2['steps'][counter]}")
    next = input("1. Next Step\n 2. Previous\n 3.Exit \n Your input: ")
    return next

def navigate_steps(model, option, counter):
    if option == "1":
        if counter < len(model['steps']) - 1:
            counter += 1
            # show_steps(model,counter)
        else:
            print("You're at the last step.")
    elif option == "2":
        if counter > 0:
            counter -= 1
            # show_steps(model,counter)
        else:
            print("You're at the first step.")
    elif option =="3":
        print("It was good talking to you, Byee!!")
        exit
    return counter