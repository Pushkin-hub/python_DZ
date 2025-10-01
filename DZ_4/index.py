import requests
from bs4 import BeautifulSoup
import json

# URL каталога сайтов
catalog_url = "https://q-parser.ru/catalog"


def get_catalog_links():
    response = requests.get(catalog_url)
    soup = BeautifulSoup(response.text, 'html.parser')
    # Предположим, что ссылки на сайты в каталоге расположены в определённых элементах.
    # Необходимо адаптировать в зависимости от структуры сайта.
    links = {}
    for a in soup.find_all('a', href=True):
        title = a.get_text(strip=True)
        href = a['href']
        if href.startswith('http'):
            links[title] = href
    return links


def select_site(sites):
    print("Доступные сайты для парсинга:")
    for i, site in enumerate(sites.keys(), 1):
        print(f"{i}. {site}")
    choice = int(input("Введите номер сайта для парсинга: "))
    selected_site = list(sites.items())[choice - 1]
    return selected_site


def get_category_links(site_url):
    response = requests.get(site_url)
    soup = BeautifulSoup(response.text, 'html.parser')
    # Аналогично, ищем категории; структура зависит от сайта.
    categories = {}
    # Предположим, что категории в списках или меню
    for a in soup.find_all('a', href=True):
        title = a.get_text(strip=True)
        href = a['href']
        # фильтруем по логике
        if 'category' in href:
            categories[title] = href
    return categories


def parse_category(category_url):
    response = requests.get(category_url)
    soup = BeautifulSoup(response.text, 'html.parser')
    # Предположим, что позиции расположены в карточках или списках
    items = []
    for item_div in soup.find_all('div', class_='product-item'):
        name = item_div.find('h2').get_text(strip=True)
        features = item_div.find('ul')
        features_list = [li.get_text(strip=True) for li in features.find_all('li')]
        item = {
            'name': name,
            'features': features_list
        }
        items.append(item)
    return items


def save_to_json(data, filename='result.json'):
    with open(filename, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=4)


def main():
    sites = get_catalog_links()
    site_name, site_url = select_site(sites)
    print(f"Выбран сайт: {site_name}")
    categories = get_category_links(site_url)
    print("Доступные рубрики:")
    for i, cat in enumerate(categories.keys(), 1):
        print(f"{i}. {cat}")
    category_choice = int(input("Введите номер рубрики для парсинга: "))
    category_name = list(categories.keys())[category_choice - 1]
    category_url = categories[category_name]
    print(f"Парсинг рубрики: {category_name}")
    
    items = parse_category(category_url)
    save_to_json(items, f"{category_name}.json")
    print("Позиции:")

    for item in items:
        print(f"{item['name']}: {', '.join(item['features'])}")

    # Дополнительно: поиск по названию
    search_name = input("Введите название позиции для поиска (или оставьте пустым): ").strip()
    if search_name:
        for item in items:
            if search_name.lower() in item['name'].lower():
                print(f"Найдено: {item['name']}")
                print(f"Характеристики: {', '.join(item['features'])}")
                break
        else:
            print("Позиция не найдена.")

if __name__ == "__main__":
    main()