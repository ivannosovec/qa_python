import pytest


class TestBooksCollector:

   # Тест 1: Проверка инициализации и базовых методов коллектора
def test_init_and_basic_methods(self):
    """Проверяем что коллектор инициализируется и базовые методы работают"""
    collector = BooksCollector()
    
    # Проверяем через методы, а не через атрибуты
    assert collector.get_books_genre() == {}  # через метод get_books_genre()
    assert collector.get_list_of_favorites_books() == []  # через метод get_list_of_favorites_books()
    
    # Проверяем что можем добавить книгу
    collector.add_new_book('Тестовая книга')
    assert len(collector.get_books_genre()) == 1  # через метод
    
    # Проверяем что можем добавить в избранное
    collector.add_book_in_favorites('Тестовая книга')
    assert len(collector.get_list_of_favorites_books()) == 1  # через метод
        assert collector.genre == ['Фантастика', 'Ужасы', 'Детективы', 'Мультфильмы', 'Комедии']
        assert collector.genre_age_rating == ['Ужасы', 'Детективы']

    # Тест 2: Параметризованный тест для добавления новой книги
    @pytest.mark.parametrize('valid_book_name', [
    'Война и мир',           # валидное название
    'A' * 40,                # граничное значение (40 символов)
    'Книга',                 # обычное название
    '1984',                  # название с цифрами
    'Book Name',             # название с пробелом
    'Книга с запятой, и точкой.',  # название со знаками препинания
])
def test_add_new_book_success(self, valid_book_name):
    """Проверяем успешное добавление книги с валидными названиями"""
    collector = BooksCollector()
    collector.add_new_book(valid_book_name)
    
    # Проверяем что книга добавилась
    assert valid_book_name in collector.get_books_genre()
    # Проверяем что жанр не установлен (пустая строка)
    assert collector.get_book_genre(valid_book_name) == ''


# Тест 2.2: Неуспешное добавление книги (невалидные данные)
@pytest.mark.parametrize('invalid_book_name', [
    '',                      # пустая строка
    'A' * 41,                # слишком длинное название (41 символ)
    '   ',                   # только пробелы
    '\n',                    # только перенос строки
    '\t',                    # только табуляция
])
def test_add_new_book_failure(self, invalid_book_name):
    """Проверяем что книга с невалидным названием не добавляется"""
    collector = BooksCollector()
    collector.add_new_book(invalid_book_name)
    
    # Проверяем что книга НЕ добавилась
    assert invalid_book_name not in collector.get_books_genre()
    # Проверяем что коллекция осталась пустой
    assert len(collector.get_books_genre()) == 0


# Тест 2.3: Добавление дубликата книги
def test_add_new_book_duplicate(self):
    """Проверяем что книгу нельзя добавить дважды"""
    collector = BooksCollector()
    book_name = 'Дубликат'
    
    # Первое добавление
    collector.add_new_book(book_name)
    assert book_name in collector.get_books_genre()
    assert len(collector.get_books_genre()) == 1
    
    # Второе добавление той же книги
    collector.add_new_book(book_name)
    
    # Проверяем что книга осталась одна
    assert book_name in collector.get_books_genre()
    assert len(collector.get_books_genre()) == 1
    ])
    def test_add_new_book(self, book_name, expected):
        collector = BooksCollector()
        collector.add_new_book(book_name)
        
        if expected:
            assert book_name in collector.books_genre
            assert collector.books_genre[book_name] == ''
        else:
            assert book_name not in collector.books_genre

    # Тест 3: Нельзя добавить одну книгу дважды
    def test_add_new_book_twice(self):
        collector = BooksCollector()
        book_name = 'Мастер и Маргарита'
        
        collector.add_new_book(book_name)
        collector.add_new_book(book_name)  # повторная попытка
        
        assert len(collector.books_genre) == 1
        assert list(collector.books_genre.keys()) == [book_name]

    # Тест 4: Установка жанра для книги
    def test_set_book_genre_valid(self):
        collector = BooksCollector()
        collector.add_new_book('1984')
        collector.set_book_genre('1984', 'Фантастика')
        
        assert collector.get_book_genre('1984') == 'Фантастика'

    # Тест 5: Нельзя установить несуществующий жанр
    def test_set_book_genre_invalid_genre(self):
        collector = BooksCollector()
        collector.add_new_book('Книга')
        collector.set_book_genre('Книга', 'Несуществующий жанр')
        
        assert collector.get_book_genre('Книга') == ''

    # Тест 6: Получение жанра книги
    def test_get_book_genre(self):
        collector = BooksCollector()
        collector.add_new_book('Преступление и наказание')
        collector.set_book_genre('Преступление и наказание', 'Детективы')
        
        assert collector.get_book_genre('Преступление и наказание') == 'Детективы'
        assert collector.get_book_genre('Несуществующая книга') is None

    # Тест 7: Получение книг с определенным жанром
    def test_get_books_with_specific_genre(self):
        collector = BooksCollector()
        
        # Добавляем книги разных жанров
        books = [
            ('Солярис', 'Фантастика'),
            ('Оно', 'Ужасы'),
            ('Шерлок Холмс', 'Детективы'),
            ('Зеленая миля', 'Фантастика')
        ]
        
        for name, genre in books:
            collector.add_new_book(name)
            collector.set_book_genre(name, genre)
        
        fantasy_books = collector.get_books_with_specific_genre('Фантастика')
        assert len(fantasy_books) == 2
        assert 'Солярис' in fantasy_books
        assert 'Зеленая миля' in fantasy_books

    # Тест 8: Получение всех книг
    def test_get_books_genre(self):
        collector = BooksCollector()
        collector.add_new_book('Книга 1')
        collector.add_new_book('Книга 2')
        
        books = collector.get_books_genre()
        assert isinstance(books, dict)
        assert len(books) == 2

    # Тест 9: Получение книг для детей
    def test_get_books_for_children(self):
        collector = BooksCollector()
        
        # Книги с разными жанрами
        children_books = [
            ('Гарри Поттер', 'Фантастика'),
            ('Ну погоди!', 'Мультфильмы'),
            ('Маска', 'Комедии')
        ]
        
        adult_books = [
            ('Сияние', 'Ужасы'),
            ('Десять негритят', 'Детективы')
        ]
        
        # Добавляем все книги
       def test_get_books_for_children_includes_children_books(self):
    """Детские книги включаются в результат"""
    collector = BooksCollector()
    
    # Только детские книги
    children_books = [
        ('Мультфильм 1', 'Мультфильмы'),
        ('Фантастика 1', 'Фантастика'),
        ('Комедия 1', 'Комедии'),
    ]
    
    for name, genre in children_books:
        collector.add_new_book(name)
        collector.set_book_genre(name, genre)
    
    result = collector.get_books_for_children()
    
    # Проверяем что все детские книги в результате
    assert len(result) == 3
    for name, _ in children_books:
        assert name in result


# Тест 2: Проверка что взрослые книги НЕ возвращаются  
def test_get_books_for_children_excludes_adult_books(self):
    """Взрослые книги не включаются в результат"""
    collector = BooksCollector()
    
    # Только взрослые книги
    adult_books = [
        ('Ужасы 1', 'Ужасы'),
        ('Детектив 1', 'Детективы'),
    ]
    
    for name, genre in adult_books:
        collector.add_new_book(name)
        collector.set_book_genre(name, genre)
    
    result = collector.get_books_for_children()
    
    # Проверяем что результат пуст
    assert len(result) == 0
    for name, _ in adult_books:
        assert name not in result


# Тест 3: Проверка смешанного списка
def test_get_books_for_children_mixed_books(self):
    """При смешанном списке возвращаются только детские книги"""
    collector = BooksCollector()
    
    children_books = [('Мультфильм', 'Мультфильмы')]
    adult_books = [('Ужасы', 'Ужасы')]
    
    # Добавляем все книги
    all_books = children_books + adult_books
    for name, genre in all_books:
        collector.add_new_book(name)
        collector.set_book_genre(name, genre)
    
    result = collector.get_books_for_children()
    
    # Проверяем что только детская книга в результате
    assert len(result) == 1
    assert children_books[0][0] in result
    assert adult_books[0][0] not in result


# Тест 4: Проверка пустого результата
def test_get_books_for_children_empty(self):
    """Если нет подходящих книг, возвращается пустой список"""
    collector = BooksCollector()
    
    # Не добавляем книги вообще
    result = collector.get_books_for_children()
    
    assert isinstance(result, list)
    assert len(result) == 0

    # Тест 10: Параметризованный тест для добавления в избранное
    def test_add_book_in_favorites_success(self):
    """Книга из словаря успешно добавляется в избранное"""
    collector = BooksCollector()
    book_name = 'Избранная книга'
    
    # 1. Добавляем книгу в словарь
    collector.add_new_book(book_name)
    
    # 2. Добавляем в избранное
    collector.add_book_in_favorites(book_name)
    
    # 3. Проверяем через метод (не через атрибут!)
    favorites = collector.get_list_of_favorites_books()
    assert book_name in favorites
    assert len(favorites) == 1


# Тест 2: Попытка добавить несуществующую книгу в избранное
def test_add_book_in_favorites_failure(self):
    """Несуществующая книга не добавляется в избранное"""
    collector = BooksCollector()
    book_name = 'Несуществующая книга'
    
    # Книгу НЕ добавляем в словарь
    
    # Пытаемся добавить в избранное
    collector.add_book_in_favorites(book_name)
    
    # Проверяем что избранное осталось пустым
    favorites = collector.get_list_of_favorites_books()
    assert book_name not in favorites
    assert len(favorites) == 0


# Тест 3: Нельзя добавить одну книгу в избранное дважды
def test_add_book_in_favorites_duplicate(self):
    """Книгу нельзя добавить в избранное дважды"""
    collector = BooksCollector()
    book_name = 'Дубликат в избранном'
    
    # Добавляем книгу в словарь
    collector.add_new_book(book_name)
    
    # Первое добавление в избранное
    collector.add_book_in_favorites(book_name)
    favorites = collector.get_list_of_favorites_books()
    assert book_name in favorites
    assert len(favorites) == 1
    
    # Второе добавление в избранное
    collector.add_book_in_favorites(book_name)
    
    # Проверяем что книга не добавилась второй раз
    favorites = collector.get_list_of_favorites_books()
    assert book_name in favorites
    assert len(favorites) == 1

    # Тест 11: Нельзя добавить книгу в избранное дважды
    def test_add_book_in_favorites_twice(self):
        collector = BooksCollector()
        book_name = 'Двойное избранное'
        
        collector.add_new_book(book_name)
        collector.add_book_in_favorites(book_name)
        collector.add_book_in_favorites(book_name)  # повторная попытка
        
        assert len(collector.favorites) == 1
        assert collector.favorites == [book_name]

    # Тест 12: Удаление книги из избранного
    def test_delete_book_from_favorites_success(self):
    """Книга успешно удаляется из избранного"""
    collector = BooksCollector()
    book_name = 'Удаляемая книга'
    
    # Подготовка: добавляем книгу в избранное
    collector.add_new_book(book_name)
    collector.add_book_in_favorites(book_name)
    
    # Действие: удаляем книгу из избранного
    collector.delete_book_from_favorites(book_name)
    
    # Проверка: книги нет в избранном
    favorites = collector.get_list_of_favorites_books()
    assert book_name not in favorites


# Тест 2: Удаление несуществующей книги из избранного
def test_delete_nonexistent_book_from_favorites(self):
    """Попытка удалить несуществующую книгу не вызывает ошибок"""
    collector = BooksCollector()
    book_name = 'Несуществующая книга'
    
    # Книгу НЕ добавляем в избранное
    
    # Действие: пытаемся удалить несуществующую книгу
    # (не должно вызывать ошибку)
    collector.delete_book_from_favorites(book_name)
    
    # Проверка: избранное осталось пустым
    favorites = collector.get_list_of_favorites_books()
    assert len(favorites) == 0


# Тест 3: Избранное пусто после удаления
def test_favorites_empty_after_deletion(self):
    """После удаления книги из избранное становится пустым"""
    collector = BooksCollector()
    book_name = 'Единственная книга'
    
    # Подготовка: добавляем одну книгу в избранное
    collector.add_new_book(book_name)
    collector.add_book_in_favorites(book_name)
    
    # Проверяем что книга добавилась (отдельный тест!)
    # Но в этом тесте мы проверяем только удаление, 
    # поэтому не проверяем добавление
    
    # Действие: удаляем книгу
    collector.delete_book_from_favorites(book_name)
    
    # Проверка: избранное пустое
    favorites = collector.get_list_of_favorites_books()
    assert len(favorites) == 0
    assert favorites == []


# Тест 4: Проверка что удаляется только нужная книга
def test_delete_specific_book_from_favorites(self):
    """Удаляется только указанная книга, другие остаются"""
    collector = BooksCollector()
    book_to_delete = 'Удаляемая'
    book_to_keep = 'Оставляемая'
    
    # Подготовка: добавляем две книги в избранное
    collector.add_new_book(book_to_delete)
    collector.add_new_book(book_to_keep)
    collector.add_book_in_favorites(book_to_delete)
    collector.add_book_in_favorites(book_to_keep)
    
    # Действие: удаляем только одну книгу
    collector.delete_book_from_favorites(book_to_delete)
    
    # Проверка: одна книга удалена, вторая осталась
    favorites = collector.get_list_of_favorites_books()
    assert book_to_delete not in favorites
    assert book_to_keep in favorites
    assert len(favorites) == 1

    # Тест 13: Удаление несуществующей книги из избранногоо
    def test_delete_nonexistent_book_from_favorites(self):
        collector = BooksCollector()
        
        # Попытка удалить несуществующую книгу не должна вызывать ошибку
        collector.delete_book_from_favorites('Несуществующая книга')
        assert collector.favorites == []

    # Тест 14: Получение списка избранных книг
    def test_get_list_of_favorites_books(self):
        collector = BooksCollector()
        
        # Добавляем несколько книг в избранное
        books = ['Книга 1', 'Книга 2', 'Книга 3']
        for book in books:
            collector.add_new_book(book)
            collector.add_book_in_favorites(book)
        
        favorites = collector.get_list_of_favorites_books()
        
        assert isinstance(favorites, list)
        assert len(favorites) == 3
        assert favorites == books

    # Тест 15: Комплексный тест - несколько операций
    def test_set_and_get_book_genre(self):
    """Устанавливаем и получаем жанр книги"""
    collector = BooksCollector()
    collector.add_new_book('Властелин колец')
    
    # Устанавливаем жанр
    collector.set_book_genre('Властелин колец', 'Фантастика')
    
    # Получаем жанр
    genre = collector.get_book_genre('Властелин колец')
    assert genre == 'Фантастика'


# Тест 2: Тестируем get_books_for_children
def test_get_books_for_children_returns_correct_count(self):
    """get_books_for_children возвращает правильное количество детских книг"""
    collector = BooksCollector()
    
    # Добавляем детские книги
    collector.add_new_book('Фантастика')
    collector.add_new_book('Мультфильм')
    collector.set_book_genre('Фантастика', 'Фантастика')
    collector.set_book_genre('Мультфильм', 'Мультфильмы')
    
    # Добавляем взрослую книгу (не должна войти в результат)
    collector.add_new_book('Ужасы')
    collector.set_book_genre('Ужасы', 'Ужасы')
    
    # Проверяем метод get_books_for_children
    children_books = collector.get_books_for_children()
    assert len(children_books) == 2


# Тест 3: Тестируем get_list_of_favorites_books
def test_get_list_of_favorites_books_returns_correct_count(self):
    """get_list_of_favorites_books возвращает правильное количество избранных книг"""
    collector = BooksCollector()
    
    # Добавляем книги в избранное
    collector.add_new_book('Книга 1')
    collector.add_new_book('Книга 2')
    collector.add_book_in_favorites('Книга 1')
    collector.add_book_in_favorites('Книга 2')
    
    # Проверяем метод get_list_of_favorites_books
    favorites = collector.get_list_of_favorites_books()
    assert len(favorites) == 2


# Тест 4: Тестируем delete_book_from_favorites
def test_delete_book_from_favorites_removes_specific_book(self):
    """delete_book_from_favorites удаляет конкретную книгу из избранного"""
    collector = BooksCollector()
    
    # Добавляем две книги в избранное
    collector.add_new_book('Книга 1')
    collector.add_new_book('Книга 2')
    collector.add_book_in_favorites('Книга 1')
    collector.add_book_in_favorites('Книга 2')
    
    # Удаляем одну книгу
    collector.delete_book_from_favorites('Книга 1')
    
    # Проверяем метод get_list_of_favorites_books
    favorites = collector.get_list_of_favorites_books()
    assert favorites == ['Книга 2']


# Тест 5: Тестируем взаимодействие методов (но все еще один основной метод)
def test_books_genre_updated_after_setting_genre(self):
    """Словарь books_genre обновляется после установки жанра"""
    collector = BooksCollector()
    collector.add_new_book('Книга')
    
    # Проверяем начальное состояние
    books = collector.get_books_genre()
    assert books['Книга'] == ''
    
    # Устанавливаем жанр
    collector.set_book_genre('Книга', 'Фантастика')
    
    # Проверяем обновленное состояние
    books = collector.get_books_genre()
    assert books['Книга'] == 'Фантастика'
