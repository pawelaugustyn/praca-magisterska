from locust import HttpUser, task, between

class Tester(HttpUser):
    @task
    def get_time(self):
        self.client.get("sort")

    wait_time = between(1, 2)