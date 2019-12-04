"""测试函数"""


def get_city_country(city_name, country_name, population=0):
    if population:
        return city_name.title() + ', ' + country_name.title() + " - population " + str(population)
    else:
        return city_name.title() + ', ' + country_name.title()

