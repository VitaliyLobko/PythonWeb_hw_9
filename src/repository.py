from sqlalchemy import and_, or_
from src.db import session
from src.models import User, Person, Notice
from sqlalchemy.orm import joinedload

def get_user(login) -> User:
    user = session.query(User).filter(User.login == login).one()
    return user


def create_contact(fullname, email, phone):
    person = Person(fullname=fullname, email=email, cell_phone=phone)
    session.add(person)
    session.commit()
    session.close()


def update_contact(_id, fullname, email, phone):
    person = session.query(Person).filter(Person.id == _id)
    person.update({'fullname': fullname, 'email': email, 'cell_phone': phone})
    session.commit()
    session.close()
    return person.one()


def get_all_contacts():
    persons = session.query(Person).all()
    return persons


def search_contacts(fullname):
    p = session.query(Person).filter(Person.fullname == fullname).one()
    return p


def remove_contact(_id) -> int:
    r = session.query(Person).filter(Person.id == _id).delete()
    session.commit()
    session.close()
    return r


def add_notice(_id, description):
    person = session.query(Person).filter(Person.id == _id).one()
    notice = Notice(
        text=description,
        person_id=person.id,
        tags='test'
    )
    session.add(notice)
    session.commit()
    session.close()


def remove_notice(_id) -> int:
    r = session.query(Notice).filter(Notice.id == _id).delete()
    session.commit()
    session.close()
    return r


def list_notice(_id):
    notices =session.query(Notice).options(joinedload('person')).filter(Notice.person_id == _id).all()
    return notices