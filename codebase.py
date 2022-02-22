import os

path    = os.getcwd()
result  = {} 

for file in os.listdir():

    if file != 'codebase.py':
        
        f             = open(file)
        current       = ""
        # imported_comp = []

        for line in f:

            # get the imported files
            '''if "import" in line:

                comp = line.split()[-1]
                
                imported_comp.append(comp)'''

            if 'def' in line:
                curr_func_name = line[4:line.index('(')]
                current   = "".join([x for x in curr_func_name])

                result[current] = []

            elif '(' and ')' in line and '.' not in line:

                check = line[line.index('(')+1:line.index(')')]

                if check == '' or "'" not in check and '"' not in check:

                    used_func_name_list = line[0:line.index('(')]
                    used_func_name      = "".join(used_func_name_list.split())

                    result[current].append(used_func_name)

print(result)