from random import randint
from re import sub
from aes import ecb
from util import randBytes

key = randBytes(16)


def profile_for(email, role='user'):
    email = sub('[\&\=]', '', email)
    profile = {'email': email,
               'uid': str(randint(1, 1000)),
               'role': role}
    return profile


def parser(encoded):
    splitted = encoded.split('&')
    kwargs = {i.split('=')[0]: i.split('=')[1] for i in splitted}
    return kwargs


def serialize(profile):
    encoded = 'email={}&uid={}&role={}'.format(profile['email'],
                                               profile['uid'],
                                               profile['role'])
    return encoded


def encrypt(profile):
    cipher = ecb(key)
    return cipher.encrypt(bytes(profile, 'utf-8'))


def decrypt(ciphertext):
    cipher = ecb(key)
    return cipher.decrypt(ciphertext)


def query(email):
    user = profile_for(email)
    ciphertext = encrypt(serialize(user))
    return ciphertext


def get_profile(ciphertext):
    serialized = decrypt(ciphertext)
    kwargs = parser(str(serialized))
    return kwargs['role']


if __name__ == '__main__':
    cookie = query('john@doeeeeeeeeeeee.com')
    print(cookie)
    profile = get_profile(cookie)
    print(profile)
