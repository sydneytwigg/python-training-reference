from pyflowchart import Flowchart
with open('ntol_script.py') as f:
    code = f.read()

fc = Flowchart.from_code(code)
print(fc.flowchart())