from app import app
import unittest
import json

class TestEndpoints(unittest.TestCase):
    def setUp(self):
        self.client = app.test_client(self)
        self.pdt =  {
                'id': 3,
                'name': "Iphone6",
                'quantity': 24,
                'ammount': 1200000,
                'image': "iphone.jpeg"
            }

        self.sale = {
            'id': 2,
            'product_name': "Iphone6",
            'quantity': 1,
            'ammount': 1200000,
            'sold_by': "Peter Mulindwa"
        }

    def test_create_product(self):
        res = self.client.post(
            '/store_manager/api/v1/admin/products',
            data=json.dumps(self.pdt),
            content_type='application/json'
        )
        self.assertTrue(res.status_code, 201)

    def test_create_sale(self):
        res = self.client.post(
           '/store_manager/api/v1/user/sales',
            data=json.dumps(self.sale),
            content_type='application/json' 
        )
        self.assertTrue(res.status_code, 201)

    def test_get_all_products(self):
        res = self.client.get(
            '/store_manager/api/v1/user/products'
        )
        self.assertTrue(res.status_code, 200)

    def test_get_all_sales(self):
        res = self.client.get(
            '/store_manager/api/v1/admin/sales'
        )
        self.assertEqual(res.status_code, 200)

if __name__ == '__main__':
    unittest.main()

    