from CustomArt import CustomArt

font = {
    'm': '1',
    'e':'2',
    's':'3'
}
art = CustomArt('hp')

art.justify = 'right'
art.create()
print(art)

art.justify = 'center'
art.create()
print(art)


art.justify = 'left'
art.create()
print(art)
