from datetime import date

from Lesson2.src import db, app
from Lesson2.src.models import Film, Actor


def populate_films():
    harry_potter_and_ph_stone = Film(
        title='Harry Potter and the Philosopher\'s Stone',
        release_date=date(2001, 11, 4),
        description='An orgphaned boy enrolls...',
        distributed_by='Warner Bros. Pictures',
        length=152,
        rating=7.6,
    )
    harry_potter_and_ch_s = Film(
        title='Harry Potter and Chamber of Secrets',
        release_date=date(2002, 11, 3),
        description='An ancient prophecy...',
        distributed_by='Warner Bros. Pictures',
        length=161,
        rating=7.4,
    )
    harry_potter_and_priz_az = Film(
        title='Harry Potter and the Prizoner of Azkaban',
        release_date=date(2005, 11, 6),
        description='Harry Potter finds himself...',
        distributed_by='Warner Bros. Pictures',
        length=157,
        rating=7.7,
    )
    harry_potter_and_order_phoenix = Film(
        title='Harry Potter and the Order of he Phoenix',
        release_date=date(2007, 7, 19),
        description='With their warning about...',
        distributed_by='Warner Bros. Pictures',
        length=138,
        rating=7.5,
    )

    daniel_readcliffe = Actor(name='Daniel Readcliff', birthday=date(1989, 7, 23), is_active=True)
    emma_watson = Actor(name='Emma Watson', birthday=date(1990, 4, 15), is_active=True)
    alan_rickman = Actor(name='Alan Rickman', birthday=date(1946, 2, 21), is_active=False)

    with app.app_context():
        db.session.add(harry_potter_and_ph_stone)
        db.session.add(harry_potter_and_ch_s)
        db.session.add(harry_potter_and_priz_az)
        db.session.add(harry_potter_and_order_phoenix)

        db.session.add(daniel_readcliffe)
        db.session.add(emma_watson)
        db.session.add(alan_rickman)

        db.session.commit()
        db.session.close()


if __name__ == '__main__':
    print('Population db...')
    populate_films()
    print('Successfuly populated!')