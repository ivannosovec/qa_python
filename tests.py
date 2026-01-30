import pytest


class TestBooksCollector:

    # Тест 1: Проверка инициализации коллектора
    def test_init_books_collector(self):
        collector = BooksCollector()
        assert collector.books_genre == {}
        assert collector.favorites == []
        assert collector.genre == ['Фантастика', 'Ужасы', 'Детективы', 'Мультфильмы', 'Комедии']
        assert collector.genre_age_rating == ['Ужасы', 'Детективы']

    # Тест 2: Параметризованный тест для добавления новой книги
    @pytest.mark.parametrize('book_name, expected', [
        ('Война и мир', True),           # валидное название
        ('A' * 40, True),                # граничное значение (40 символов)
        ('Книга', True),                 # обычное название
        ('', False),                     # пустая строка
        ('A' * 41, False),               # слишком длинное название (41 символ)
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
        for name, genre in children_books + adult_books:
            collector.add_new_book(name)
            collector.set_book_genre(name, genre)
        
        children_only = collector.get_books_for_children()
        
        # Проверяем, что только детские книги
        assert len(children_only) == 3
        for name, _ in children_books:
            assert name in children_only
        
        for name, _ in adult_books:
            assert name not in children_only

    # Тест 10: Параметризованный тест для добавления в избранное
    @pytest.mark.parametrize('book_in_dict, expected_in_favorites', [
        (True, True),    # книга в словаре → добавляется в избранное
        (False, False),  # книги нет в словаре → не добавляется
    ])
    def test_add_book_in_favorites(self, book_in_dict, expected_in_favorites):
        collector = BooksCollector()
        book_name = 'Избранная книга'
        
        if book_in_dict:
            collector.add_new_book(book_name)
        
        collector.add_book_in_favorites(book_name)
        
        if expected_in_favorites:
            assert book_name in collector.favorites
        else:
            assert book_name not in collector.favorites

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
    def test_delete_book_from_favorites(self):
        collector = BooksCollector()
        book_name = 'Удаляемая книга'
        
        collector.add_new_book(book_name)
        collector.add_book_in_favorites(book_name)
        
        # Проверяем, что книга добавилась
        assert book_name in collector.favorites
        
        # Удаляем
        collector.delete_book_from_favorites(book_name)
        assert book_name not in collector.favorites
        assert collector.favorites == []

    # Тест 13: Удаление несуществующей книги из избранного
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
    def test_complex_scenario(self):
        collector = BooksCollector()
        
        # Добавляем книги
        collector.add_new_book('Властелин колец')
        collector.add_new_book('Оно')
        collector.add_new_book('Том и Джерри')
        
        # Устанавливаем жанры
        collector.set_book_genre('Властелин колец', 'Фантастика')
        collector.set_book_genre('Оно', 'Ужасы')
        collector.set_book_genre('Том и Джерри', 'Мультфильмы')
        
        # Добавляем в избранное
        collector.add_book_in_favorites('Властелин колец')
        collector.add_book_in_favorites('Том и Джерри')
        
        # Проверяем
        assert collector.get_book_genre('Властелин колец') == 'Фантастика'
        assert len(collector.get_books_for_children()) == 2  # Фантастика и Мультфильмы
        assert len(collector.get_list_of_favorites_books()) == 2
        
        # Удаляем из избранного
        collector.delete_book_from_favorites('Том и Джерри')
        assert collector.get_list_of_favorites_books() == ['Властелин колец']
