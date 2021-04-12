///Нет, ну это вообще оказалосъ без шансов... толъко копипейститъ и редактироватъ чужой код..))) ///
goods = []
features = {'Name': '', 'Price': '', 'Qty': '', 'Measurement Unit': ''}
analytics = {'Name': [], 'Price': [], 'Qty': [], 'Measurement Unit': []}
num = 0

while True:
    if input('Press Enter to start the application or type Q to leave: ').upper() == 'Q':
        break
    num += 1
    for f in features.keys():
        prop = input(f'Enter the following value: {f} - ')
        features[f] = int(prop) if (f == 'Price' or f == 'Qty') else prop
        analytics[f].append(features[f])
    goods.append((num, features.copy()))
    # print(f"\nGoods structure\n{goods}")
    print(f"\nCurrent goods analytics:\n{'~' * 70}")
    for key, value in analytics.items():
        print(f"{key[:25]:>30}: {value}")
    print('~' * 70)


# a = 'qqqqqqqqs;aldfaksdfdkljfdks;affjd;jas;klfasfakldsfjs;lkfadlkfjadkls;fja;sldkfjal;sfja;lksdfjas;kldfjkl;sdfj' \
#     ';laskdfalxfsjfdjfkjkfjdkfjdf dkjfkdjfdkkfjdkfj kdjfkdfjdkjffdkj dfkdjfkdjfkdjf kdjfkdjfkdjkfjkdjkfjkfjdjfk' \
#     'kdlfkldfkldkdlkfdlfkdkfdkflfkdl'


