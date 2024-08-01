from notification.gateway.interface import IGateway


class Gateway(IGateway):
    def send(self, user_id: str, message: str):
        print(f"Sending message to {user_id}: {message}")
