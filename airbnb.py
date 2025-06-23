import pandas as pd
import streamlit as st
from streamlit_option_menu import option_menu
import plotly.express as px

#streamlit part
st.set_page_config(layout = "wide")
st.title("Airbnb Data Analysis")
st.write("")

df = pd.read_csv(r"C:\datascience\guvi_projects\guvi-airbnb-project\airbnb_data_cleaned.csv")

with st.sidebar:
    select = option_menu("Menu",["Home","Data Exploration"])

if select == "Home":
    image_url = "https://images.unsplash.com/photo-1560448204-e02f11c3d0e2"
    st.markdown(
        f'''
        <div style="text-align:center; margin: 20px 0;">
            <img src="{image_url}" alt="Airbnb Interior" style="width:50%; max-width:800px; border-radius:10px;">
        </div>
        ''',
        unsafe_allow_html=True
    )
    st.header("About Airbnb")
    st.write("")
    st.write('''***Airbnb is an online marketplace that connects people looking to 
                rent out their homes with those looking for accommodations. Founded in 2008, 
                it has grown to become one of the largest hospitality services in the world, 
                offering a wide range of lodging options from single rooms to entire homes and 
                unique stays like treehouses and castles.***''')
    st.write("")

    st.header("About the Project")
    st.write("This project is a comprehensive analysis of Airbnb data, focusing on various aspects such as price differences, availability, location-based insights, and geospatial analysis. The goal is to provide valuable insights into the Airbnb market and help users make informed decisions.")
    
    st.write("### Key Features:")
    st.write("- **Price Analysis**: Understand how property types and room types affect pricing.")
    st.write("- **Availability Analysis**: Explore how availability varies across different time frames.")
    st.write("- **Location-Based Analysis**: Visualize properties on a map based on their location and characteristics.")
    st.write("- **Geospatial Analysis**: Analyze properties geographically to identify trends and patterns.")
    st.write("- **Top Charts**: Highlight top-rated and most expensive properties for quick insights.")
    
    st.write("### Technologies Used:")
    st.write("- Python")
    st.write("- Pandas")
    st.write("- Streamlit")
    st.write("- Plotly")

if select == "Data Exploration":
    tab1, tab2, tab3, tab4, tab5 = st.tabs(["Price Analysis", "Availability Analysis", "Location Based",
                                            "Geospatial Analysis",
                                            "Top Charts"])
    
    with tab1:
        st.title("PRICE DIFFERENCE")
        col1, col2 = st.columns(2)

        with col1:
            country = st.selectbox("Select Country", df["country"].unique())
            df1 = df[df["country"] == country]
            df1.reset_index(drop=True, inplace=True)

            room_type = st.selectbox("Select Room Type", df1["room_type"].unique())
            df2 = df1[df1["room_type"] == room_type]
            df2.reset_index(drop=True, inplace=True)

            df_bar = df2.groupby("property_type").agg({"price": "sum", "number_of_reviews": "sum", "review_scores": "mean"})
            df_bar.reset_index(inplace=True)

            fig_bar = px.bar(df_bar, x="property_type", y="price", title="Price for property types", hover_data=["number_of_reviews", "review_scores"], width=600, height=500, color_discrete_sequence=px.colors.sequential.Rainbow)
            st.plotly_chart(fig_bar)
        
        with col2:
            st.write("")
            st.write("")
            st.write("")
            st.write("")
            st.write("")

            property_ty = st.selectbox("Select Property Type", df2["property_type"].unique())
            df3 = df2[df1["property_type"] == property_ty]
            df3.reset_index(drop=True, inplace=True)

            df_pie = df3.groupby("host_response_time")[["price","bedrooms"]].sum()
            df_pie.reset_index(inplace=True)

            fig_pie = px.pie(df_pie, names="host_response_time", values = "price",
                            hover_data=["bedrooms"],color_discrete_sequence=px.colors.sequential.Burg,
                            title="Price for host response time", width=600, height=500)
            st.plotly_chart(fig_pie)
   
    with tab2:
        st.title("AVAILABILITY ANALYSIS ")
        col1, col2 = st.columns(2)

        with col1:
            country = st.selectbox("Select Country_a", df["country"].unique())
            df1 = df[df["country"] == country]
            df1.reset_index(drop=True, inplace=True)

            property_ty = st.selectbox("Select Property Type_a", df1["property_type"].unique())
            df2 = df1[df1["property_type"] == property_ty]
            df2.reset_index(drop=True, inplace=True)

            df_a_sunb_30 = px.sunburst(df2, path=["room_type", "bed_type","is_location_exact"], 
                                       values="availability_30",width=600, height=500,
                                       title="Availability in 30 days for room type, bed type and location exact",
                                       color_discrete_sequence=px.colors.sequential.Plasma)
            st.plotly_chart(df_a_sunb_30)
 
        
        with col2:
            st.write("")
            st.write("")
            st.write("")
            st.write("")
            st.write("")
            st.write("")
            st.write("")
            st.write("")
            st.write("")
            st.write("")
            st.write("")

            df_a_sunb_60 = px.sunburst(df2, path=["room_type", "bed_type","is_location_exact"], 
                                       values="availability_60",width=600, height=500,
                                       title="Availability in 60 days for room type, bed type and location exact",
                                       color_discrete_sequence=px.colors.sequential.Darkmint_r)
            st.plotly_chart(df_a_sunb_60)

        col1, col2 = st.columns(2)

        with col1:
            df_a_sunb_90 = px.sunburst(df2, path=["room_type", "bed_type","is_location_exact"], 
                                       values="availability_90",width=600, height=500,
                                       title="Availability in 90 days for room type, bed type and location exact",
                                       color_discrete_sequence=px.colors.sequential.GnBu_r)
            st.plotly_chart(df_a_sunb_90)

        with col2:
            df_a_sunb_365 = px.sunburst(df2, path=["room_type", "bed_type","is_location_exact"], 
                                        values="availability_365",width=600, height=500,
                                        title="Availability in 365 days for room type, bed type and location exact",
                                        color_discrete_sequence=px.colors.sequential.turbid_r)
            st.plotly_chart(df_a_sunb_365)
        
        room_ty_a = st.selectbox("Select Room Type_a", df2["room_type"].unique())
        
        df3_a = df2[df2["room_type"] == room_ty_a]
        df3_a.reset_index(drop=True, inplace=True)

        df3_a.groupby("host_response_time")[["availability_30","availability_60",
                                             "availability_90","availability_365"]].sum()
        df3_a.reset_index(inplace=True)

        fig_df_mul_bar_a = px.bar(df3_a, x="host_response_time",
                                  y=["availability_30", "availability_60", "availability_90", "availability_365"],
                                  title="Availability based on host response time",
                                  barmode="group",
                                  color_discrete_sequence=px.colors.qualitative.Pastel,
                                  width=600, height=500)
        st.plotly_chart(fig_df_mul_bar_a)
    
    with tab3:
        st.title("LOCATION BASED ANALYSIS")
        col1, col2 = st.columns(2)

        with col1:
            country = st.selectbox("Select Country_b", df["country"].unique())
            df1 = df[df["country"] == country]
            df1.reset_index(drop=True, inplace=True)

            property_ty = st.selectbox("Select Property Type_b", df1["property_type"].unique())
            df2 = df1[df1["property_type"] == property_ty]
            df2.reset_index(drop=True, inplace=True)

            fig_map = px.scatter_mapbox(df2, lat="latitude", lon="longitude", color="room_type",
                                        size="price", hover_name="name", zoom=10,
                                        title="Location based analysis for room type and price",
                                        color_discrete_sequence=px.colors.qualitative.Plotly)
            fig_map.update_layout(mapbox_style="open-street-map")
            st.plotly_chart(fig_map)

        with col2:
            st.write("")
            st.write("")
            st.write("")
            st.write("")
            st.write("")
            st.write("")
            st.write("")
            st.write("")
            st.write("")
            st.write("")

            fig_map2 = px.scatter_mapbox(df2, lat="latitude", lon="longitude", color="bed_type",
                                         size="price", hover_name="name", zoom=10,
                                         title="Location based analysis for bed type and price",
                                         color_discrete_sequence=px.colors.qualitative.Plotly)
            fig_map2.update_layout(mapbox_style="open-street-map")
            st.plotly_chart(fig_map2)
        
    with tab4:
        st.title("GEOSPATIAL ANALYSIS")
        col1, col2 = st.columns(2)

        with col1:
            country = st.selectbox("Select Country_c", df["country"].unique())
            df1 = df[df["country"] == country]
            df1.reset_index(drop=True, inplace=True)

            property_ty = st.selectbox("Select Property Type_c", df1["property_type"].unique())
            df2 = df1[df1["property_type"] == property_ty]
            df2.reset_index(drop=True, inplace=True)

            fig_geo = px.scatter_geo(df2, lat="latitude", lon="longitude", color="room_type",
                                     size="price", hover_name="name", title="Geospatial analysis for room type and price",
                                     color_discrete_sequence=px.colors.qualitative.Plotly)
            st.plotly_chart(fig_geo)

        with col2:
            st.write("")
            st.write("")
            st.write("")
            st.write("")
            st.write("")
            st.write("")
            st.write("")
            st.write("")
            st.write("")
            st.write("")
            st.write("")

            fig_geo2 = px.scatter_geo(df2, lat="latitude", lon="longitude", color="bed_type",
                                      size="price", hover_name="name", title="Geospatial analysis for bed type and price",
                                      color_discrete_sequence=px.colors.qualitative.Plotly)
            st.plotly_chart(fig_geo2)
    
    with tab5:
        st.title("TOP CHARTS")
        col1, col2 = st.columns(2)

        with col1:
            country = st.selectbox("Select Country_d", df["country"].unique())
            df1 = df[df["country"] == country]
            df1.reset_index(drop=True, inplace=True)

            property_ty = st.selectbox("Select Property Type_d", df1["property_type"].unique())
            df2 = df1[df1["property_type"] == property_ty]
            df2.reset_index(drop=True, inplace=True)

            top_rated = df2.nlargest(10, 'review_scores')
            fig_top_rated = px.bar(top_rated, x='name', y='review_scores',
                                   title='Top 10 Rated Properties', color='review_scores',
                                   color_continuous_scale=px.colors.sequential.Viridis,
                                   height=600)
            st.plotly_chart(fig_top_rated)

        with col2:
            st.write("")
            st.write("")
            st.write("")
            st.write("")
            st.write("")
            st.write("")
            st.write("")
            st.write("")
            st.write("")
            st.write("")

    
            top_price = df2.nlargest(10, 'price')
            fig_top_price = px.bar(top_price, x='name', y='price', 
                                   title='Top 10 Most Expensive Properties', color='price',
                                   color_continuous_scale=px.colors.sequential.Inferno, height=600)
            st.plotly_chart(fig_top_price)
