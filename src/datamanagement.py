import pandas as pd
import os

# Using Pandas directly here because it handles large multi-student data better
data_file = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'data', 'student_marks.csv')

def load_complete_data():
    # it will load complete data
    if not os.path.exists(data_file):
        return pd.DataFrame()
    return pd.read_csv(data_file)

def take_studentdata(student_id):
    # provides marks for a specified student
    df = load_complete_data()
    if df.empty:
        return []
    
    # this will help gettong specifid student ID
    student_records = df[df['Student_ID'] == student_id]
    

    # makingfor other module easy to process we will convert list into dictionary
    return student_records.to_dict('records')

def take_student_name(student_id):

    # it will help us find name of that particular id easily
    df = load_complete_data()
    if df.empty: 
        return "NO DATA FOUND"
    result = df[df['Student_ID'] == student_id]['Name'].unique()
    return result[0] if len(result) > 0 else "INVALID"

def add_record(student_id, name, sem, sub, cred, marks):
    # This will add the new data given to the list
    new_row = pd.DataFrame([[student_id, name, sem, sub, cred, marks]], 
                           columns=["Student_ID", "Name", "Semester", "Subject", "Credits", "Marks"])
    
    # Append to CSV mode='a' (append) without header
    new_row.to_csv(data_file, mode='a', header=not os.path.exists(data_file), index=False)
    return True