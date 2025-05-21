import os 
import shutil

def copy_static_into_public(path):

    if path == "static":
        shutil.rmtree("public")
        os.mkdir("public")
    
    if os.path.isfile(path):
        public_path = path.replace("static","public")
        shutil.copy(path,public_path)

    if os.path.isdir(path):
        for entry in os.listdir(path):
            public_path = path.replace("static","public")
            if not os.path.isdir(public_path):
                os.mkdir(public_path)
            copy_static_into_public(os.path.join(path,entry))
    
    
    
        
        