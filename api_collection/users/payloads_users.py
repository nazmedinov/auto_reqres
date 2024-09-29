class Payloads:

    @staticmethod
    def create_user_payload(name, job):
        return {"name": name, "job": job}

    @staticmethod
    def edit_exist_user(name, job):
        return {"name": name, "job": job}
