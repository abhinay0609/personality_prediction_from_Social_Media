import streamlit as st
import joblib
from utils.preprocessor import clean_text

import streamlit as st
import joblib
from utils.preprocessor import clean_text

# ✅ Load vectorizer and model
vectorizer = joblib.load("models/tfidf_vectorizer.pkl")
model = joblib.load("models/logistic_model.pkl")

# ✅ Streamlit UI
st.set_page_config(page_title="Personality Type Predictor", page_icon="🧠")
st.title("🧠 Personality Type Predictor (MBTI)")
st.markdown("Enter a social media post or comment, and we'll predict your personality type!")

user_input = st.text_area("Write something you'd typically post online:")

if st.button("Predict Personality"):
    if not user_input.strip():
        st.warning("⚠️ Please enter some text.")
    else:
        try:
            # ✅ Clean the input
            cleaned = clean_text(user_input)
            st.write("✅ Cleaned Text:", cleaned)

            # ✅ Transform input (must be list of strings)
            vect_text = vectorizer.transform([cleaned])
            st.write("✅ Vectorized Shape:", vect_text.shape)

            # ✅ Predict
            prediction = model.predict(vect_text)
            st.success(f"🎯 Predicted Personality Type: **{prediction[0]}**")
            
            # Mapping numerical labels to MBTI full descriptions
            mbti_details = {
            0: ("ENFJ", "Warm, empathetic, responsive, and responsible. Highly attuned to the emotions, needs, and motivations of others."),
            1: ("ENFP", "Warmly enthusiastic and imaginative. See life as full of possibilities. Make connections between events and information very quickly, and confidently proceed based on the patterns they see. "),
            2: ("ENTJ", "Frank, decisive, assume leadership readily. Quickly see illogical and inefficient procedures and policies, develop and implement comprehensive systems to solve organizational problems. Enjoy long-term planning and goal setting. "),
            3: ("ENTP", "Quick, ingenious, stimulating, alert, and outspoken. Resourceful in solving new and challenging problems. Adept at generating conceptual possibilities and then analyzing them strategically."),
            4: ("ESFJ", "Warmhearted, conscientious, and cooperative. Want harmony in their environment, work with determination to establish it. Like to work with others to complete tasks accurately and on time. Loyal, follow through even in small matters. "),
            5: ("ESFP", "Outgoing, friendly, and accepting. Exuberant lovers of life, people, and material comforts. Enjoy working with others to make things happen. Bring common sense and a realistic approach to their work and make work fun."),
            6: ("ESTJ", "Practical, realistic, matter-of-fact. Decisive, quickly move to implement decisions. Organize projects and people to get things done, focus on getting results in the most efficient way possible."),
            7: ("ESTP", "Flexible and tolerant, take a pragmatic approach focused on immediate results. Bored by theories and conceptual explanations; want to act energetically to solve the problem."),
            8: ("INFJ", "Seek meaning and connection in ideas, relationships, and material possessions. Want to understand what motivates people and are insightful about others. Conscientious and committed to their firm values."),
            9: ("INFP", "Idealistic, loyal to their values and to people who are important to them. Want to live a life that is congruent with their values. Curious, quick to see possibilities, can be catalysts for implementing ideas."),
            10: ("INTJ", "Have original minds and great drive for implementing their ideas and achieving their goals. Quickly see patterns in external events and develop long-range explanatory perspectives."),
            11: ("INTP", "Seek to develop logical explanations for everything that interests them. Theoretical and abstract, interested more in ideas than in social interaction. Quiet, contained, flexible, and adaptable."),
            12: ("ISFJ", "Quiet, friendly, responsible, and conscientious. Committed and steady in meeting their obligations. Thorough, painstaking, and accurate."),
            13: ("ISFP", "Quiet, friendly, sensitive, and kind. Enjoy the present moment, what's going on around them. Like to have their own space and to work within their own time frame. Loyal and committed to their values and to people who are important to them. "),
            14: ("ISTJ", "Quiet, serious, earn success by being thorough and dependable. Practical, matter-of-fact, realistic, and responsible. Decide logically what should be done and work toward it steadily, regardless of distractions."),
            15: ("ISTP", "Tolerant and flexible, quiet observers until a problem appears, then act quickly to find workable solutions. Analyze what makes things work and readily get through large amounts of data to isolate the core of practical problems.")
}

        # Get prediction
            predicted_label = prediction[0]
            mbti_name, mbti_desc = mbti_details.get(predicted_label, ("Unknown", ""))


        # Display full personality type info
            st.success(f"🎯 **Predicted Personality Type:** {mbti_name}\n\n🧠 {mbti_desc}")





        except Exception as e:
            st.error(f"❌ Prediction failed: {str(e)}")
