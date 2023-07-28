from app import db
from models import Pet

db.drop_all()
db.create_all()

CAT_PHOTO = 'https://en.wikipedia.org/wiki/Cat#/media/File:Orange_tabby_cat_sitting_on_fallen_leaves-Hisashi-01A.jpg'
DOG_PHOTO = 'https://upload.wikimedia.org/wikipedia/commons/9/99/Brooks_Chase_Ranger_of_Jolly_Dogs_Jack_Russell.jpg'

pet1 = Pet(name="pet1",
        species="pet1_species",
        photo_url= CAT_PHOTO,
        age="baby",
        notes="test1_notes",
        available=True)

pet2 = Pet(name="pet2",
        species="pet2_species",
        photo_url= DOG_PHOTO,
        age="adult",
        notes="test2_notes",
        available=False)

db.session.add(pet1)
db.session.add(pet2)

db.session.commit()