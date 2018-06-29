import os, sys
from optparse import OptionParser

def main():
  BASE_DIR = os.path.abspath(os.path.dirname(__file__))

  sys.path.insert(0, os.path.join(BASE_DIR, "medusa_site"))

  os.environ["DJANGO_SETTINGS_MODULE"] = "medusa_site.settings"

  import django
  django.setup()

  from django.core.handlers.wsgi import WSGIHandler
  from twisted.web import server
  from twisted.web.wsgi import WSGIResource
  from twisted.python.threadpool import ThreadPool
  from twisted.application import service, strports
  from twisted.internet import reactor

  port = 8000

  opt_parser = OptionParser()
  opt_parser.add_option("-p", "--port", dest="port")

  opts, args = opt_parser.parse_args()

  if opts.port is not None:
    port = int(opts.port)

  reactor.suggestThreadPoolSize(1024)

  application = WSGIHandler()

  wsgi_resource = WSGIResource(reactor, reactor.getThreadPool(), application)

  site = server.Site(wsgi_resource)
  reactor.listenTCP(port, site)

  print "start wangzu company management site at :%s" % port

  try:
    reactor.run()

  except KeyboardInterrupt:
    reactor.stop()

if __name__ == "__main__":
  main()
