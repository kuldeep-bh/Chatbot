import streamlit as st
from nltk.chat.util import Chat, reflections

# Define chatbot pairs
pairs = [
    [
        r"(.*)my name is (.*)",
        ["Hello %2, How are you today ?",]
    ],
    [
        r"(.*)help(.*) ",
        ["I can help you ",]
    ],
    [
        r"(.*) your name ?",
        ["My name is thecleverprogrammer, but you can just call me robot and I'm a chatbot.",]
    ],
    [
        r"how are you (.*) ?",
        ["I'm doing very well", "I am great !"]
    ],
    [
        r"sorry (.*)",
        ["It's alright", "It's OK, never mind that",]
    ],
    [
        r"i'm (.*) (good|well|okay|ok)",
        ["Nice to hear that", "Alright, great !",]
    ],
    [
        r"(hi|hey|hello|hola|holla)(.*)",
        ["Hello", "Hey there",]
    ],
    [
        r"what (.*) want ?",
        ["Make me an offer I can't refuse",]
    ],
    [
        r"(.*)created(.*)",
        ["Kuldeep created me using Python's NLTK library", "Top secret ;)",]
    ],
    [
        r"(.*) (location|city) ?",
        ['Hyderabad, India',]
    ],
    [
        r"(.*)raining in (.*)",
        ["No rain in the past 4 days here in %2", "In %2 there is a 50% chance of rain",]
    ],
    [
        r"how (.*) health (.*)",
        ["Health is very important, but I am a computer, so I don't need to worry about my health",]
    ],
    [
        r"(.*)(sports|game|sport)(.*)",
        ["I'm a very big fan of Cricket",]
    ],
    [
        r"who (.*) (Cricketer|Batsman)?",
        ["Kuldeep Singh"]
    ],

    # ⛺ Camping-related questions below
    [
        r"(.*)camping(.*)tips(.*)",
        ["Always pack light, carry a first-aid kit, and never forget your flashlight!", "Tip: Keep food sealed to avoid attracting animals."]
    ],
    [
        r"(.*)best place to camp(.*)",
        ["That depends on where you are — national parks are always a great choice!", "Try camping near lakes or in forest reserves."]
    ],
    [
        r"(.*)need for camping(.*)",
        ["You’ll need a tent, sleeping bag, food, water, and basic tools.", "Don’t forget a lighter, map, and first-aid kit!"]
    ],
    [
        r"(.*)cook while camping(.*)",
        ["You can cook over a fire, use a portable stove, or make no-cook meals.", "Campfire cooking is fun — try foil-wrapped meals!"]
    ],
    [
        r"how to start a campfire(.*)",
        ["Gather dry wood, stack it properly, and light with a match or lighter.", "Use kindling and a fire starter to make it easier."]
    ],
    [
        r"(.*)safe to camp alone(.*)",
        ["It can be safe if you're experienced, but always inform someone.", "Solo camping is peaceful, but take extra precautions."]
    ],
    [
        r"(.*)best time to go camping(.*)",
        ["Spring and fall are ideal — not too hot, not too cold!", "Avoid the rainy season if possible."]
    ],
    [
        r"(.*)afraid of animals while camping(.*)",
        ["Stay calm, store food properly, and avoid strong scents.", "Making noise helps keep wild animals away."]
    ],
    [
        r"(.*)camping with kids(.*)",
        ["Keep them entertained with nature games and keep safety a priority.", "Camping with kids is fun — bring snacks and activities."]
    ],
    [
        r"(.*)camping food ideas(.*)",
        ["Try hot dogs, s'mores, trail mix, or canned beans!", "Wrap veggies and meat in foil and cook over the fire."]
    ],
    [
        r"(.*)tent vs RV(.*)",
        ["Tents are more immersive, RVs are more comfortable.", "Tents give the real camping feel, but RVs are great for families."]
    ],
    [
        r"(.*)what if it rains while camping(.*)",
        ["Make sure your tent is waterproof and bring a tarp.", "Stay dry and cozy inside — rain can be relaxing!"]
    ],
    [
        r"(.*)bear(.*)camping(.*)",
        ["Use bear-proof containers and don’t leave food out.", "Hang food from a tree if bears are around."]
    ],
    [
        r"(.*)sleep comfortably(.*)camping(.*)",
        ["Use a good sleeping pad, warm bag, and stay dry.", "Try earplugs and an eye mask for better sleep."]
    ],
    [
        r"(.*)bathroom(.*)camping(.*)",
        ["Use campsite restrooms or dig a cat hole if in the wild.", "Bring biodegradable wipes and toilet paper."]
    ],
    [
        r"(.*)camping checklist(.*)",
        ["Tent, sleeping bag, flashlight, food, water, first-aid kit, and clothing.", "Don’t forget bug spray and a map!"]
    ],
    [
        r"(.*)stay warm while camping(.*)",
        ["Layer your clothing and use a warm sleeping bag.", "Keep dry, wear socks, and drink something warm."]
    ],
    [
        r"(.*)activities while camping(.*)",
        ["Hiking, fishing, stargazing, or telling stories by the fire!", "Try photography, journaling, or nature scavenger hunts."]
    ],
    [
        r"(.*)campfire stories(.*)",
        ["Classic ghost stories or funny personal experiences work best!", "Tell a spooky story about the woods — safely of course."]
    ],
    [
        r"(.*)pack for a weekend camping trip(.*)",
        ["Tent, sleeping bag, food, clothes, toiletries, and gear.", "Travel light but don’t forget essentials like a first-aid kit."]
    ],

    [
        r"quit",
        ["Bye for now. See you soon :)", "It was nice talking to you. See you soon :)"]
    ],
    [
        r"(.*)",
        ['Our customer service will reach you.']
    ],
]


# Initialize the Chat object
chatbot = Chat(pairs, reflections)

# Set up the Streamlit UI
st.set_page_config(page_title="Camping Chatbot", page_icon="⛺")

st.title("⛺ Camping Chatbot")
st.markdown("Hello! I'm a chatbot trained to answer questions about camping and general topics. Type `quit` to end the chat.")

# Session state to keep track of chat history
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

# Text input from the user
user_input = st.text_input("You:", key="input")

# Process user input
if user_input:
    if user_input.lower() == "quit":
        st.session_state.chat_history.append(("You", user_input))
        st.session_state.chat_history.append(("Bot", "Bye for now. See you soon :)"))
    else:
        response = chatbot.respond(user_input)
        st.session_state.chat_history.append(("You", user_input))
        st.session_state.chat_history.append(("Bot", response))

# Display the conversation
for speaker, text in st.session_state.chat_history:
    if speaker == "You":
        st.markdown(f"**You:** {text}")
    else:
        st.markdown(f"**Bot:** {text}")
