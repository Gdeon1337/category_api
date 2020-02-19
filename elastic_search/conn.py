# from elasticsearch import Elasticsearch
# # from .models import create_index
# from uuid import uuid4
#
#
# class ElasticConn:
#     conn = None
#
#     def __init__(self):
#         self.conn = Elasticsearch([{'host': 'localhost', 'port': 9201}])
#         if self.conn.ping():
#             print('Yay Connected')
#             # create_index(self.conn)
#         else:
#             print('Awww it could not connect!')
#
#     def create(self, index: str, data: dict):
#         return self.conn.create(index=index, body=data, id=uuid4())
#
#     def delete(self, index: str, _id: str):
#         return self.conn.delete(index=index, id=_id)
#
#     def update(self, index, _id, data):
#         return self.conn.update(index=index, body=data, id=_id)
#
#     def search(self, index, body):
#         return self.conn.search(index=index, body=body)
#
#
