from main import BooksCollector
class TestBooksCollector:
    def test_set_book_genre_name_and_genre_show_book_genre(self):
        collector = BooksCollector()
        collector.add_new_book('Граф Монте-Кристо')
        collector.set_book_genre('Граф Монте-Кристо', 'Детективы')
        assert collector.get_book_genre('Граф Монте-Кристо') == 'Детективы'

    def test_set_book_genre_book_without_genre_has_no_genre(self):
        collector = BooksCollector()
        collector.add_new_book('Маша и Медведь')
        assert collector.get_book_genre('Маша и Медведь') != 'Детективы'

    def test_books_with_specific_genre_add_genre_comparison_genre(self):
        collector = BooksCollector()
        collector.add_new_book('Шантарам')
        collector.set_book_genre('Шантарам', 'Детективы')
        assert collector.get_books_with_specific_genre('Детективы') == ['Шантарам']

    def test_get_books_genre_add_book_genre_check_existent_book(self):
        collector = BooksCollector()
        collector.add_new_book('Кора')
        collector.set_book_genre('Кора', 'Ужасы')
        assert collector.get_books_genre() == {'Кора': 'Ужасы'}

    def test_get_books_for_children_different_genres_show_for_children(self):
        collector = BooksCollector()
        collector.add_new_book('Винни Пух')
        collector.set_book_genre('Винни Пух', 'Мультфильмы')
        collector.add_new_book('Кора')
        collector.set_book_genre('Кора', 'Ужасы')
        assert collector.get_books_for_children() == ['Винни Пух']

    def test_add_book_in_favorites_new_book_in_favorites_return_favorite_book(self):
        collector = BooksCollector()
        collector.add_new_book('Евгений Онегин')
        collector.add_book_in_favorites('Евгений Онегин')
        assert collector.get_list_of_favorites_books() == ['Евгений Онегин']

    def test_delete_book_from_favorites_add_favorite_book_return_list(self):
        collector = BooksCollector()
        collector.add_new_book('Тихий Дон')
        collector.add_book_in_favorites('Тихий Дон')
        collector.delete_book_from_favorites('Тихий Дон')
        assert collector.get_list_of_favorites_books() != ['Тихий Дон']

    def test_get_list_of_favorites_books_add_favorite_book_return_book(self):
        collector = BooksCollector()
        collector.add_new_book('Унесенные ветром')
        collector.add_book_in_favorites('Унесенные ветром')
        assert collector.get_list_of_favorites_books() == ['Унесенные ветром']

    def test_delete_book_from_favorites_double_delete_not_existent_book(self):
        collector = BooksCollector()
        collector.add_new_book('Погоня')
        collector.add_book_in_favorites('Погоня')
        collector.delete_book_from_favorites('Погоня')
        collector.delete_book_from_favorites('Погоня')
        assert collector.get_list_of_favorites_books() == []


dsfg








