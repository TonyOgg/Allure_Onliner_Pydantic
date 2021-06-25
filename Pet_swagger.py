from pydantic import BaseModel
import requests

address = 'https://petstore.swagger.io/v2/pet'

petty = """{
  "id": 0,
  "category": {
    "id": 0,
    "name": "string"
  },
  "name": "doggie",
  "photoUrls": [
    "string"
  ],
  "tags": [
    {
      "id": 0,
      "name": "string"
    }
  ],
  "status": "available"
}"""

class Categoies_fields(BaseModel):
    id: int
    name: str


class Tags_fields(BaseModel):
    id: int
    name: str


class Pets(BaseModel):
    id: int
    category: dict[Categoies_fields]
    name: str
    photoUrls: list[str]
    tags: dict[Tags_fields]
    status: str


pet = Pets.parse_raw(petty)
print(pet)

pet_1 = Pets(222333,
    {
    16,
    "Cat"
  },
  "Oudrey",
  [
    'https://cs9.pikabu.ru/post_img/2017/05/12/8/1494592816133830021.jpg'
  ],
  [
    {
      15,
      "Catty"
    }
  ],
  "available"
)

pet_1_new = Pets(222333,
    {
    16,
    "Kittens"
  },
  "doggie",
  [
    'https://cs9.pikabu.ru/post_img/2017/05/12/8/1494592816133830021.jpg'
  ],
  [
    {
      15,
      "Catty"
    }
  ],
  "available"
)

def test_creating_pet():
    response = requests.post(address, json=pet_1.json())
    assert response.status_code == 200

def test_is_pet_in():
    response = requests.post(address + f'/%{}'.format(pet_1.id))
    assert response.status_code == 200

def test_updating_pet():
    response = requests.put(address, json=pet_1_new.json())
    assert response.status_code == 200

def test_delete_pet():
    response = requests.post(address + f'/%{}'.format(pet_1.id))
    assert response.status_code == 200
