from django.test import SimpleTestCase
from django.urls import reverse, resolve
from budget.views import project_list, project_detail, ProjectCreateView


class TestUrls(SimpleTestCase):

    def test_list_url_is_resolves(self):
        # assert 1 == 2 #esitlik sagliyor
        url = reverse('list')
        print(resolve(url))
        self.assertEqual(resolve(url).func, project_list)
        # ikisi esit mi ona bakiyor

    def test_project_add_url_is_resolves(self):
        # assert 1 == 2 #esitlik sagliyor
        url = reverse('add')
        print(resolve(url))
        self.assertEqual(resolve(url).func.view_class, ProjectCreateView)
        # ikisi esit mi ona bakiyor .view.class yaparsan class view yapiyor function yerine

    def test_detail_url_is_resolves(self):
        # assert 1 == 2 #esitlik sagliyor
        url = reverse('detail',args=['some-slug'])
        print(resolve(url))
        self.assertEqual(resolve(url).func, project_detail)
        # ikisi esit mi ona bakiyor .view.class yaparsan class view yapiyor function yerine

