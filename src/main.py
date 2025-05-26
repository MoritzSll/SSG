import sys
from generate_page import load_content
from copy_static import copy_static_into_docs


def main():
   basepath = ""
   if len(sys.argv) > 1:
      basepath = sys.argv[1]
   else:
      basepath = "/"
   print(basepath)

   copy_static_into_docs("static")
   load_content("content",basepath)

main()


