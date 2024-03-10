def generate_ddl(df):
    # Extract the table name
    table_name = df.iloc[0, 0]
    # Extract the column names
    column_names = df.iloc[1, :].dropna()
    # Extract the data
    data = df.iloc[2:, :].dropna()

    # Generate the DDL statement
    ddl = f"CREATE TABLE {table_name} (\n"
    for column_name in column_names:
        ddl += f"{column_name} VARCHAR(255),\n"
    ddl = ddl.rstrip(',\n') + "\n);"
    print(ddl)
    return data, table_name, ddl


def generate_dml(data, table_name):
    for _, row in data.iterrows():
        dml = f"INSERT INTO {table_name} VALUES ("
        for value in row:
            dml += f"'{value}', "
        dml = dml.rstrip(', ') + ");"
        print(dml)
    return dml
