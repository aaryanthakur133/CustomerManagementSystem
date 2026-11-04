import os
import streamlit as st
import pandas as pd
import mysql.connector
import datetime

st.set_page_config(page_title="Customer Management System",
page_icon="https://c8.alamy.com/comp/KDR54Y/illustrative-diagram-of-customer-relationship-management-for-managing-KDR54Y.jpg")

st.title("CUSTOMER MANAGEMENT SYSTEM")

# Calling Database

def connect_db():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password=os.getenv("DB_PASSWORD", ""),
        database="CustomerManagement"
    )

# Sidebar Options :

choice=st.sidebar.selectbox("My Menu",(
    "Home",
    "User",
    "Customers",
    "Reviews",
    "Dashboard"))

# HOME PANEL :- 

if(choice=="Home"):
    
    st.write("This is a web application of Customer Management System project")
    st.markdown("<center><h1>WELCOME</h1></center>",unsafe_allow_html=True)
    st.image("https://www.questionpro.com/blog/wp-content/uploads/2023/10/Customer-Management.jpg")

# USER PANEL :- 

elif(choice=="User"):

    if 'LOGIN' not in st.session_state:
        st.session_state['LOGIN']=False

    if not st.session_state['LOGIN']:
        Uid=st.text_input("Enter User ID")
        Updw=st.text_input("Enter Password",type="password")
        btn=st.button("LOGIN")

        if btn:

            mydb=connect_db()
            c=mydb.cursor()
            c.execute("select * from Users")

            for r in c:
                if(r[0]==Uid and r[2]==Updw):
                    st.session_state['LOGIN']=True
                    break

            if(not st.session_state['LOGIN']):
                st.write("Incorrect ID and Password")

    if(st.session_state['LOGIN']):

        st.success("Login Successful")

        logout_btn=st.button("LOGOUT")

        if logout_btn:
            st.session_state['LOGIN']=False
            st.success("Logout Successful")
            st.rerun()

# User Options :            


        choice2 = st.selectbox("Feature", (
            "None",
            "── USERS ──",
            "View all Users",
            "Add a User",
            "Delete a User",            
            "── CUSTOMERS ──",
            "View all Customers",
            "Search Customer",
            "Add a Customer",
            "Edit Customer",
            "Delete Customer",
            "── PRODUCTS ──",
            "View all Products",
            "Search Product",
            "Add a Product",
            "Edit Product",
            "Delete a Product",
            "── ORDERS ──",
            "View all PurchasedItems",
            "View all ReturnedItems",
            "── REVIEWS ──",
            "View all Reviews",
            "Delete a Review"))
 
        mydb = connect_db()

        if choice2 == "View all Users":
            df = pd.read_sql("SELECT user_id, name FROM Users", mydb)
            st.dataframe(df, use_container_width=True)
 
        elif choice2 == "Add a User":
            uid  = st.text_input("New User ID")
            unam = st.text_input("Username")
            upas = st.text_input("Password", type="password")
            if st.button("Add User"):
                c = mydb.cursor()
                c.execute("INSERT INTO Users VALUES(%s,%s,%s)",
                          (uid, unam, hash_password(upas)))
                mydb.commit()
                st.success("User Added Successfully!")
 
        elif choice2 == "Delete a User":
            uid = st.text_input("User ID to Delete")
            if st.button("Delete User"):
                c = mydb.cursor()
                c.execute("DELETE FROM Users WHERE user_id=%s", (uid,))
                mydb.commit()
                st.success("User Deleted Successfully!")

 
        elif choice2 == "View all Customers":
            df = pd.read_sql("SELECT * FROM Customer", mydb)
            st.dataframe(df, use_container_width=True)
 
        elif choice2 == "Search Customer":
            keyword = st.text_input("Search by Customer ID or Name")
            if st.button("Search"):
                df = pd.read_sql(
                    "SELECT * FROM Customer WHERE customer_id LIKE %s OR name LIKE %s",
                    mydb, params=(f"%{keyword}%", f"%{keyword}%")
                )
                if df.empty:
                    st.warning("No customer found.")
                else:
                    st.dataframe(df, use_container_width=True)
 
        elif choice2 == "Add a Customer":
            cid  = st.text_input("Customer ID")
            nam  = st.text_input("Customer Name")
            ph   = st.text_input("Phone Number")
            gen  = st.selectbox("Gender", ("Male", "Female", "Other"))
            adrs = st.text_input("Address")
            pas  = st.text_input("Password", type="password")
            if st.button("Add Customer"):
                c = mydb.cursor()
                c.execute("INSERT INTO Customer VALUES(%s,%s,%s,%s,%s,%s)",
                          (cid, nam, ph, gen, adrs, pas))
                mydb.commit()
                st.success("Customer Added Successfully!")
 
        elif choice2 == "Edit Customer":
            cid = st.text_input("Enter Customer ID to Edit")
            if st.button("Load"):
                c = mydb.cursor()
                c.execute("SELECT * FROM Customer WHERE customer_id=%s", (cid,))
                row = c.fetchone()
                if row:
                    st.session_state['edit_cust'] = row
                else:
                    st.warning("Customer not found.")
 
            if 'edit_cust' in st.session_state:
                row = st.session_state['edit_cust']
                new_nam  = st.text_input("Name",    value=row[1])
                new_ph   = st.text_input("Phone",   value=row[2])
                new_gen  = st.text_input("Gender",  value=row[3])
                new_adrs = st.text_input("Address", value=row[4])
                if st.button("Update Customer"):
                    c = mydb.cursor()
                    c.execute("""UPDATE Customer
                                 SET name=%s, phone=%s, gender=%s, address=%s
                                 WHERE customer_id=%s""",
                              (new_nam, new_ph, new_gen, new_adrs, row[0]))
                    mydb.commit()
                    del st.session_state['edit_cust']
                    st.success("Customer Updated Successfully!")
 
        elif choice2 == "Delete Customer":
            cid = st.text_input("Customer ID to Delete")
            if st.button("Delete Customer"):
                c = mydb.cursor()
                c.execute("DELETE FROM Customer WHERE customer_id=%s", (cid,))
                mydb.commit()
                st.success("Customer Deleted Successfully!")
 
 
        elif choice2 == "View all Products":
            df = pd.read_sql("SELECT * FROM Product", mydb)
            st.dataframe(df, use_container_width=True)
 
        elif choice2 == "Search Product":
            keyword = st.text_input("Search by Product ID or Name")
            if st.button("Search"):
                df = pd.read_sql(
                    "SELECT * FROM Product WHERE product_id LIKE %s OR product_name LIKE %s",
                    mydb, params=(f"%{keyword}%", f"%{keyword}%")
                )
                if df.empty:
                    st.warning("No product found.")
                else:
                    st.dataframe(df, use_container_width=True)
 
        elif choice2 == "Add a Product":
            pid = st.text_input("Product ID")
            nam = st.text_input("Product Name")
            amt = st.text_input("Product Amount")
            if st.button("Add Product"):
                c = mydb.cursor()
                c.execute("INSERT INTO Product VALUES(%s,%s,%s)", (pid, nam, amt))
                mydb.commit()
                st.success("Product Added Successfully!")
 
        elif choice2 == "Edit Product":
            pid = st.text_input("Enter Product ID to Edit")
            if st.button("Load"):
                c = mydb.cursor()
                c.execute("SELECT * FROM Product WHERE product_id=%s", (pid,))
                row = c.fetchone()
                if row:
                    st.session_state['edit_prod'] = row
                else:
                    st.warning("Product not found.")
 
            if 'edit_prod' in st.session_state:
                row = st.session_state['edit_prod']
                new_nam = st.text_input("Product Name",   value=row[1])
                new_amt = st.text_input("Product Amount", value=str(row[2]))
                if st.button("Update Product"):
                    c = mydb.cursor()
                    c.execute("UPDATE Product SET product_name=%s, amount=%s WHERE product_id=%s",
                              (new_nam, new_amt, row[0]))
                    mydb.commit()
                    del st.session_state['edit_prod']
                    st.success("Product Updated Successfully!")
 
        elif choice2 == "Delete a Product":
            pid = st.text_input("Product ID to Delete")
            if st.button("Delete Product"):
                c = mydb.cursor()
                c.execute("DELETE FROM Product WHERE product_id=%s", (pid,))
                mydb.commit()
                st.success("Product Deleted Successfully!")
 
        elif choice2 == "View all PurchasedItems":
            df = pd.read_sql("SELECT * FROM PurchaseItems", mydb)
            st.dataframe(df, use_container_width=True)
 
        elif choice2 == "View all ReturnedItems":
            df = pd.read_sql("SELECT * FROM ReturnItems", mydb)
            st.dataframe(df, use_container_width=True)

        elif choice2=="View all Reviews":
            mydb=connect_db()
            df=pd.read_sql("select * from Review",mydb)
            st.dataframe(df)

        elif choice2 == "Delete a Review":
            pid = st.text_input("Product ID")
            cid = st.text_input("Customer ID")
            if st.button("Delete Review"):
                c = mydb.cursor()
                c.execute("DELETE FROM Review WHERE product_id=%s AND customer_id=%s",
                          (pid, cid))
                mydb.commit()
                st.success("Review Deleted")

 
# CUSTOMER PANEL :- 

elif(choice=="Customers"):

    if 'CLOGIN' not in st.session_state:
        st.session_state['CLOGIN']=False

    if not st.session_state['CLOGIN']:
        Cid=st.text_input("Enter Customer ID")
        Cpdw=st.text_input("Enter Password",type="password")
        btn=st.button("CLOGIN")

        if btn:

            mydb=connect_db()
            c=mydb.cursor()
            c.execute("select * from Customer")

            for r in c:
                if(r[0]==Cid and r[5]==Cpdw):
                    st.session_state['CLOGIN']=True
                    break

            if(not st.session_state['CLOGIN']):
                st.write("Incorrect ID and Password")

    if(st.session_state['CLOGIN']):

        st.success("Login Successful")

        logout_btn=st.button("CLOGOUT")

        if logout_btn:
            st.session_state['CLOGIN']=False
            
            st.success("Logout Successful")
            st.rerun()

# Customer Options :
            
        choice2=st.selectbox("Feature",(
            "None",
            "View all Product",
            "Buy a Product",
            "Return a Product"))

        if(choice2=="View all Product"):
            mydb=connect_db()
            df=pd.read_sql("select * from Product",mydb)
            st.dataframe(df)

        elif(choice2=="Buy a Product"):

            pid=st.text_input("Enter Product id :")
            cid=st.text_input("Enter Customer id :")
            nam=st.text_input("Enter Product Name :")
            dat=st.text_input("Enter Product Buy Date (in yyyy-mm-dd format) :")
            sat=st.text_input("Enter Buy or NotBuy:")
            btn2=st.button("Buy Product")

            if btn2:

                mydb=connect_db()
                c=mydb.cursor()
                c.execute("INSERT INTO PurchaseItems values(%s,%s,%s,%s,%s)",
                          (pid,cid,nam,dat,sat))
                
                mydb.commit()
                st.header("Product Buyed Successfully")

        elif(choice2=="Return a Product"):

            pid1=st.text_input("Enter Product id :")
            cid1=st.text_input("Enter Customer id :")
            nam1=st.text_input("Enter Product Name :")
            dat1=st.text_input("Enter Product Return Date (in yyyy-mm-dd format) :")
            sat1=st.text_input("Enter Return or NotReturn:")
            btn2=st.button("Return Product")

            if btn2:

                mydb=connect_db()
                c=mydb.cursor()
                c.execute("INSERT INTO ReturnItems values(%s,%s,%s,%s,%s)",
                          (pid1,cid1,nam1,dat1,sat1))
                
                mydb.commit()
                st.header("Product Returned Successfully")


# REVIEW PANEL :- 

elif(choice =="Reviews"):

        choice2=st.selectbox("Feature",(
            "None",
            "View all Reviews",
            "Write your Review"))

        if(choice2=="View all Reviews"):
            mydb=connect_db()
            df=pd.read_sql("select * from Review",mydb)
            st.dataframe(df)

        elif choice2 == "Write your Review":
            pid     = st.text_input("Product ID")
            cust_id = st.text_input('CUSTOMER_ID')
            rat  = st.text_input("Add Rating ( min_value=1, max_value=5)" )
            rew  = st.text_area("Review (max 200 characters)", max_chars=200)
            btn2=st.button("Add Review")

            if btn2:

                mydb=connect_db()
                c=mydb.cursor()
                c.execute("INSERT INTO Review values(%s,%s,%s,%s)",
                          (pid,cust_id,rat,rew))
                
                mydb.commit()
                st.header("Review Added Successfully")    

    
# DASHBOARD PANEL :- 

elif choice == "Dashboard":

    st.header("📊 DASHBOARD")
    mydb  = connect_db()
    today = str(datetime.date.today())
    c     = mydb.cursor()

    c.execute("SELECT count(*) FROM Customer")
    total_customer = c.fetchone()[0]

    c.execute("SELECT count(*) FROM Product")
    total_product = c.fetchone()[0]

    c.execute("SELECT count(*) FROM PurchaseItems WHERE purchase_date=%s", (today,))
    total_purchase_today = c.fetchone()[0]

    c.execute("SELECT count(*) FROM ReturnItems WHERE return_date=%s", (today,))
    total_return_today = c.fetchone()[0]

    c.execute("SELECT count(*) FROM Review")
    total_reviews = c.fetchone()[0]

    c.execute("SELECT ROUND(AVG(rating),1) FROM Review")
    avg_rating = c.fetchone()[0] or 0

    total_order_today = total_purchase_today + total_return_today

    st.subheader("Overview")
    col1, col2, col3 = st.columns(3)
    col1.metric("👥 Customers",       total_customer)
    col2.metric("📦 Products",        total_product)
    col3.metric("🛒 Purchases Today", total_purchase_today)

    col4, col5, col6 = st.columns(3)
    col4.metric("↩️ Returns Today",   total_return_today)
    col5.metric("📋 Total Reviews",   total_reviews)
    col6.metric("⭐ Avg Rating",      avg_rating)

    st.divider()
                
