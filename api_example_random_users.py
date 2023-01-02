from randomuser import RandomUser
import pandas as pd

# Crear obj randomUser
r = RandomUser()

lista_users = r.generate_users(10)
nombre = r.get_full_name()
# obtener el nombre completo y los emails de los 10 usuarios random
for user in lista_users:
    print(user.get_full_name(), " ", user.get_email())

# generar una tabla con la información que nos interesa y crear un dataframe panda
def get_users():
    users = []

    for user in RandomUser.generate_users(10):
        users.append({"Name" : user.get_full_name(), "Email" : user.get_email(), "City": user.get_city(), "Picture": user.get_picture()})
        return pd.DataFrame(users)

print(get_users())












"""
Get Methods
get_cell()
get_city()
get_dob()
get_email()
get_first_name()
get_full_name()
get_gender()
get_id()
get_id_number()
get_id_type()
get_info()
get_last_name()
get_login_md5()
get_login_salt()
get_login_sha1()
get_login_sha256()
get_nat()
get_password()
get_phone()
get_picture()
get_postcode()
get_registered()
get_state()
get_street()
get_username()
get_zipcode()

"""