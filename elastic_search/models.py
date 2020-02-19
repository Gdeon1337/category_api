# from elasticsearch_dsl import connections, Document, Text, Nested, InnerDoc, Double, Object
#
#
# class Attribute(InnerDoc):
#     title = Text(required=True)
#
#
# class AttributeValue(InnerDoc):
#     attribute = Object(Attribute)
#     value = Text(required=True)
#     value_type = Text(required=True)
#
#
# class Product(Document):
#     title = Text(required=True)
#     price = Double()
#     product_attributes = Nested(AttributeValue)
#
#     class Index:
#         name = 'products'
#
#
# class Category(Document):
#     title = Text(required=True)
#     products = Nested(Product)
#
#     class Index:
#         name = 'categories'
#         settings = {
#             "number_of_shards": 2,
#         }
#
#
# connections.create_connection(hosts=[{'host': 'localhost', 'port': 9201}])
# Category.init()
# # a = Category.get('LeCKGXABIOy04vP2y8NL')
# # a.products.append(Product(title='Product', price=1234.2))
# b = Product(title='Product_1', price=1234.1)
# b.save()
# print(b.meta.id)
# # a.save()
