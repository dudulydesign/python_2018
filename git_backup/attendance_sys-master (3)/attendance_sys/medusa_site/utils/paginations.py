import urllib
from django.utils.safestring import mark_safe
from django.core.paginator import Paginator


def generate_pagination(request, qs, perpage=50):

  page_num = 1
  try:
    page_num = int(request.GET["page"])
  except:
    pass

  if page_num < 1:
    page_num = 1

  print "page_num", page_num

  paginator = Paginator(qs, perpage)
  page = paginator.page(page_num)
  pagination = Pagination(request, page)

  return pagination

class Pagination(object):
  
  def __init__(self, request, page):
    self.request = request
    self.page = page

  def _make_link(self, text, klass, **kwargs):
    qs = {}
    for k in self.request.GET:
      qs[k] = self.request.GET[k]
    qs.update(kwargs)
    url = "%s?%s" % (self.request.path_info, urllib.urlencode(qs))

    return u'<span class="%s"><a href="%s">%s</a></span>' % (" ".join(klass), url, text)

  def _iter_render(self):
    paginator = self.page.paginator
    yield u"<span>%s筆記錄</span>" % "{:,}".format(paginator.count)
    yield u"<span>共%s頁</span>" % paginator.num_pages

    if self.page.number > 1:
      yield self._make_link(u"第1頁", [], page=1)

    prev_page_number = 1
    klass = []
    if self.page.has_previous():
      prev_page_number = self.page.previous_page_number()
    else:
      klass.append("disabled")

    yield self._make_link(u"上一頁", klass, page=prev_page_number)

    p_start = self.page.number - 5
    if p_start < 1:
      p_start = 1

    p_end = p_start + 9 
    if p_end > self.page.paginator.num_pages:
      p_end = self.page.paginator.num_pages

    for p in range(p_start, p_end+1):
      klass = []
      if p == self.page.number:
        klass.append("current")
      yield self._make_link(p, klass, page=p)

    
    next_page_number = 1
    klass = []
    if self.page.has_next():
      next_page_number = self.page.next_page_number()
    else:
      klass.append("disabled")

    yield self._make_link(u"下一頁", klass, page=next_page_number)

    yield self._make_link(u"最後頁", [], page=paginator.num_pages)


  def render(self):
    
    output = []
    for x in self._iter_render():
      output.append(x)

    return mark_safe(u"".join(output))
