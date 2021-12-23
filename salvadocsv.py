from docxtpl import DocxTemplate
#aqui seleciona a fonte de dados 
with open("info.csv","r") as csvf:
    op = csvf.readlines()

#pula o titulo roda da segunda linha
for i in op[1:]:

    workplan = i.split(",")[0]
    nrelatorio = i.split(",")[1]
    executante1 = i.split(",")[2]
    executante2 = i.split(",")[3]
    numerotitulo = i.split(",")[4]
    data = i.split(",")[5]
    rev = i.split(",")[6]

    #aqui seleciona o template
    doc = DocxTemplate("relatoriotmp.docx")
    context = { 
        'nrelatorio': nrelatorio,
        'executante1': executante1,
        'executante2': executante2,
        'numerotitulo': numerotitulo,
        'data': data,
        'rev':rev,
  
        }

    doc.render(context)

   #Cria o arquivo e seta o nome
    doc.save(f"{nrelatorio}_relatorio.docx")
