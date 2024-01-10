from unittest.mock import patch

from django.shortcuts import reverse
from rest_framework import test

from recipes.tests.test_recipe_base import RecipeMixin


class RecipeAPIv2Test(test.APITestCase, RecipeMixin):
    def test_recipe_api_list_returns_status_code_200(self):
        api_url = reverse('recipes:recipes-api-list')
        response = self.client.get(api_url)
        self.assertEqual(
            response.status_code,
            200
        )

    @patch('recipes.views.api.RecipeAPIv2Pagination.page_size', new=7)
    def test_recipe_api_list_loads_correct_number_of_recipes(self):
        recipes_wanted_number = 7
        self.make_recipe_in_batch(qtd=recipes_wanted_number)

        response = self.client.get(
            reverse('recipes:recipes-api-list') + '?page=1'
        )
        recipes_loaded_quantity = len(response.data.get('results'))

        self.assertEqual(
            recipes_wanted_number,
            recipes_loaded_quantity
        )
