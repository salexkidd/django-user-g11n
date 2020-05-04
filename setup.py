from setuptools import setup

long_description = """Allows Django users to set g11n(language, timezone).

Provides an indication of the translation and time that will be displayed to the user at the set value.
"""


setup(
    name='django-user-g11n',
    author="salexkidd",
    author_email="salexkidd@gmail.com",
    url="https://github.com/salexkidd/django-user-g11n",
    description='User g11n extension for Django',
    long_description=long_description,
    keywords=["django", "i18n", "l10n", "g11n", "timezone", ],
    version='0.1',
    packages=['user_g11n'],
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
    ],
)
