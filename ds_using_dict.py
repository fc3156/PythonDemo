ab = {
    'Swaroop': 'swaroop@swaroop.com',
    'Larry': 'larry@wall.com',
    'Matsumoto': 'matz@lang.org',
    'Spammer': 'spammer@hotmail.com'
}
print('Swaroops address is ', ab['Swaroop'])

del ab['Spammer']

print('\nThree are {} contacts in the address-book\n'.format(len(ab)))

for name, address in ab.items():
    print('Contact {} at {}'.format(name, address))

ab['Guido'] = 'guido@python.com'

if 'Guido' in ab:
    print("\nGuido address is ", ab['Guido'])
