import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from PredictionPipeline import predict

temp_input = [{'processed_comment': 'i hate you', 'prediction': 'postive'}, {'processed_comment': 'i love you', 'prediction': 'postive'}]

def Predict(text): # text is a list of strings
    try:
        output = predict(text)
        return output
    except Exception as e:
        raise e

def get_count(text):
    positive_count = 0
    negative_count = 0
    for precessed_comment, prediction in text.items():
        if prediction == 'Postive':
            positive_count += 1
        else:
            negative_count += 1
    return positive_count, negative_count
    
def main():
    st.title("Youtube Sentiment Analysis")
    # text = st.text_input("Enter the text")
    number_of_top_videos = st.number_input("Enter the number of top videos", min_value = 1, max_value = 5, value = 1)
    number_of_comments = st.number_input("Enter the number of comments", min_value = 1, max_value = 100, value = 1)

    # START YOUTUBE API CALL FETCH DATA 
    text = ['i hate you', 'i love you']
    # END YOUTUBE API CALL FETCH DATA 

    # positive_count, negative_count = get_count(temp_input)
    positive_count, negative_count = 100, 50

    if st.button("Predict"):
        with st.spinner("Predicting..."):
            text = Predict(text)
            print(text)
        st.success("Predicted")
        
        fig, ax = plt.subplots()
        fig.patch.set_facecolor('#0E1117')

        categories = ['Positive', 'Negative']
        counts = [positive_count, negative_count]

        # Create histogram
        ax.bar(categories, counts, color = ['#00c878', '#fe0366'], 
               width = 0.7, align = 'center', edgecolor = 'white', linewidth = 2, 
               capsize = 10, label = 'Toxicity Percentage')
        fig.set_size_inches(10, 6)
        ax.set_facecolor('#0E1117')
        # change the color of x and y axis
        ax.spines['bottom'].set_color('white')
        ax.spines['left'].set_color('white')
        ax.tick_params(axis = 'x', colors = 'white')
        ax.tick_params(axis = 'y', colors = 'white')
        # change color of y axis label
        ax.yaxis.label.set_color('white')
        ax.spines['top'].set_visible(False)
        ax.spines['right'].set_visible(False)

        # Set labels and title
        ax.set_ylabel('Count')

        # Display plot
        st.pyplot(fig)
        
        df = pd.DataFrame(temp_input)
        df.index += 1

        st.table(df)
        
    st.text("Made by: Rounak Bachwani , Gaurav Jha, and Hetvi Gandhi")


if __name__ == "__main__":
    main()