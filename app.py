import streamlit as st
from datetime import date

# =========================================================
# PAGE CONFIG
# =========================================================

st.set_page_config(
    page_title="CrowdWise",
    page_icon="🌴",
    layout="wide",
    initial_sidebar_state="expanded"
)

# =========================================================
# GROUP DATA
# =========================================================

GROUP_DATA = {
    "Friends": {
        "icon": "👥",
        "title": "Create Unforgettable Memories",
        "description": "Discover exciting places with your friends.",
        "tagline": "Good vibes. Great friends. Better adventures.",
        "image": "https://images.unsplash.com/photo-1529156069898-49953e39b3ac?w=1600"
    },

    "Family": {
        "icon": "👨‍👩‍👧‍👦",
        "title": "Make Every Family Moment Special",
        "description": "Find comfortable and family-friendly destinations.",
        "tagline": "More smiles. Less stress. Happy memories.",
        "image": "https://images.unsplash.com/photo-1511895426328-dc8714191300?w=1600"
    },

    "Couples": {
        "icon": "❤️",
        "title": "Plan Beautiful Moments Together",
        "description": "Discover peaceful and romantic places.",
        "tagline": "Better places. Deeper connections.",
        "image": "https://images.unsplash.com/photo-1516589178581-6cd7833ae3b2?w=1600"
    }
}

# =========================================================
# PLACE DATA
# =========================================================

PLACES = {

    "Chennai": {

        "Marina Beach": {
            "type": "Beach",
            "icon": "🌊",
            "description": "Waves, sand and endless skies",
            "crowd": 78,
            "count": 4200,
            "best_time": "6:00 AM - 8:00 AM"
        },

        "Besant Nagar Beach": {
            "type": "Beach",
            "icon": "🌊",
            "description": "Relax by the sea and enjoy the breeze",
            "crowd": 58,
            "count": 2300,
            "best_time": "6:00 AM - 8:00 AM"
        },

        "Express Avenue Mall": {
            "type": "Mall",
            "icon": "🛍️",
            "description": "Shopping, food and entertainment",
            "crowd": 62,
            "count": 1800,
            "best_time": "10:00 AM - 12:00 PM"
        },

        "Phoenix Marketcity": {
            "type": "Mall",
            "icon": "🏬",
            "description": "Shopping, movies and great food",
            "crowd": 72,
            "count": 2500,
            "best_time": "10:00 AM - 12:00 PM"
        },

        "Guindy National Park": {
            "type": "Nature",
            "icon": "🌳",
            "description": "Nature, fresh air and peaceful surroundings",
            "crowd": 35,
            "count": 650,
            "best_time": "7:00 AM - 9:00 AM"
        },

        "Kapaleeshwarar Temple": {
            "type": "Temple",
            "icon": "🛕",
            "description": "Culture, heritage and peaceful surroundings",
            "crowd": 48,
            "count": 1200,
            "best_time": "6:00 AM - 8:00 AM"
        },

        "Government Museum": {
            "type": "Museum",
            "icon": "🏛️",
            "description": "History, culture and fascinating exhibits",
            "crowd": 30,
            "count": 500,
            "best_time": "10:00 AM - 12:00 PM"
        }
    },

    "Coimbatore": {

        "Brookefields Mall": {
            "type": "Mall",
            "icon": "🛍️",
            "description": "Shopping, food and entertainment",
            "crowd": 65,
            "count": 1600,
            "best_time": "10:00 AM - 12:00 PM"
        },

        "VOC Park": {
            "type": "Nature",
            "icon": "🌳",
            "description": "Nature, fresh air and family time",
            "crowd": 38,
            "count": 700,
            "best_time": "7:00 AM - 9:00 AM"
        },

        "Marudamalai Temple": {
            "type": "Temple",
            "icon": "🛕",
            "description": "Spiritual vibes and scenic views",
            "crowd": 72,
            "count": 2500,
            "best_time": "6:00 AM - 8:00 AM"
        },

        "Siruvani Hills": {
            "type": "Hills",
            "icon": "⛰️",
            "description": "Cool weather and beautiful views",
            "crowd": 42,
            "count": 900,
            "best_time": "6:00 AM - 9:00 AM"
        }
    }
}

# =========================================================
# PLACE VISUALS
# =========================================================

PLACE_VISUALS = {
    "Beach": {
        "visual": "🌊 🌊 🌊",
        "icon": "🌊",
        "text": "Waves • Sand • Sea breeze"
    },

    "Mall": {
        "visual": "🏬 🛍️",
        "icon": "🛍️",
        "text": "Shopping • Food • Entertainment"
    },

    "Nature": {
        "visual": "🌳 🌲 🌳",
        "icon": "🌳",
        "text": "Fresh air • Greenery • Peace"
    },

    "Temple": {
        "visual": "🛕 ✨",
        "icon": "🛕",
        "text": "Culture • Heritage • Peace"
    },

    "Hills": {
        "visual": "🏔️ ⛰️ 🏔️",
        "icon": "⛰️",
        "text": "Views • Nature • Adventure"
    },

    "Museum": {
        "visual": "🏛️ 🏛️",
        "icon": "🏛️",
        "text": "History • Culture • Learning"
    }
}

# =========================================================
# CSS
# =========================================================

st.markdown("""
<style>

.stApp {
    background: #F4F7FB;
}

/* SIDEBAR */

[data-testid="stSidebar"] {
    background: linear-gradient(180deg, #071B36 0%, #102F54 100%);
}

[data-testid="stSidebar"] label {
    color: white !important;
}

[data-testid="stSidebar"] p {
    color: white !important;
}

[data-testid="stSidebar"] [data-baseweb="select"] {
    background: white !important;
    border-radius: 12px !important;
}

[data-testid="stSidebar"] [data-baseweb="select"] div {
    color: #17365D !important;
}

[data-testid="stSidebar"] input {
    background: white !important;
    color: #17365D !important;
}

/* BRAND */

.brand {
    font-size: 28px;
    font-weight: 800;
}

.brand-green {
    color: #2DD4BF;
}

.brand-subtitle {
    color: #B9C9DC !important;
    font-size: 12px;
    margin-bottom: 25px;
}

/* PLACE PREVIEW */

.place-preview {
    padding: 15px;
    margin-top: 10px;
    border-radius: 16px;
    text-align: center;
    background: rgba(255,255,255,0.10);
    border: 1px solid rgba(255,255,255,0.25);
}

.place-visual {
    font-size: 28px;
}

.place-name {
    color: white;
    font-size: 16px;
    font-weight: 700;
}

.place-small {
    color: #C5D3E5;
    font-size: 11px;
}

/* SECTIONS */

.section-title {
    color: #17365D;
    font-size: 28px;
    font-weight: 800;
    margin-top: 20px;
}

/* CARDS */

.info-card {
    background: white;
    border-radius: 18px;
    padding: 20px;
    box-shadow: 0 5px 20px rgba(0,0,0,0.06);
}

.info-label {
    color: #64748B;
    font-size: 13px;
}

.info-value {
    color: #17365D;
    font-size: 22px;
    font-weight: 700;
    margin-top: 5px;
}

.alt-card {
    background: white;
    border-radius: 16px;
    padding: 18px;
    margin-bottom: 12px;
    border: 1px solid #E2E8F0;
}

.alt-title {
    color: #17365D;
    font-size: 18px;
    font-weight: 700;
}

.alt-text {
    color: #64748B;
    font-size: 13px;
}

.footer {
    text-align: center;
    color: #64748B;
    padding: 30px;
}

</style>
""", unsafe_allow_html=True)


# =========================================================
# SIDEBAR
# =========================================================

with st.sidebar:

    st.markdown(
        '<div class="brand">🌴 Crowd<span class="brand-green">Wise</span></div>',
        unsafe_allow_html=True
    )

    st.markdown(
        '<div class="brand-subtitle">Smart Crowd Prediction & Place Recommendation</div>',
        unsafe_allow_html=True
    )

    st.markdown("## 🧭 Plan Your Outing")

    city = st.selectbox(
        "📍 Select City",
        list(PLACES.keys())
    )

    outing_type = st.radio(
        "👥 Who are you going with?",
        ["Friends", "Family", "Couples"]
    )

    visit_date = st.date_input(
        "🗓️ Select Date",
        min_value=date.today()
    )

    visit_time = st.selectbox(
        "⏰ Preferred Time",
        [
            "Morning",
            "Afternoon",
            "Evening",
            "Night"
        ]
    )

    selected_place = st.selectbox(
        "📍 Choose a Place",
        list(PLACES[city].keys())
    )

    # =====================================================
    # PLACE PREVIEW
    # =====================================================

    place_data = PLACES[city][selected_place]
    place_type = place_data["type"]
    visual = PLACE_VISUALS[place_type]

    preview_html = f"""
    <div class="place-preview">
        <div class="place-visual">{visual["visual"]}</div>
        <div class="place-name">
            {visual["icon"]} {selected_place}
        </div>
        <div class="place-small">
            {visual["text"]}
        </div>
    </div>
    """

    # Use st.html instead of st.markdown
    st.html(preview_html)

    st.write("")

    predict_button = st.button(
        "🔍 Predict Crowd",
        use_container_width=True
    )


# =========================================================
# HERO
# =========================================================

group = GROUP_DATA[outing_type]

hero_html = f"""
<div style="
    height:330px;
    border-radius:26px;
    overflow:hidden;
    background-image:url('{group["image"]}');
    background-size:cover;
    background-position:center;
    margin-bottom:25px;
">
    <div style="
        height:100%;
        padding:45px;
        box-sizing:border-box;
        display:flex;
        flex-direction:column;
        justify-content:center;
        background:linear-gradient(
            90deg,
            rgba(4,18,40,0.92),
            rgba(4,18,40,0.55),
            rgba(4,18,40,0.08)
        );
    ">
        <div style="
            color:white;
            background:rgba(255,255,255,0.18);
            padding:8px 15px;
            border-radius:25px;
            width:max-content;
            font-size:14px;
            margin-bottom:12px;
        ">
            {group["icon"]} {outing_type} Experience
        </div>

        <div style="
            color:white;
            font-size:44px;
            font-weight:800;
            line-height:1.1;
            margin-bottom:10px;
        ">
            {group["title"]}
        </div>

        <div style="
            color:#E4EDF8;
            font-size:18px;
            margin-bottom:8px;
        ">
            {group["description"]}
        </div>

        <div style="
            color:white;
            font-size:15px;
        ">
            ✨ <b>{group["tagline"]}</b>
        </div>
    </div>
</div>
"""

# =========================================================
# IMPORTANT
# =========================================================
# st.html() directly renders HTML.
# It prevents the <div> tags from appearing as text.

st.html(hero_html)


# =========================================================
# PLANNER
# =========================================================

st.markdown(
    '<div class="section-title">✨ Your Personalized Travel Planner</div>',
    unsafe_allow_html=True
)

st.write(
    "Plan your outing based on your group, destination and preferred time."
)


# =========================================================
# INFO CARDS
# =========================================================

col1, col2, col3 = st.columns(3)

with col1:

    st.markdown(
        f"""
        <div class="info-card">
            <div class="info-label">📍 SELECTED CITY</div>
            <div class="info-value">{city}</div>
        </div>
        """,
        unsafe_allow_html=True
    )

with col2:

    st.markdown(
        f"""
        <div class="info-card">
            <div class="info-label">👥 OUTING TYPE</div>
            <div class="info-value">{outing_type}</div>
        </div>
        """,
        unsafe_allow_html=True
    )

with col3:

    st.markdown(
        f"""
        <div class="info-card">
            <div class="info-label">🗓️ VISIT DATE</div>
            <div class="info-value">{visit_date}</div>
        </div>
        """,
        unsafe_allow_html=True
    )


# =========================================================
# CROWD PREDICTION
# =========================================================

if predict_button:

    crowd_score = place_data["crowd"]
    crowd_count = place_data["count"]
    best_time = place_data["best_time"]

    if crowd_score <= 40:

        crowd_level = "Low"
        crowd_icon = "🟢"
        advice = "A relatively peaceful experience may be possible."

    elif crowd_score <= 70:

        crowd_level = "Medium"
        crowd_icon = "🟡"
        advice = "Moderate crowd expected. Plan your visit accordingly."

    else:

        crowd_level = "High"
        crowd_icon = "🔴"
        advice = "Higher crowd expected. Consider an alternative place."

    st.markdown(
        '<div class="section-title">📊 Crowd Prediction</div>',
        unsafe_allow_html=True
    )

    r1, r2, r3 = st.columns(3)

    with r1:
        st.metric(
            "Expected Crowd",
            f"{crowd_count:,} people"
        )

    with r2:
        st.metric(
            "Crowd Level",
            f"{crowd_icon} {crowd_level}"
        )

    with r3:
        st.metric(
            "Crowd Score",
            f"{crowd_score}/100"
        )

    st.progress(crowd_score / 100)

    st.info(
        f"""
        📍 **{selected_place}**

        {advice}

        ⏰ **Suggested time:** {best_time}
        """
    )

    # =====================================================
    # ALTERNATIVES
    # =====================================================

    # =====================================================
    # ALTERNATIVES
    # =====================================================

    st.markdown(
        '<div class="section-title">🌿 Recommended Alternatives</div>',
        unsafe_allow_html=True
    )

    alternatives = []

    for name, data in PLACES[city].items():

        if name != selected_place and data["crowd"] < crowd_score:
            alternatives.append((name, data))

    alternatives.sort(
        key=lambda x: x[1]["crowd"]
    )

    if alternatives:

        for name, data in alternatives[:3]:
            st.markdown(
                f"### {data['icon']} {name}"
            )

            st.write(
                data["description"]
            )

            col_a, col_b, col_c = st.columns(3)

            with col_a:
                st.metric(
                    "Expected Crowd",
                    f"{data['count']:,}"
                )

            with col_b:
                st.metric(
                    "Crowd Score",
                    f"{data['crowd']}/100"
                )

            with col_c:
                st.metric(
                    "Best Time",
                    data["best_time"]
                )

            st.divider()

    else:

        st.warning(
            "No less-crowded alternative is available in this demo."
        )
    # =====================================================
    # BEST TIME
    # =====================================================

    st.markdown(
        '<div class="section-title">⏰ Best Time to Visit</div>',
        unsafe_allow_html=True
    )

    st.success(
        f"The prototype suggests visiting **{selected_place}** "
        f"around **{best_time}**."
    )

else:

    st.info(
        "👈 Select your preferences and click **Predict Crowd** "
        "to see your personalized result."
    )


# =========================================================
# PROTOTYPE NOTICE
# =========================================================

st.divider()

st.warning(
    "Prototype: Crowd values shown here are demonstration data. "
    "A trained ML model will replace these values in the next stage."
)


# =========================================================
# FOOTER
# =========================================================

st.markdown(
    """
    <div class="footer">
        🌴 <b>CrowdWise</b><br>
        Plan Smart • Explore More • Enjoy Better
    </div>
    """,
    unsafe_allow_html=True
)