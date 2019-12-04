"""函数返回值8.3"""


def main():
    def city_country(name, city):
        str = '"' + name + ", " + city + '"'
        return str

    def make_album(singer, album_name, song_num=0):
        music_album = {
                        'singer': singer,
                        'album_name': album_name,
                        }
        if song_num:
            music_album['song_cnt'] = song_num
        return music_album
    print(city_country('Paris', 'France'))
    print(make_album('HANG', 'company', 12))
    while True:
        print("if you want to go out, input q.")
        singer = input("singer of this album:")
        if singer == 'q':
            break
        name = input("the name of this album:")
        if name == 'q':
            break
        print(make_album(singer, name))

    pass


if __name__ == '__main__':
    main()