import os 
import shutil

def copy_static_into_docs(path):

    if not os.path.isdir("docs"):
        os.mkdir("docs")

    if path == "static":
        shutil.rmtree("docs")
        os.mkdir("docs")
    
    if os.path.isfile(path):
        docs_path = path.replace("static","docs")
        shutil.copy(path,docs_path)

    if os.path.isdir(path):
        for entry in os.listdir(path):
            docs_path = path.replace("static","docs")
            if not os.path.isdir(docs_path):
                os.mkdir(docs_path)
            copy_static_into_docs(os.path.join(path,entry))
    
    
    
        
        