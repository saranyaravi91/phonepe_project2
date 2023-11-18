
import pandas as pd
import streamlit as st
import plotly.express as px
import os
import json
from streamlit_option_menu import option_menu
from PIL import Image
import pymysql


mydb = pymysql.connect(
     host="localhost",
     user="root",
     password="12345",
     database="phonepe_db",
     autocommit=True
     )
print(mydb)
cursor=mydb.cursor()

# Creating Options in app
img=Image.open("C:\\Users\\saran\\.vscode\\PhonePe_Logo_PNG1.png")
st.set_page_config(page_title="PhonePe Pulse", page_icon=img, layout="wide", )
icons = {
    "Home": "🏠",
    "Basic insights": "🔄",
    "Top Charts" :"📈",              
    "About": "📊",
    "Explore Data":"👥"
}
SELECT = st.sidebar.selectbox("Choose an option", list(icons.keys()), format_func=lambda option: f'{icons[option]} {option}', key='selectbox')

if SELECT == "About":
    st.subheader("The Indian digital payments story has truly captured the world's imagination."
                 " From the largest towns to the remotest villages, there is a payments revolution being driven by the penetration of mobile phones, mobile internet and state-of-the-art payments infrastructure built as Public Goods championed by the central bank and the government."
                 " Founded in December 2015, PhonePe has been a strong beneficiary of the API driven digitisation of payments in India. When we started, we were constantly looking for granular and definitive data sources on digital payments in India. "
                 "PhonePe Pulse is our way of giving back to the digital payments ecosystem.")
    col1,col2 = st.columns(2)
if SELECT == "Home":
    col1,col2, = st.columns(2)
    col1.image(Image.open("C:\\Users\\saran\\.vscode\\PhonePe_Logo_PNG1.png"),width=500)
    with col1:
        st.subheader("PhonePe  is an Indian digital payments and financial technology company headquartered in Bengaluru, Karnataka, India. PhonePe was founded in December 2015, by Sameer Nigam, Rahul Chari and Burzin Engineer. The PhonePe app, based on the Unified Payments Interface (UPI), went live in August 2016. It is owned by Flipkart, a subsidiary of Walmart.")
        st.download_button("DOWNLOAD THE APP NOW", "C:\\Users\\saran\\.vscode\\Phonepe.mp4")
    with col2:
        st.video("C:\\Users\\saran\\.vscode\\upi.mp4")

#Basic insights
if SELECT == "Basic insights":
    st.title("BASIC INSIGHTS")
    st.write("----")
    st.subheader("Let's know some basic insights about the data")
    options = ["--select--",
               "1. Top 10 states based on year and amount of transaction",
               "2. Least 10 states based on year and amount of transaction",
               "3. Top 10 States and Districts based on Registered_users",
               "4. Least 10 States and Districts based on Registered_users",
               "5. Top 10 Districts based on the Transaction Amount",
               "6. Least 10 Districts based on the Transaction Amount",
               "7. Top 10 Districts based on the Transaction count",
               "8. Least 10 Districts based on the Transaction count",
               "9. Top Transaction types based on the Transaction Amount",
               "10. Top 10 Mobile Brands based on the User count of transaction"]
    select = st.selectbox(":violet[Select the option]",options)
    if select == "1. Top 10 states based on year and amount of transaction":
    
        cursor.execute(
                "SELECT DISTINCT State,Year, SUM(Transaction_amount) AS Total_Transaction_Amount FROM top_trans1 GROUP BY State,Year ORDER BY Total_Transaction_Amount DESC LIMIT 10");
        data = cursor.fetchall()
        columns = ['States', 'Year', 'Transaction_amount']
        df = pd.DataFrame(data, columns=columns, index=range(1, len(data) + 1))

        col1, col2 = st.columns(2)
        with col1:
            st.write(df)
        with col2:
            st.title("Top 10 states based on amount of transaction")
            st.bar_chart(data=df, x="Transaction_amount", y="States")
    if select == "2. Least 10 states based on year and amount of transaction":
        cursor.execute(
            "SELECT DISTINCT State,Year, SUM(Transaction_amount) as Total FROM top_trans1 GROUP BY State, Year ORDER BY Total ASC LIMIT 10");
        data = cursor.fetchall()
        columns = ['States', 'Year', 'Transaction_amount']
        df = pd.DataFrame(data, columns=columns, index=range(1,len(data)+1))
        col1, col2 = st.columns(2)
        with col1:
            st.write(df)
        with col2:
            st.title("Least 10 states based on amount of transaction")
            st.bar_chart(data=df, x="Transaction_amount", y="States")
    elif select == "3. Top 10 States and Districts based on Registered_users":
        cursor.execute("SELECT DISTINCT State, Pincode, SUM(RegisteredUser) AS Users FROM top_user1 GROUP BY State, Pincode ORDER BY Users DESC LIMIT 10;");
        data = cursor.fetchall()
        columns = ['State', 'Pincode', 'Registered_users']
        df = pd.DataFrame(data, columns=columns, index=range(1, len(data) + 1))

        col1, col2 = st.columns(2)
        with col1:
            st.write(df)
        with col2:
            st.title("Top 10 States and Districts based on Registered_users")
            st.bar_chart(data=df, x="Registered_users", y="State")
    elif select == "4. Least 10 States and Districts based on Registered_users":
        cursor.execute("SELECT DISTINCT State, Pincode, SUM(RegisteredUser) AS Users FROM top_user1 GROUP BY State, Pincode ORDER BY Users ASC LIMIT 10");
        data = cursor.fetchall()
        columns = ['State', 'Pincode', 'Registered_users']
        df = pd.DataFrame(data, columns=columns, index=range(1, len(data) + 1))
        col1, col2 = st.columns(2)
        with col1:
            st.write(df)
        with col2:
            st.title("Least 10 States and Districts based on Registered_users")
            st.bar_chart(data=df, x="Registered_users", y="State")
    elif select == "5. Top 10 Districts based on the Transaction Amount":
        cursor.execute("SELECT DISTINCT State, District, SUM(Amount) AS Total FROM map_trans2 GROUP BY State, District ORDER BY Total DESC LIMIT 10");
        data = cursor.fetchall()
        columns = ['States', 'District', 'Amount']
        df = pd.DataFrame(data, columns=columns, index=range(1, len(data) + 1))
        col1, col2 = st.columns(2)
        with col1:
            st.write(df)
        with col2:
            st.title("Top 10 Districts based on Transaction Amount")
            st.bar_chart(data=df, x="District", y="Amount")
    elif select == "6. Least 10 Districts based on the Transaction Amount":
        cursor.execute(
            "SELECT DISTINCT State, District, SUM(Amount) AS Total FROM map_trans2 GROUP BY State, District ORDER BY Total ASC LIMIT 10");
        data = cursor.fetchall()
        columns = ['States', 'District', 'Amount']
        df = pd.DataFrame(data, columns=columns, index=range(1, len(data) + 1))

        col1, col2 = st.columns(2)
        with col1:
            st.write(df)
        with col2:
            st.title("Least 10 Districts based on Transaction Amount")
            st.bar_chart(data=df, x="District", y="Amount")
    elif select == "7. Top 10 Districts based on the Transaction count":
        cursor.execute(
            "SELECT DISTINCT State, District, SUM(Count) AS Counts FROM map_trans2 GROUP BY State, District ORDER BY Counts DESC LIMIT 10");
        data = cursor.fetchall()
        columns = ['States', 'District', 'Count']
        df = pd.DataFrame(data, columns=columns, index=range(1, len(data) + 1))

        col1, col2 = st.columns(2)
        with col1:
            st.write(df)
        with col2:
            st.title("Top 10 Districts based on Transaction Count")
            st.bar_chart(data=df, x="Count", y="District")
    elif select == "8. Least 10 Districts based on the Transaction count":
        cursor.execute(
            "SELECT DISTINCT State, District, SUM(Count) AS Counts FROM map_trans2 GROUP BY State, District ORDER BY Counts ASC LIMIT 10");
        data = cursor.fetchall()
        columns = ['States', 'District', 'Count']
        df = pd.DataFrame(data, columns=columns, index=range(1, len(data) + 1))

        col1, col2 = st.columns(2)
        with col1:
            st.write(df)
        with col2:
            st.title("Top 10 Districts based on the Transaction Count")
            st.bar_chart(data=df, x="Count", y="District")
    elif select == "9. Top Transaction types based on the Transaction Amount":
        cursor.execute(
            "SELECT DISTINCT Transaction_type, SUM(Transaction_amount) AS Amount FROM agg_trans1 GROUP BY Transaction_type ORDER BY Amount DESC LIMIT 5");
        data = cursor.fetchall()
        columns = ['Transaction_type', 'Transaction_amount']
        df = pd.DataFrame(data, columns=columns, index=range(1, len(data) + 1))

        col1, col2 = st.columns(2)
        with col1:
            st.write(df)
        with col2:
            st.title("Top Transaction Types based on the Transaction Amount")
            st.bar_chart(data=df, x="Transaction_type", y="Transaction_amount")
    elif select == "10. Top 10 Mobile Brands based on the User count of transaction":
        cursor.execute(
            "SELECT DISTINCT Brands, SUM(Count) as Total FROM agg_user1 GROUP BY Brands ORDER BY Total DESC LIMIT 10");
        data = cursor.fetchall()
        columns = ['Brands', 'Count']
        df = pd.DataFrame(data, columns=columns, index=range(1, len(data) + 1))

        col1, col2 = st.columns(2)
        with col1:
            st.write(df)
        with col2:
            st.title("Top 10 Mobile Brands based on User count of transaction")
            st.bar_chart(data=df , x="Count", y="Brands")


if SELECT == "Top Charts":
    st.markdown("## :violet[Top Charts]")
    Type = st.sidebar.selectbox("**Type**", ("Transactions", "Users"))
    colum1,colum2= st.columns([1,1.5],gap="large")
    with colum1:
        Year = st.slider("**Year**", min_value=2018, max_value=2023)
        Quarter = st.slider("Quarter", min_value=1, max_value=4)
    
    with colum2:
        st.info(
                """
                #### From this menu we can get insights like :
                - Overall ranking on a particular Year and Quarter.
                - Top 10 State, District, Pincode based on Total number of transaction and Total amount spent on phonepe.
                - Top 10 State, District, Pincode based on Total phonepe users and their app opening frequency.
                - Top 10 mobile brands and its percentage based on the how many people use phonepe.
                """,icon="🔍"
                )
    
# Top Charts - TRANSACTIONS    
    if Type == "Transactions":        
        tab1,tab2,tab3 = st.tabs(["$\huge State $", "$\huge District $","$\huge Pincode $"])
            
        with tab1:
            st.markdown("### :violet[State]")
            cursor.execute(f"select State, sum(Transaction_count) as Total_Transactions_Count, sum(Transaction_amount) as Total from agg_trans1 where year = {Year} and quarter = {Quarter} group by State order by Total desc limit 10")
            df = pd.DataFrame(cursor.fetchall(), columns=['State', 'Transactions_Count','Total_Amount'])
            fig = px.pie(df, values='Total_Amount',
                                names='State',
                                title='Top 10',
                                color_discrete_sequence=px.colors.sequential.Agsunset,
                                hover_data=['Transactions_Count'],
                                labels={'Transactions_Count':'Transactions_Count'})

            fig.update_traces(textposition='inside', textinfo='percent+label')
            st.plotly_chart(fig,use_container_width=True)
            
        with tab2:
            st.markdown("### :violet[District]")
            cursor.execute(f"select District , sum(Count) as Count, sum(Amount) as Total from map_trans2 where year = {Year} and quarter = {Quarter} group by District order by Total desc limit 10")
            df = pd.DataFrame(cursor.fetchall(), columns=['District', 'Transactions_count','Total_Amount'])

            fig = px.pie(df, values='Total_Amount',
                                names='District',
                                title='Top 10',
                                color_discrete_sequence=px.colors.sequential.Agsunset,
                                hover_data=['Transactions_count'],
                                labels={'Transactions_count':'Transactions_count'})

            fig.update_traces(textposition='inside', textinfo='percent+label')
            st.plotly_chart(fig,use_container_width=True)
            
        with tab3:
            st.markdown("### :violet[Pincode]")
            cursor.execute(f"select Pincode, sum(Transaction_Count) as Total_Transactions_Count, sum(Transaction_Amount) as Total from top_trans1 where year = {Year} and quarter = {Quarter} group by Pincode order by Total desc limit 10")
            df = pd.DataFrame(cursor.fetchall(), columns=['Pincode', 'Transactions_Count','Transaction_Amount'])
            fig = px.pie(df, values='Transaction_Amount',
                                names='Pincode',
                                title='Top 10',
                                color_discrete_sequence=px.colors.sequential.Agsunset,
                                hover_data=['Transactions_Count'],
                                labels={'Transactions_Count':'Transactions_Count'})

            fig.update_traces(textposition='inside', textinfo='percent+label')
            st.plotly_chart(fig,use_container_width=True)

    # Top Charts - USERS          
    if Type == "Users":
        tab1,tab2,tab3,tab4 = st.tabs(["$\huge Brand $", "$\huge District $","$\huge Pincode $","$\huge State $"])
        
        with tab1:
            st.markdown("### :violet[Brands]")
            if Year == 2022 and Quarter in [2,3,4]:
                st.markdown("#### Sorry No Data to Display for 2022 Qtr 2,3,4")
            else:
                cursor.execute(f"select Brands, sum(Count) as Count, avg(Percentage)*100 as Percentage from agg_user1 where year = {Year} and quarter = {Quarter} group by Brands order by Count desc limit 10")
                df = pd.DataFrame(cursor.fetchall(), columns=['Brands', 'Count','Percentage'])
                fig = px.bar(df, x="Count",
                                   y="Brands",
                                   title='Top 10',
                                
                                   orientation='h',
                                   color='Percentage',
                                   color_continuous_scale=px.colors.sequential.Agsunset)
                st.plotly_chart(fig,use_container_width=True)   

        with tab2:
            st.markdown("### :violet[District]")
            cursor.execute(f"select District, sum(RegisteredUser) as RegisteredUser, sum(AppOpens) as AppOpens from map_user where year = {Year} and quarter = {Quarter} group by District order by RegisteredUser desc limit 10")
            df = pd.DataFrame(cursor.fetchall(), columns=['District', 'RegisteredUser','TotalAppOpens'])
            df.RegisteredUser = df.RegisteredUser.astype(float)
            fig = px.bar(df, x="RegisteredUser",
                               y="District",
                               title='Top 10',
                               orientation='h',
                               color='RegisteredUser',
                               color_continuous_scale=px.colors.sequential.Agsunset)
            st.plotly_chart(fig,use_container_width=True)
                
        with tab3:
            st.markdown("### :violet[Pincode]")
            cursor.execute(f"select Pincode, sum(RegisteredUser) as RegisteredUser from top_user1 where year = {Year} and quarter = {Quarter} group by Pincode order by RegisteredUser desc limit 10")
            df = pd.DataFrame(cursor.fetchall(), columns=['Pincode', 'RegisteredUser'])
            fig = px.pie(df, values='RegisteredUser',
                               names='Pincode',
                               title='Top 10',
                               color_discrete_sequence=px.colors.sequential.Agsunset,
                               hover_data=['RegisteredUser'])
            fig.update_traces(textposition='inside', textinfo='percent+label')
            st.plotly_chart(fig,use_container_width=True)
            
        with tab4:
            st.markdown("### :violet[State]")
            cursor.execute(f"select State, sum(RegisteredUser) as RegisteredUser, sum(AppOpens) as AppOpens from map_user where year = {Year} and quarter = {Quarter} group by State order by RegisteredUser desc limit 10")
            df = pd.DataFrame(cursor.fetchall(), columns=['State', 'RegisteredUser','AppOpens'])
            fig = px.pie(df, values='RegisteredUser',
                               names='State',
                               title='Top 10',
                               color_discrete_sequence=px.colors.sequential.Agsunset,
                               hover_data=['AppOpens'],
                               labels={'Appopens':'AppOpens'})

            fig.update_traces(textposition='inside', textinfo='percent+label')
            st.plotly_chart(fig,use_container_width=True)    


if SELECT == "Explore Data":
    Year = st.sidebar.slider("**Year**", min_value=2018, max_value=2022)
    Quarter = st.sidebar.slider("Quarter", min_value=1, max_value=4)
    Type = st.sidebar.selectbox("**Type**", ("Transactions", "Users"))
    col1,col2 = st.columns(2)

    # EXPLORE DATA - TRANSACTIONS
    if Type == "Transactions":
        
        # Overall State Data - TRANSACTIONS AMOUNT - INDIA MAP 
        with col1:
            world = pd.read_csv('C:\\Users\\saran\\.vscode\\map_trans.csv')
            st.markdown("## :violet[Overall State Data - Transactions Amount]")
            cursor.execute("SELECT State, SUM(Count) AS Total_Transactions, SUM(Amount) AS Total_amount FROM map_trans2 WHERE Year = 2018 AND Quarter = 3 GROUP BY State ORDER BY State")
            df1 = pd.DataFrame(cursor.fetchall(),columns= ['State', 'Total_Transactions', 'Total_amount'])
            df2 = pd.read_csv("C:\\Users\saran\\Documents\\State.csv")
            df1.State = df2
            df1 = df1.merge(df2, left_on='State', right_on='State')
                                               
            fig = px.choropleth(df1, geojson="https://gist.githubusercontent.com/jbrobst/56c13bbbf9d97d187fea01ca62ea5112/raw/e388c4cae20aa53cb5090210a42ebb9b765c0a36/india_states.geojson",
            featureidkey='properties.ST_NM',
            locations='State',
            color='Total_amount',
            color_continuous_scale='sunset'
            )
            fig.update_geos(fitbounds="locations", visible=False)
            st.plotly_chart(fig,use_container_width=True)

    with col2:
            
            st.markdown("## :violet[Overall State Data - Transactions Count]")
            cursor.execute(f"SELECT State, SUM(Count) AS Total_Transactions, sum(Amount) AS Total_amount FROM map_trans2 WHERE Year = '{Year}' AND Quarter = '{Quarter}' GROUP BY State ORDER BY State")
            df1 = pd.DataFrame(cursor.fetchall(),columns= ['State', 'Total_Transactions', 'Total_amount'])
            df2 = pd.read_csv("C:\\Users\saran\\Documents\\State.csv")
            df1.State = df2

            fig = px.choropleth(df1,geojson="https://gist.githubusercontent.com/jbrobst/56c13bbbf9d97d187fea01ca62ea5112/raw/e388c4cae20aa53cb5090210a42ebb9b765c0a36/india_states.geojson",
                      featureidkey='properties.ST_NM',
                      locations='State',
                      color='Total_Transactions',
                      color_continuous_scale='sunset')

            fig.update_geos(fitbounds="locations", visible=False)
            st.plotly_chart(fig,use_container_width=True)

    # BAR CHART - TOP PAYMENT TYPE
    st.markdown("## :violet[Top Payment Type]")
    cursor.execute(f"SELECT Transaction_type, SUM(Transaction_count) AS Total_Transactions, SUM(Transaction_amount) AS Total_amount FROM agg_trans1 WHERE Year= '{Year}' AND Quarter = '{Quarter}' GROUP BY Transaction_type ORDER BY Transaction_type")
    df = pd.DataFrame(cursor.fetchall(), columns=['Transaction_type', 'Total_Transactions','Total_amount'])

    fig = px.bar(df,
                    title='Transaction_type vs Total_Transactions',
                    x="Transaction_type",
                    y="Total_Transactions",
                    orientation='v',
                    color='Total_amount',
                    color_continuous_scale=px.colors.sequential.Agsunset)
    st.plotly_chart(fig,use_container_width=False) 

    # BAR CHART TRANSACTIONS - DISTRICT WISE DATA            
    st.markdown("# ")
    st.markdown("# ")
    st.markdown("# ")
    st.markdown("## :violet[Select any State to explore more]")
    selected_state = st.selectbox("",
                            ('Andaman & Nicobar','Andhra Pradesh','Arunachal Pradesh','Assam','Bihar',
                            'Chandigarh','Chhattisgarh','Dadra and Nagar Haveli and Daman and Diu','Delhi','Goa','Gujarat','Haryana',
                            'Himachal Pradesh','Jammu & Kashmir','Jharkhand','Karnataka','Kerala','Ladakh','Lakshadweep',
                            'Madhya Pradesh','Maharashtra','Manipur','Meghalaya','Mizoram',
                            'Nagaland','Odisha','Puducherry','Punjab','Rajasthan','Sikkim',
                            'Tamil Nadu','Telangana','Tripura','Uttar Pradesh','Uttarakhand','West Bengal'),index=30)
        
    cursor.execute(f"SELECT State, District,Year,Quarter, SUM(Count) AS Count, SUM(Amount) AS Amount FROM map_trans2 WHERE Year = '{Year}' AND Quarter = '{Quarter}' AND State = '{selected_state}' GROUP BY State, District,Year,Quarter ORDER BY State,District")
    
    df1 = pd.DataFrame(cursor.fetchall(), columns=['State','District','Year','Quarter',
                                                        'Count','Amount'])
    fig = px.bar(df1,
                x="District",
                y="Count",
                title='selected_state',
                orientation='v',
                color='Amount',
                color_continuous_scale=px.colors.sequential.Agsunset)
    st.plotly_chart(fig,use_container_width=True) 

# EXPLORE DATA - USERS      
    if Type == "Users":
        
        # Overall State Data - TOTAL APPOPENS - INDIA MAP
        st.markdown("## :violet[Overall State Data - User App opening frequency]")
        cursor.execute(f"SELECT State, SUM(District), SUM(RegisteredUser) AS RegisteredUser FROM map_user WHERE Year = '{Year}' AND Quarter = '{Quarter}' GROUP BY State ORDER BY RegisteredUser ")
        df1 = pd.DataFrame(cursor.fetchall(), columns=['State','District', 'RegisteredUser'])
        df2 = pd.read_csv('C:\\Users\saran\\Documents\\State.csv')
        df1.State = df2
        
        # BAR CHART TOTAL UERS - DISTRICT WISE DATA s
        st.markdown("## :violet[Select any State to explore more]")
        selected_state= st.selectbox("Select State",
                                      
                                        ('Andaman & Nicobar','Andhra Pradesh','Arunachal Pradesh','Assam','Bihar',
                                        'Chandigarh','Chhattisgarh','Dadra and Nagar Haveli and Daman and Diu','Delhi','Goa','Gujarat','Haryana',
                                        'Himachal Pradesh','Jammu & Kashmir','Jharkhand','Karnataka','Kerala','Ladakh','Lakshadweep',
                                        'Madhya Pradesh','Maharashtra','Manipur','Meghalaya','Mizoram',
                                        'Nagaland','Odisha','Puducherry','Punjab','Rajasthan','Sikkim',
                                        'Tamil Nadu','Telangana','Tripura','Uttar Pradesh','Uttarakhand','West Bengal'),index=30)
                    
        cursor.execute(f"SELECT State,Year,Quarter,District,SUM(RegisteredUser) AS Total_Users FROM map_user WHERE Year = '{Year}' AND Quarter = '{Quarter}' AND State = '{selected_state}' GROUP BY State, District,Year,Quarter ORDER BY State,District")
        
        df = pd.DataFrame(cursor.fetchall(), columns=[ 'State','Year','Quarter','District','Total_Users'])
       
        
        fig = px.bar(df,
                     title=selected_state,
                     x="District",
                     y="Total_Users",
                     orientation='v',
                     color='Total_Users',
                     color_continuous_scale=px.colors.sequential.Agsunset)
        st.plotly_chart(fig,use_container_width=True)