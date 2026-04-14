from django.test import TestCase
from lists.models import Item, List


class ItemModelTest(TestCase):

    def test_cannot_save_empty_list_items(self):
        list_ = List.objects.create()

        item = Item(list=list_, text='')

        with self.assertRaises(Exception):
            item.save()


class HomePageTest(TestCase):

    def test_invalid_input_nothing_saved(self):
        self.client.post('/', data={'item_text': ''})
        self.assertEqual(Item.objects.count(), 0)

    def test_invalid_input_renders_home_template(self):
        response = self.client.post('/', data={'item_text': ''})
        self.assertTemplateUsed(response, 'home.html')

    def test_invalid_input_shows_error(self):
        response = self.client.post('/', data={'item_text': ''})
        self.assertContains(response, "Você não pode enviar um item vazio")