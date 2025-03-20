from django.shortcuts import render


class Car:
    def __init__(self, name, disc, photo):
        self.name = name
        self.disc = disc
        self.photo = photo


a = Car('Toyota Camry', 'Комфортный седан бизнес-класса с надежным двигателем, отличной шумоизоляцией и современными технологиями. Идеален для города и трассы.', f"https://tflcar.com/wp-content/uploads/2017/12/2018_Toyota_Camry_XLE_Hybrid_24_FF81643D84BB8725A24A887F95C671C5CD1D057C.jpg")
b = Car('Toyota RAV4', 'Популярный кроссовер с экономичным расходом топлива, высоким клиренсом и просторным салоном. Отличный выбор для семейных поездок.', f"https://cdn.automobile-propre.com/uploads/2023/05/Toyota-RAV4-Trail-2023-1.jpg")
c = Car('Honda Civic', 'Стильный и динамичный седан с отличной управляемостью, экономичным двигателем и технологичным интерьером. Подходит для молодежи и любителей драйва.', f"https://www.worthytoshare.com/wp-content/uploads/2018/12/Honda-Civic.png")
d = Car('Honda CR-V', 'Надежный кроссовер с вместительным багажником, комфортной подвеской и передовыми системами безопасности. Отличный вариант для путешествий.', f"https://images.hgmsites.net/hug/honda-cr-v_100755452_h.jpg")
e = Car('Renault Duster', 'Бюджетный, но проходимый кроссовер с хорошей подвеской, высоким клиренсом и надежным мотором. Подходит для бездорожья.', f"https://quatrorodas.abril.com.br/wp-content/uploads/2020/02/renault-duster-iconic-1.6-cvt-2021-2-1-e1583247536423.jpg?quality=70&strip=info")
f = Car('Renault Megane', 'Элегантный хэтчбек с экономичным дизельным двигателем, стильным дизайном и комфортным салоном. Идеален для города и трассы.', f"https://www.motoringresearch.com/wp-content/uploads/2015/12/01_Megane.jpg")
cars_info = [a, b, c, d, e, f]


def index(request):
    context = {
        'title': 'Cars',

    }
    return render(request, 'cars/index.html', context)


def toyota(request):
    context = {
        'title': 'Toyota',
        'cars_info': cars_info,
    }
    return render(request, 'cars/toyota.html', context)


def honda(request):
    context = {
        'title': 'Honda',
        'cars_info': cars_info,
    }
    return render(request, 'cars/honda.html', context)


def renault(request):
    context = {
        'title': 'Renault',
        'cars_info': cars_info,
    }
    return render(request, 'cars/renault.html', context)
