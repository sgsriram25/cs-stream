import streamlit as st
import pandas as pd
import plotly.graph_objects as go
import chart_studio.plotly as py
from plotly import offline as pyoff

tx_data = pd.read_csv('data.csv', encoding= "ISO-8859-1")
tx_data['InvoiceDate'] = pd.to_datetime(tx_data['InvoiceDate'])
tx_data['InvoiceYearMonth'] = tx_data['InvoiceDate'].map(lambda date: 100*date.year + date.month)
st.set_page_config(layout = "wide")
st.title("Customer Segmentation Stark Shop Dashboard")

side = st.sidebar.selectbox('Select page',
  ['Monthly Customer Status','New vs Existing Customers','Segmentation based on UK','Product Clustering','RFM Clustering'])

if side == 'Monthly Customer Status':
    
    
    #st.set_page_config(layout = "wide")
    col1, col2 = st.columns(2)
    with col1:
        st.markdown("""Monthly Revenue Line graph""")
        first = pd.read_csv('first.csv')
        plot_data = [
            go.Scatter(
                x=first['InvoiceYearMonth'],
                y=first['Revenue'],
            )
        ]
        
        plot_layout = go.Layout(
                xaxis={"type": "category"},
                title='Montly Revenue'
            )
        
        fig = go.Figure(data=plot_data, layout=plot_layout)
        
        st.plotly_chart(fig, use_container_width=True)
    with col2:
        st.markdown("""Monthly Revenue Growth Rate""")
        month = pd.read_csv('month.csv')
        plot_data10 = [
          go.Scatter(
            x=month['InvoiceYearMonth'],
            y=month['MonthlyGrowth'],
          )
        ]
    
        plot_layout = go.Layout(
             xaxis={"type": "category"},
             title='Montly Growth Rate'
        )
    
        fig10 = go.Figure(data=plot_data10, layout=plot_layout)        
        st.plotly_chart(fig10, use_container_width=True)
    
    st.markdown("""Monthly Order Status""")
    page = st.selectbox('Select page',['Monthly Active Customers','Monthly Total Order','Monthly Average Order'])
    
    if page == 'Monthly Active Customers':
        active = pd.read_csv('active.csv')
        plot_data11 = [
            go.Bar(
                x=active['InvoiceYearMonth'],
                y=active['CustomerID'],
                )
            ]

        plot_layout = go.Layout(
            xaxis={"type": "category"},
            title='Monthly Active Customers'
            )

        fig11 = go.Figure(data=plot_data11, layout=plot_layout)
        st.plotly_chart(fig11, use_container_width=True)
    
    elif page == 'Monthly Total Order':
         sale = pd.read_csv('sale.csv')
         plot_data12 = [
             go.Bar(
                 x=sale['InvoiceYearMonth'],
                 y=sale['Quantity'],
         )
        ]

         plot_layout = go.Layout(
                    xaxis={"type": "category"},
                    title='Monthly Total # of Order'
                )

         fig12 = go.Figure(data=plot_data12, layout=plot_layout) 
         st.plotly_chart(fig12, use_container_width=True)
         
    else:
         avg = pd.read_csv('avg.csv')
         plot_data13 = [
             go.Bar(
                 x=avg['InvoiceYearMonth'],
                 y=avg['Revenue'],
                 )
             ]

         plot_layout = go.Layout(
             xaxis={"type": "category"},
             title='Monthly Order Average Revenue'
          )
         fig13 = go.Figure(data=plot_data13, layout=plot_layout)
         st.plotly_chart(fig13, use_container_width=True)
         

elif side == 'New vs Existing Customers':
    st.markdown("""New vs Existing """)
    comp = pd.read_csv('comp.csv')
    plot_data14 = [
    go.Scatter(
        x=comp.query("UserType == 'Existing'")['InvoiceYearMonth'],
        y=comp.query("UserType == 'Existing'")['Revenue'],
        name = 'Existing'
    ),
    go.Scatter(
        x=comp.query("UserType == 'New'")['InvoiceYearMonth'],
        y=comp.query("UserType == 'New'")['Revenue'],
        name = 'New'
    )
    ]

    plot_layout = go.Layout(
        xaxis={"type": "category"},
        title='New vs Existing'
    )
    fig14 = go.Figure(data=plot_data14, layout=plot_layout)
    st.plotly_chart(fig14, use_container_width=True)
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    tx_uk = tx_data.query("Country=='United Kingdom'").reset_index(drop=True)
    tx_monthly_active = tx_uk.groupby('InvoiceYearMonth')['CustomerID'].nunique().reset_index()
    
    plot_data2 = [
        go.Bar(
            x=tx_monthly_active['InvoiceYearMonth'],
            y=tx_monthly_active['CustomerID'],
        )
    ]
    
    plot_layout = go.Layout(
            xaxis={"type": "category"},
            title='Monthly Active Customers'
        )
    
    fig2 = go.Figure(data=plot_data2, layout=plot_layout)
    st.plotly_chart(fig2, use_container_width=True)
    
    st.markdown("""Histogram 2""")
    page = st.selectbox('Select page',['Recency','Frequency'])
    
    if page == 'Recency':
        sec = pd.read_csv('second.csv')
        plot_data3 = [
            go.Histogram(
                x=sec['Recency']
                )
            ]
    
        plot_layout = go.Layout(
                title='Recency'
                )
        fig3 = go.Figure(data=plot_data3, layout=plot_layout)
        st.plotly_chart(fig3, use_container_width=True)
    
    else:
         fin = pd.read_csv('final.csv')
         plot_data4 = [
             go.Histogram(
                 x=fin.query('Frequency < 1000')['Frequency']
                 )
             ]
         plot_layout = go.Layout(
                    title='Frequency'
                    )
         fig4 = go.Figure(data=plot_data4, layout=plot_layout)  
         st.plotly_chart(fig4, use_container_width=True)