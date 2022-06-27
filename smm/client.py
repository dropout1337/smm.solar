import requests, typing

class SMM():
    
    def __init__(self, apikey: str, base_url: str = "https://smm.solar/api/v2"):
        self.apikey = apikey
        self.base_url = base_url
        
        self.session = requests.Session()

    def get_services(self):
        data = {
            "key": self.apikey,
            "action": "services"
        }
        response = self.session.post(self.base_url, data=data)
        if response.status_code == 200:
            return response.json()
        else:
            raise Exception(response.text)
        
    def create_order(self, service: int, link: str, quantity: int):
        data = {
            "key": self.apikey,
            "action": "add",
            "service": service,
            "link": link,
            "quantity": quantity
        }
        response = self.session.post(self.base_url, data=data)
        if response.status_code == 200:
            return response.json()
        else:
            raise Exception(response.text)
    
    def order_status(self, orders: typing.Union[list, int]):
        data = {
            "key": self.apikey,
            "action": "status"
        }
        if type(orders) == int:
            data["order"] = orders
        else:
            data["orders"] = orders
        response = self.session.post(self.base_url, data=data)
        if response.status_code == 200:
            return response.json()
        else:
            raise Exception(response.text)
    
    def get_balance(self):
        data = {
            "key": self.apikey,
            "action": "balance"
        }
        response = self.session.post(self.base_url, data=data)
        if response.status_code == 200:
            return response.json()
        else:
            raise Exception(response.text)