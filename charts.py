import streamlit as st
import matplotlib.pyplot as plt
import seaborn as sns

def render_visualizations(df):
    if df.empty:
        st.warning("⚠️ No data matches your filter parameters. Try expanding your sidebar selection!")
        return

    st.subheader("📊 Analytical Visualizations")
    
    # Create an organized layout with two columns
    col1, col2 = st.columns(2)
    
    with col1:
        # Chart A: Pie Chart (Proportional Distribution)
        if 'Flood_Severity' in df.columns:
            st.markdown("#### 🍕 Proportional Distribution of Flood Severity")
            fig1, ax1 = plt.subplots(figsize=(6, 4))
            severity_counts = df['Flood_Severity'].value_counts()
            ax1.pie(severity_counts, labels=severity_counts.index, autopct='%1.1f%%', colors=sns.color_palette('pastel'))
            ax1.axis('equal')  
            st.pyplot(fig1)
            plt.close(fig1)
            
        # Chart B: Histogram (Frequency Distribution)
        if 'Displaced_Persons' in df.columns and df['Displaced_Persons'].max() > 0:
            st.markdown("#### 🧮 Frequency Distribution of Displaced Persons")
            fig2, ax2 = plt.subplots(figsize=(6, 4))
            sns.histplot(data=df, x='Displaced_Persons', bins=15, kde=True, color='purple', ax=ax2)
            ax2.set_title("Displaced Persons Spread", fontsize=10, fontweight='bold')
            ax2.set_xlabel("Number of Displaced Persons")
            ax2.set_ylabel("Frequency")
            st.pyplot(fig2)
            plt.close(fig2)

    with col2:
        # Chart C: Bar Chart (Categorical Comparison)
        if 'Country_Code' in df.columns and 'Displaced_Persons' in df.columns:
            st.markdown("#### 🗺️ Total Displaced Population by Country")
            fig3, ax3 = plt.subplots(figsize=(6, 4))
            country_summary = df.groupby('Country_Code')['Displaced_Persons'].sum().reset_index()
            country_summary = country_summary.sort_values(by='Displaced_Persons', ascending=False).head(10)
            
            ax3.bar(country_summary['Country_Code'], country_summary['Displaced_Persons'], color='#3498db', edgecolor='black')
            ax3.set_title("Top Impacted Countries", fontsize=10, fontweight='bold')
            ax3.set_xlabel("Country Identifier")
            ax3.set_ylabel("Total Displaced")
            st.pyplot(fig3)
            plt.close(fig3)
            
        # Chart D: Scatter Plot (Numerical Relationships)
        if 'Affected_Area_Sqm' in df.columns and 'Displaced_Persons' in df.columns:
            st.markdown("#### 📉 Area Size vs. Displaced Persons")
            fig4, ax4 = plt.subplots(figsize=(6, 4))
            sns.scatterplot(data=df, x='Affected_Area_Sqm', y='Displaced_Persons', hue='Flood_Severity', palette='viridis', ax=ax4)
            ax4.set_title("Impact Scope Correlation", fontsize=10, fontweight='bold')
            ax4.set_xlabel("Affected Area (Sqm)")
            ax4.set_ylabel("Displaced Persons")
            st.pyplot(fig4)
            plt.close(fig4)