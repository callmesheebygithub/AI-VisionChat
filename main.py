import streamlit as st
from PIL import Image

def main():
    st.set_page_config(page_title="🖼️ Chat with Image", page_icon="💬", layout="wide")
    
    with st.sidebar:
        st.image("images/smarthive logo 1.PNG", width=50)
        st.title("📤 Upload Your Images")
        uploaded_files = st.file_uploader("Choose images", type=["jpg", "jpeg", "png"], accept_multiple_files=True)
        
        if uploaded_files:
            for uploaded_file in uploaded_files:
                image = Image.open(uploaded_file)
                st.image(image, caption=f"Uploaded Image: {uploaded_file.name}", use_container_width=True)
    
    st.image("images/smarthive logo 1.PNG", width=250)
    st.title("🤖 AI-Powered Chat with Image")
    
    if "messages" not in st.session_state:
        st.session_state["messages"] = []
    
    for message in st.session_state["messages"]:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])
    
    user_input = st.chat_input("💡 Ask anything about the images...")
    if user_input:
        st.session_state["messages"].append({"role": "user", "content": user_input})
        st.session_state["messages"].append({"role": "assistant", "content": user_input})
        with st.chat_message("user"):
            st.markdown(user_input)
    
if __name__ == "__main__":
    main()
