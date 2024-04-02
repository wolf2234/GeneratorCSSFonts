import os
file_names = []

fl = os.listdir('C:/Users/avtom/Visual_Studio_Code/ДНТБ-Projects/Test_projects/FreelanceOfLife/HomeWork/lesson_6-10/DBS-Interactive/fonts/NunitoSans')

for i in fl:
    file_names.append(i.split('.')[0])

for j in set(file_names):
    path = "../fonts/NunitoSans"
    str = "@font-face {" \
          "\n" \
          "    font-family: 'NunitoSans'; \n" \
          f"    src: url('{path}/{j}.woff2') format('woff2'), \n" \
          f"         url('{path}/{j}.woff') format('woff'); \n" \
          "    font-weight: normal; \n" \
          "    font-style: normal; \n" \
          "    font-display: swap; \n" \
          "}"
    print(str)
    print('\n')

