import os
file_names = []

fl = os.listdir('C:/Users/avtom/Visual_Studio_Code/Projects/Test_projects/FreelanceOfLife/cesis/fonts/OpenSans')

for i in fl:
    file_names.append(i.split('.')[0])

for j in set(file_names):
    path = "../fonts/OpenSans"
    str = "@font-face {" \
          "\n" \
          "    font-family: 'OpenSans';\n" \
          f"    src: local('{j}'),\n" \
          f"         url('{path}/{j}.woff2') format('woff2'),\n" \
          f"         url('{path}/{j}.woff') format('woff');\n" \
          "    font-weight: normal;\n" \
          "    font-style: normal;\n" \
          "    font-display: swap;\n" \
          "}"
    print(str)
    print('\n')

