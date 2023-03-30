import psycopg2

conn = psycopg2.connect(
    dbname = 'atmmachine',
    user = 'postgres',
    password = '1921u0030'
)

cur = conn.cursor()

cur.execute("select * from atmusers")

user_input = int(input(" 1. Register: \n 2. Login: \n"))

if user_input == 1:
    print("Register \n")
    username = input("Enter your name: \n")
    password = input("Enter your password: \n")

    query = f"insert into atmusers (username, password) values('{username}', '{password}')"
    data = (username,password)


    cur.execute(query)

    conn.commit()

    if cur.rowcount > 0:
        print("Registered")
        print("signup bonus 500 credited \n")
    
elif user_input == 2:
    print("Login \n")
    username = input("Enter your name: \n")
    password = input("Enter your password: \n")

    queryy = f"select * from atmusers where username = '{username}'"
    cur.execute(queryy)

    conn.commit()

    if cur.rowcount > 0:
        print("Login successfull \n")
        user_input = 1


atm_functionalities = int(input(" 1. To view the total: \n 2. To deposit amount: \n 3. To withdraw amount: \n"))

if atm_functionalities == 1:
    cur.execute(f"select totalamount from atmusers where username = '{username}'")
    print(cur.fetchone())

elif atm_functionalities == 2:
    deposited_value = input("How much you need to deposit: \n")
    queryyy = f"update atmusers set totalamount = '{deposited_value}' + totalamount where username = '{username}'"

    cur.execute(queryyy)

    conn.commit()

    print("success")

elif atm_functionalities == 3:
    withdraw_value = input("How much you need to withdraw: \n")
    query = f"update atmusers set totalamount = '{withdraw_value}' - totalamount where username = '{username}'"

    cur.execute(query)

    conn.commit()

    print("success")

else:
    print("Please enter a correct number!!! \n")

cur.close()

conn.close()