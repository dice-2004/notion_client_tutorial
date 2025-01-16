from notion_client import Client

class Notion:
    def __init__(self, token):
        self.client = Client(auth=token)

    def fetch_database(self, database_id):
        response = self.client.databases.query(
            **{
                "database_id": database_id,
            }
        )
        return response

    def fetch_page_content(self, page_id):
        data = self.client.blocks.children.list(
            **{
                "block_id": page_id,
                "page_size": 50
            }
        )
        return data

    
