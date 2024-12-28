import streamlit as st
import mysql.connector
def connection(**kwargs):
    db_connection = mysql.connector.connect(
    host="sql12.freesqldatabase.com",
    user="sql12754553",
    password="xsSDGidrJq",
    database="sql12754553"  
    )
    cursor = db_connection.cursor()
    insert_query = "INSERT INTO emp_data (name, father, age, cnic, cnic_issue, cnic_expiry, contact, kin, kin_relation, kin_contact, kin_cnic, address) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
    employee_data = (kwargs['name'] ,kwargs['father'], kwargs['age'], kwargs['cnic'], kwargs['cnic_issue'], kwargs['cnic_expiry'], kwargs['contact'], kwargs['kin'], kwargs['kin_relation'], kwargs['kin_contact'], kwargs['kin_cnic'], kwargs['kin_address'])
    cursor.execute(insert_query, employee_data)
    db_connection.commit()
    db_connection.close()


def number_validation(num, length):
    if num.isdigit() and len(num) == length:
        return True
    else:
        if num:
            st.error("Number is not valid")
        return False
    

    


kin_opt = ["Select Releation", "Father", "Mother", "Brother", "Sister"]
with st.form(key="employee-form"):
    st.title("Metaviz Pro Employee Information")
    st.write("This is a sample employee information page for Metaviz Pro")
    name = st.text_input("Name")
    father = st.text_input("Fathe Name")
    age = st.slider("Age:", 0, 100, 18)
    cnic = st.text_input("CNIC No.", placeholder="3520012345678")
    cnic_num_valid = number_validation(cnic, 13)
    cnic_issue = st.date_input("Cnic Issue Date", value=None)
    cnic_expiry = st.date_input("Cnic Expiry Date", value=None)
    contact = st.text_input("Contact No.", placeholder="03000000000")
    phone_valid = number_validation(contact, 11)
    kin = st.text_input("Kin Name")
    kin_relation = st.selectbox("Releationship With Kin", kin_opt)
    kin_contact = st.text_input("Kin's Contact No.", placeholder="03000000000")
    kin_phone_valid = number_validation(kin_contact, 11)
    kin_cnic = st.text_input("Kin's Cnic No.", placeholder="3520012345678")
    kin_cnic_valid = number_validation(kin_cnic, 13)
    kin_address = st.text_input("Kin's Address", placeholder="House no 1, Street no 1, Lahore, Pakistan")

    check = st.checkbox("Are you sure, the details you filled are correct?")

    submit_button = st.form_submit_button("Submit Now")
    
    if submit_button:
        if cnic_num_valid and phone_valid and kin_contact and kin_cnic_valid and check:
            st.success("Form submitted successfully!")
            connection(name=name, father=father, age=age, cnic=cnic, cnic_issue=cnic_issue, cnic_expiry=cnic_expiry, contact=contact, kin=kin, kin_relation=kin_relation, kin_contact=kin_contact, kin_cnic=kin_cnic, kin_address=kin_address)
        else:
            st.error("Please check the box or make sure all details are valid before submitting.")
    elif not check:
        st.warning("Please check the box to confirm your details.")
    

