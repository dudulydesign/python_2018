import os, sys

def setup():
  BASE_DIR = os.path.abspath(os.path.dirname(__file__))

  sys.path.insert(0, BASE_DIR)
  sys.path.insert(0, os.path.join(BASE_DIR, "medusa_site"))

  os.environ["DJANGO_SETTINGS_MODULE"] = "medusa_site.settings"

  import django
  django.setup()


def main():
  setup()

  argv = list(sys.argv)
  argv.pop(0)

  import imp

  for srcpath in argv:
    print srcpath
    
    mod = imp.load_source("test", srcpath)
    mod.main()

if __name__ == "__main__":
  main()
