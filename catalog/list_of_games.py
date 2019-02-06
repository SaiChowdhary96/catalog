#!/usr/bin/env python3

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from database_setup import GameType, PCGames, Base, User

engine = create_engine('sqlite:///pcgames.db')
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
session = DBSession()

# Insert Dummy values in database

# Insert dummy user
user = User(name="Sai Rapz", email="sairapz15@gmail.com",
            picture='https://o.aolcdn.com/images/dims3/GLOB/legacy_thumbnail'
            '/1200x630/format/jpg/quality/85/http%3A%2F%2Fi.huffpost.com%2F'
            'gen%2F5334782%2Fimages%2Fn-TWIN-BABY-628x314.jpg')
session.add(user)
session.commit()

# Insert dummy game type
game_type = GameType(name="Open World", user_id=1, user=user)

# Insert dummy game
PCGame = PCGames(name='GTA V',
                 description='Los Santos: a sprawling sun-soaked metropolis'
                 ' all of self-help gurus, starlets and fading celebrities,'
                 ' once the envy of the Western world, now struggling to stay'
                 ' afloat in an era of economic uncertainty and cheap reality'
                 ' TV. GTA 5 story. Amidst the turmoil, three very different'
                 ' criminals plot.',
                 image='https://www.onmsft.com/wp-content/uploads/2015/'
                 '09/GTAV.jpg',
                 release_date='17 September 2013', company='Rockstar Games',
                 game_type_id=1,
                 game_type=game_type,
                 user_id=1, user=user)

session.add(game_type)
session.add(PCGame)
session.commit()

PCGame = PCGames(name='Watch Dogs',
                 description='In October 2012, hacker Aiden Pearce and his'
                 ' mentor and partner, Damien Brenks, conduct an electronic'
                 ' bank heist at the high-end Merlaut Hotel in Chicago and'
                 ' trigger a silent alarm set by another hacker. Brenks tries'
                 ' to find the hacker, giving himself and Pearce away.',
                 image='http://paperlief.com/images/watch-dogs-wallpaper'
                 '-ipad-wallpaper-3.jpg',
                 release_date='27 May 2014',
                 company='Ubisoft', game_type_id=1, game_type=game_type,
                 user_id=1,
                 user=user)

session.add(PCGame)
session.commit()

game_type = GameType(name="Shooting", user_id=1, user=user)

PCGame = PCGames(name='Call of Duty: Black Ops 4',
                 description="In the year 2043, during a covert mission"
                 " involving a mercenary group, Jessica Mason-Green (Alexa"
                 " Kahn), a US Army Specialist is presumably killed while her"
                 "two squad mates, Donnie 'Ruin' Walsh (Christian Rummel) and"
                 " Erin 'Battery' Baker (Morla Gorrondona) escape with"
                 " critical injuries. Two years later, Savannah Mason-Meyer"
                 "(Evangeline Lilly), a trillionaire researcher and Jessica's"
                 " sister, recruits ten of the world's most elite soldiers,"
                 " including Ruin and Battery, for a top-secret project"
                 " against an unknown threat. Savannah uses a Combat"
                 " Immersion program to train the Specialists in a virtual"
                 " simulation, with Sergeant Frank Woods (James C. Burns)"
                 " acting as their instructor.",
                 image='https://www.thenerdmag.com/wp-content/uploads/2018/'
                 '10/Call-of-Duty-Black-Ops-4.jpg',
                 release_date='12 October 2018',
                 company='Activision', game_type_id=2, game_type=game_type,
                 user_id=1, user=user)

session.add(game_type)
session.add(PCGame)
session.commit()
