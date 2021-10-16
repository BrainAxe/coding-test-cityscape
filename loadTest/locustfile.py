from locust import HttpUser, task, between


class RoomBooking(HttpUser):
    wait_time = between(1,5)

    @task
    def booking_tests(self):
        self.client.post("/api/v1/book-room/", {
          "booking_date":"2021-10-21",
          "first_name":"Tanzim",
          "last_name":"Rizwan",
          "email":"tanzim@mail.com"
        })
