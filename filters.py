import streamlit as st

def render_filters(df):
    st.sidebar.header("🎯 Dashboard Filter Panel")
    
    # 1. Multi-Select Filter for Country Code (Default: All)
    if 'Country_Code' in df.columns:
        countries = sorted(df['Country_Code'].dropna().unique().tolist())
        selected_countries = st.sidebar.multiselect(
            "Filter by Country Code",
            options=countries,
            default=countries
        )
        df = df[df['Country_Code'].isin(selected_countries)]
        
    # 2. Slider Filter for Displaced Persons
    if 'Displaced_Persons' in df.columns:
        min_val = int(df['Displaced_Persons'].min())
        max_val = int(df['Displaced_Persons'].max())
        if min_val < max_val:
            selected_range = st.sidebar.slider(
                "Filter by Displaced Persons Count",
                min_value=min_val,
                max_value=max_val,
                value=(min_val, max_val)
            )
            df = df[df['Displaced_Persons'].between(selected_range[0], selected_range[1])]
            
    # 3. Category Filter for Flood Severity Level
    if 'Flood_Severity' in df.columns:
        severities = ['All'] + sorted(df['Flood_Severity'].dropna().unique().tolist())
        selected_severity = st.sidebar.selectbox("Filter by Flood Severity", severities)
        if selected_severity != 'All':
            df = df[df['Flood_Severity'] == selected_severity]
            
    return df