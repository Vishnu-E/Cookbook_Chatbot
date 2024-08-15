import streamlit as st
from extractor import extract_recipe_data

# Function to apply custom CSS
def apply_custom_css():
    st.markdown(
        """
        <style>
        body {
            background-color: #f8f9fa;
            font-family: 'Arial', sans-serif;
        }
        .stApp {
            background-color: #BC8F8F;
        }
        img {
            width: 600px;
            height: 300px;
        }
        h1 {
            color: #343a40;
            text-align: center;
            margin-bottom: 20px;
        }
        .stButton>button {
            background-color: #007bff;
            color: white;
            border-radius: 5px;
            font-size: 16px;
            padding: 8px 16px;
            margin-top: 20px;
            transition: background-color 0.3s ease;
        }
        .stButton>button:hover {
            background-color: #0056b3;
        }
        .stTextInput>div>input {
            border-radius: 5px;
            padding: 8px;
            border: 1px solid #ced4da;
            font-size: 16px;
        }
        </style>
        """,
        unsafe_allow_html=True
    )

apply_custom_css()
# Function to display recipe data
def show_recipe(recipe_data, option):
    if recipe_data:
        if option == "Show Ingredients":
            st.subheader("Ingredients:")
            for ingredient in recipe_data['ingredients']:
                st.write(f"- {ingredient}")
        
        elif option == "Show All Steps":
            st.subheader("All Preparation Steps:")
            for i, step in enumerate(recipe_data['steps']):
                st.write(f"{i+1}. {step}")

        elif option == "Show Step-wise Preparation":
            st.subheader("Step-wise Preparation")
            counter = st.session_state.get("counter", 0)

            # Show the current step
            st.write(f"Step {counter + 1}: {recipe_data['steps'][counter]}")

            # Navigation buttons
            col1, col2, col3 = st.columns(3)
            with col1:
                if st.button("Previous"):
                    if counter > 0:
                        counter -= 1
                        st.session_state.counter = counter
            with col2:
                if st.button("Next"):
                    if counter < len(recipe_data['steps']) - 1:
                        counter += 1
                        st.session_state.counter = counter
            with col3:
                if st.button("Exit"):
                    st.session_state.counter = 0
                    st.write("It was good talking to you, Byee!!")
                    st.stop()
                    
    else:
        st.error("Failed to extract recipe data.")

# Apply custom CSS
apply_custom_css()

# Streamlit App Title
st.image("food.jpg", width=600)
st.title("Recipe Extractor")

# Input URL
url = st.text_input("Enter the recipe URL:")

if st.button("Extract Recipe"):
    if url:
        recipe_data = extract_recipe_data(url)
        st.session_state.recipe_data = recipe_data
    else:
        st.error("Please enter a valid URL.")

# Display dropdown after the recipe is extracted
if 'recipe_data' in st.session_state:
    option = st.selectbox(
        "What would you like to do?",
        ("Select an option", "Show Ingredients", "Show All Steps", "Show Step-wise Preparation", "Search Online")
    )
    
    # Display the selected option
    if option in ["Show Ingredients", "Show All Steps", "Show Step-wise Preparation"]:
        show_recipe(st.session_state.recipe_data, option)
    
    elif option == "Search Online":
        query = st.text_input("Enter your query:")
        if st.button("Search"):
            if query:
                google_search_link = f"https://www.google.com/search?q={query.replace(' ', '+')}"
                youtube_search_link = f"https://www.youtube.com/results?search_query={query.replace(' ', '+')}"
                st.write(f"[Google Search]({google_search_link})")
                st.write(f"[YouTube Search]({youtube_search_link})")
            else:
                st.error("Please enter a valid query.")
