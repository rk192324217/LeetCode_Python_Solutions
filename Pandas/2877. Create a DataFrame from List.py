import pandas as pd

def createDataframe(student_data) -> pd.DataFrame:
    col_names=["student_id","age"]
    return pd.DataFrame(student_data,columns=col_names)