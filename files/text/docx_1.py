from docx import Document

def text_repl(file_name, text_1, text_2):
    doc_name = Document(file_name)
    for par in doc_name.paragraphs:
        if text_1 in par.text:
            par.text = par.text.replace(text_1, text_2)
            doc_name.save(file_name)
            return "Replace complete"
    return False
    

print(text_repl("demo.docx", "first item in unordered list", "second item in unordered list"))
