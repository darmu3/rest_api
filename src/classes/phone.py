class Phone:
    def __init__(self, id_phone, name_phone, os_phone):
        self.id_phone = id_phone
        self.name_phone = name_phone
        self.os_phone = os_phone

    def to_dict(self):
        """Преобразует объект Phone в словарь для передачи в запросы."""
        return {
            'name_phone': self.name_phone,
            'os_phone': self.os_phone
        }

    def __str__(self):
        return f"ID: {self.id_phone}, Название: {self.name_phone}, ОС: {self.os_phone}"