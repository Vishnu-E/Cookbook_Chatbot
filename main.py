from extractor import extract_recipe_data
from conversational import process_input



def main():
    user_input_url = input("Hello there, please enter the link to your address ")
    receipedata = extract_recipe_data(user_input_url)
    user_query = input("Select an option: \n 1. Ingredients \n 2. Preparation Stepwise \n 3.All Preparation Steps \n 4. More \n Your input: ")
    process_input(user_query,receipedata)


if __name__ == "__main__":
    main()