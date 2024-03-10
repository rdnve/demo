from django.conf import settings

DATA_ABOUT = {
    "me": {
        "full_name": settings.ME_FULL_NAME,
        "phone_number": settings.ME_PHONE_NUMBER,
        "email": settings.ME_EMAIL,
        "description": "дизайн, это наше все",
        "picture": "https://gravatar.com/avatar/00110b9f7111bf4b2ab22369d78a40ea?s=400&d=robohash&r=x",
    },
    "faculty": {
        "name": "Дизайн",
        "description": "Красота спасёт мир",
        "lead": {
            "full_name": settings.LEAD_FULL_NAME,
            "email": settings.LEAD_EMAIL,
            "phone_number": "+78001232323",
            "picture": settings.LEAD_PICTURE,
            "staff": settings.LEAD_STAFF,
        },
        "manager": {
            "full_name": settings.MANAGER_FULL_NAME,
            "email": settings.MANAGER_EMAIL,
            "phone_number": "+79008887766",
            "picture": settings.MANAGER_PICTURE,
            "staff": settings.MANAGER_STAFF,
        },
    },
    "friends": [
        {
            "full_name": "Иванов Иван Иванович",
            "phone_number": "+7123456789",
            "email": "ivanov@edu.hse.ru",
            "picture": "https://gravatar.com/avatar/00110b9f7111bf4b2ab22369d78a40ea?s=400&d=monsterid&r=x",
        },
        {
            "full_name": "Анна Карелян Ванивновна",
            "phone_number": "+78001002043",
            "email": "annapi@edu.hse.ru",
            "picture": "https://gravatar.com/avatar/acb002c62d9b2326d7edae95673f5c9d?s=400&d=robohash&r=x",
        },
        {
            "full_name": "Анастасия Пупкина Михайловна",
            "phone_number": "+79011002030",
            "email": "pupkina@edu.hse.ru",
            "picture": "https://gravatar.com/avatar/6076e19e79276cc86e1d91d3eba9e06f?s=400&d=robohash&r=x",
        },
    ],
}
