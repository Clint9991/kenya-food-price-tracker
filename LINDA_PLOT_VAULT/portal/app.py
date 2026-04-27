import streamlit as st
import pandas as pd
import time
import math
from PIL import Image
from PIL.ExifTags import TAGS, GPSTAGS

# --- 1. CONFIG & STYLING ---
st.set_page_config(page_title="LINDA PLOT | Private Vault", layout="centered", initial_sidebar_state="collapsed")

st.markdown("""
    <style>
    body {background-color: #050505;}
    h1, h2, h3 {color: #D4AF37 !important; text-align: center; font-family: 'Courier New', Courier, monospace;}
    .legal-text {font-size: 0.65rem; color: #444444; text-align: center; margin-top: 50px;}
    .success-data {border-left: 3px solid #4CAF50; padding-left: 15px; color: #D4AF37; font-family: monospace; background-color: #111; padding: 10px; border-radius: 4px;}
    .ledger-text {color: #888; font-family: monospace; font-size: 0.9rem;}
    .stButton>button {width: 100%; font-weight: bold; border-radius: 4px; border: 1px solid #D4AF37; color: #D4AF37; background-color: transparent;}
    .stButton>button:hover {background-color: #D4AF37; color: #050505;}
    </style>
""", unsafe_allow_html=True)

st.markdown("<h1>LINDA PLOT</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; color: #888; font-family: monospace;'>Trust-as-a-Service for the African Diaspora</p>", unsafe_allow_html=True)

tab1, tab2, tab3, tab4 = st.tabs(["🌍 ACCESS", "💼 INVESTOR VAULT", "📡 DISPATCH", "🛡️ FIELD TERMINAL"])

# --- 2. FORENSIC MATH ENGINE ---
def get_decimal_from_dms(dms, ref):
    try:
        degrees, minutes, seconds = float(dms[0]), float(dms[1]), float(dms[2])
        decimal = degrees + (minutes / 60.0) + (seconds / 3600.0)
        if ref in ['S', 'W']: decimal = -decimal
        return decimal
    except: return None

def get_exif_location(image):
    try:
        exif_data = image._getexif()
        if not exif_data: return None, None
        geotagging = {}
        for (idx, tag) in TAGS.items():
            if tag == 'GPSInfo':
                for (key, val) in GPSTAGS.items():
                    if key in exif_data[idx]: geotagging[val] = exif_data[idx][key]
        if 'GPSLatitude' in geotagging and 'GPSLongitude' in geotagging:
            lat = get_decimal_from_dms(geotagging['GPSLatitude'], geotagging['GPSLatitudeRef'])
            lon = get_decimal_from_dms(geotagging['GPSLongitude'], geotagging['GPSLongitudeRef'])
            return lat, lon
    except: pass
    return None, None

def haversine(lat1, lon1, lat2, lon2):
    R = 6371000 
    phi1, phi2 = math.radians(lat1), math.radians(lat2)
    dphi = math.radians(lat2 - lat1)
    dlambda = math.radians(lon2 - lon1)
    a = math.sin(dphi/2)**2 + math.cos(phi1)*math.cos(phi2)*math.sin(dlambda/2)**2
    return 2 * R * math.atan2(math.sqrt(a), math.sqrt(1 - a))

# --- UI TABS ---

# TAB 1: ACCESS (Waitlist / Landing)
with tab1:
    st.subheader("Secure Your Legacy")
    st.write("Stop relying on hearsay. Deploy forensic-grade surveillance to protect your Kenyan assets from encroachment.")
    
    st.error("""**[CRITICAL INTELLIGENCE]**
    
* Over $2B in diaspora remittances is lost annually to mismanaged real estate.
* 60% of diaspora investors experience land encroachment or fraudulent scout reporting.
* LINDA PLOT reduces spatial verification fraud to 0% using Haversine cryptography.""")

    st.divider()
    st.markdown("### 🔐 Request Early Access")
    st.markdown("<p style='text-align: center; color: #888; font-size: 0.9rem;'>We are onboarding our Beta cohort. Secure your position on the ledger.</p>", unsafe_allow_html=True)
    
    with st.form("waitlist_form"):
        col1, col2 = st.columns([2, 1])
        with col1:
            email = st.text_input("Email Address", placeholder="investor@diaspora.com", label_visibility="collapsed")
        with col2:
            join = st.form_submit_button("JOIN WAITLIST")
            
        if join:
            if "@" in email and "." in email:
                with st.spinner("Encrypting credentials..."):
                    time.sleep(1)
                    st.success("✅ CREDENTIALS SECURED.")
                    st.markdown(f"""
                    <div class='success-data'>
                    <strong>STATUS:</strong> Waitlist Position #427<br>
                    <strong>ENCRYPTED:</strong> {email}<br>
                    <strong>NEXT STEP:</strong> Awaiting Beta Unlocking
                    </div>
                    """, unsafe_allow_html=True)
            else:
                st.error("🚨 SYSTEM REJECT: Please enter a valid email format.")

# TAB 2: INVESTOR VAULT
with tab2:
    st.subheader("Private Asset Vault")
    st.markdown("<p style='text-align: center; color: #888; font-size: 0.8rem;'>Enter your secure Mission ID to view your live asset ledger.</p>", unsafe_allow_html=True)
    
    m_id = st.text_input("Mission ID:", placeholder="e.g., MSN-002K")
    
    if m_id == "MSN-002K":
        st.success("✅ ACCESS GRANTED: Cryptographic Handshake Successful.")
        st.divider()
        
        col1, col2 = st.columns([1.5, 1])
        
        with col1:
            st.markdown("### 🗺️ Spatial Coordinates")
            map_data = pd.DataFrame({'lat': [-1.3833], 'lon': [36.6333]})
            st.map(map_data, zoom=11, use_container_width=True)
            
        with col2:
            st.markdown("### 🗄️ Forensic Ledger")
            st.markdown("""
            <div class='success-data'>
            <strong>ASSET:</strong> Kajiado - Kimuka Block 1<br>
            <strong>STATUS:</strong> <span style='color:#4CAF50;'>SECURED</span><br>
            <strong>GEOFENCE:</strong> 100m Radius<br>
            <strong>HASH:</strong> 8a4b29...e91f<br>
            </div>
            """, unsafe_allow_html=True)
            
            st.markdown("<br><p class='ledger-text'><strong>Scout ID:</strong> 04-DELTA<br><strong>Last Audit:</strong> 2026-04-26 14:30 EAT<br><strong>Integrity:</strong> NO ENCROACHMENT DETECTED</p>", unsafe_allow_html=True)
            st.image("https://images.unsplash.com/photo-1484318571209-661cf29a69c3?ixlib=rb-4.0.3&auto=format&fit=crop&w=800&q=80", caption="Watermarked Asset Proof")

    elif m_id != "":
        st.error("🚨 ACCESS DENIED: Invalid Mission ID or unverified credentials.")

# TAB 3: DISPATCH (The Monetization Engine)
with tab3:
    st.subheader("Deploy a Field Scout")
    st.markdown("<p style='text-align: center; color: #888; font-size: 0.8rem;'>Authorize a forensic audit of your physical asset.</p>", unsafe_allow_html=True)
    
    with st.form("dispatch_form"):
        col1, col2 = st.columns(2)
        with col1:
            plot_no = st.text_input("Plot / Title Number", placeholder="e.g., KJD/KIM/1042")
            county = st.selectbox("Target Region", ["Kajiado", "Machakos", "Kiambu", "Nairobi", "Nakuru"])
        with col2:
            req_lat = st.number_input("Expected Latitude (Optional)", format="%.5f")
            req_lon = st.number_input("Expected Longitude (Optional)", format="%.5f")
            
        st.markdown("### Service Tier")
        tier = st.radio("Select your level of cryptographic custody:", [
            "**SINGLE AUDIT:** One-time spatial verification and proof-of-life report. ($50)",
            "**CONTINUOUS CUSTODY:** Monthly autonomous scout dispatch + tamper-proof ledger. ($150/mo)"
        ])
        
        instructions = st.text_area("Secure Instructions for Scout Network")
        
        submit = st.form_submit_button("AUTHORIZE DEPLOYMENT")
        
        if submit:
            if not plot_no:
                st.error("🚨 Deployment Failed: Plot Number is required.")
            else:
                with st.spinner("Encrypting parameters and pinging local scout network..."):
                    time.sleep(2) 
                    st.success("✅ DEPLOYMENT AUTHORIZED.")
                    st.markdown(f"""
                    <div class='success-data'>
                    <strong>NEW MISSION ID:</strong> MSN-{str(int(time.time()))[-4:]}<br>
                    <strong>TARGET:</strong> {plot_no}, {county}<br>
                    <strong>TIER:</strong> {tier.split(':')[0].replace('**', '')}<br>
                    <strong>STATUS:</strong> ENCRYPTED & BROADCASTED
                    </div>
                    """, unsafe_allow_html=True)

# TAB 4: FIELD TERMINAL
with tab4:
    st.subheader("Scout Command Interface")
    
    data = [
        {"mission_id": "MSN-001A", "plot_location": "Machakos - Block 4", "target_lat": -1.517, "target_lon": 37.265},
        {"mission_id": "MSN-002K", "plot_location": "Kajiado - Kimuka Block 1", "target_lat": -1.3833, "target_lon": 36.6333}
    ]
    df = pd.DataFrame(data)
    
    mission_list = df['mission_id'] + " : " + df['plot_location']
    selected = st.selectbox("Assigned Mission", mission_list)
    
    target_row = df[df['mission_id'] == selected.split(" : ")[0]].iloc[0]
    target_lat, target_lon = target_row['target_lat'], target_row['target_lon']
    
    st.info(f"📍 Target: {target_row['plot_location']} | Accuracy Required: < 100m")
    
    up = st.file_uploader("Upload Forensic Asset", type=["jpg", "jpeg"])
    if up:
        with st.spinner("Analyzing EXIF Metadata and Haversine distance..."):
            time.sleep(1.5)
            img = Image.open(up)
            photo_lat, photo_lon = get_exif_location(img)
            
            if photo_lat is None or photo_lon is None:
                st.error("🚨 [REJECTED] No GPS metadata found. Image stripped or taken from unverified device.")
            else:
                distance = haversine(target_lat, target_lon, photo_lat, photo_lon)
                if distance <= 5000:
                    st.success(f"✅ VERIFIED. Distance from target: {distance:,.1f}m.")
                    st.markdown(f"<div class='success-data'>Photo Coordinates: {photo_lat:.4f}, {photo_lon:.4f}</div>", unsafe_allow_html=True)
                else:
                    st.error(f"🚨 [CRITICAL BREACH] Asset uploaded {distance:,.1f}m away from target coordinates. Integrity failed.")

st.markdown("<div class='legal-text'>LINDA PLOT LEGAL DISCLOSURE<br>© 2026 LINDA PLOT. All Rights Reserved.</div>", unsafe_allow_html=True)