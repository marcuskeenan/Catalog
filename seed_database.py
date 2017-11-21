from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from database_setup import Base, Category, Item, User

engine = create_engine('sqlite:///catalog.db')
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
session = DBSession()

categories = [

    
    ['Tubas',
        [{'name': 'Meinl Weston 6450 Baer Handmade Series 5-Valve  CC Tuba',
          'description': 'The Meinl Weston 6450/2 Baer Handmade Series 5-Valve 6/4 CC Tuba was developed together with Alan Baer, tubist with the New York Philharmonic Orchestra.',
          'picture':'https://www.philparker.biz/media/catalog/product/cache/1/image/9df78eab33525d08d6e5fb8d27136e95/b/a/baer_product_image.png',
          'price': '31,977.00',
          'type': 'New'
          },
          {'name': 'Meinl Weston 6460 Kodiak Series 6-Valve  F Tuba',
          'description': 'The Kodiak F Tuba is the newest addition to the Meinl Weston line. Developed in cooperation with Alan Baer, principal tuba of the New York Philharmonic, this F tuba offers the player great color of sound with amazing intonation and fantastic dynamic contrasts.',
          'picture':'https://media.wwbw.com/is/image/MMGS7/6460-Kodiak-Series-6-Valve-6-4-F-Tuba-6460S-Silver/464682000232000-00-220x220.jpg',
          'price': '16,714.00',
          'type': 'Used'
          },
          {'name': 'B&S 3198 Series 5-Valve 5/4 CC Tuba',
          'description': 'The B&S 3198 is a 5-valve (4 piston and 1 rotary) CC-Tuba in 5/4 size. It has a .748"-0.827" bore and an 18.898"bell. It is constructed of yellow brass and features a clear lacquered finish.',
          'picture':'http://www.bamusikk.no/images/4198pt7p_large.jpg',
          'price': '13,586.00',
          'type': 'Used'
          }
        ]
    ],
    ['Bass Trombones',
        [{'name': 'Getzen 1062FD Eterna Series Bass Trombone',
          'description': 'Getzen Bass Trombones 1062FD This dual bore .562".578" bass trombone is totally responsive to the players musical interpretation. From the dark round sound to bright and brassy, it gives the player whatever is needed. The instrument plays very freely through the open wrap valve section with very little difference in resistance from the open horn.',
          'picture':'https://media.wwbw.com/is/image/MMGS7/1062FD-Eterna-Series-Bass-Trombone-1062FDR-Lacquer-Red-Brass-Bell/464533000924000-00-220x220.jpg',
          'price': '3,569.00',
          'type': 'New'
          },
          {'name': 'Getzen 1062FD Eterna Series Bass Trombone',
          'description': 'Getzen Bass Trombones 1062FD This dual bore .562".578" bass trombone is totally responsive to the players musical interpretation. From the dark round sound to bright and brassy, it gives the player whatever is needed. The instrument plays very freely through the open wrap valve section with very little difference in resistance from the open horn.',
          'picture':'https://media.wwbw.com/is/image/MMGS7/1062FD-Eterna-Series-Bass-Trombone-1062FDR-Lacquer-Red-Brass-Bell/464533000924000-00-220x220.jpg',
          'price': '3,569.00',
          'type': 'Used'
          }
        ]
    ]
    
]


current_user = User(name="Marcus Keenan", email="marcusekeenan@gmail.com",
             picture='https://pbs.twimg.com/profile_images/2671170543/18debd694829ed78203a5a36dd364160_400x400.png')
session.add(current_user)
session.commit()


for category in categories:
    current_category = Category(name=category[0], user=current_user)
    session.add(current_category)
    session.commit()

    for item in category[1]:
        current_item = Item(name=item['name'],
                            description=item['description'],
                            picture=item['picture'],
                            price=item['price'],
                            type=item['type'],
                            category=current_category,
                            user=current_user)
        session.add(current_item)
        session.commit()

print "Database seeding complete!"
