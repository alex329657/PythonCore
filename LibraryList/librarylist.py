from asciimatics.widgets import Frame, ListBox, Layout, Divider, Text, \
    Button, TextBox, Widget
from asciimatics.scene import Scene
from asciimatics.screen import Screen
from asciimatics.exceptions import ResizeScreenError, NextScene, StopApplication
import sys
import os
import sqlite3


# noinspection SqlResolve
class Book(object):
    def __init__(self):

        # Create /db folder if not exist.
        if not os.path.exists('db'):
            os.makedirs('db')

        # Create a database in /db folder
        self._db = sqlite3.connect("./db/library.db")
        self._db.row_factory = sqlite3.Row

        # Create table if not exist.
        self._db.cursor().execute('''
            CREATE TABLE IF NOT EXISTS books(
                id INTEGER PRIMARY KEY,
                title TEXT,
                author TEXT,
                genre TEXT,
                year TEXT,
                publisher TEXT)
        ''')
        self._db.commit()

        # Current book id.
        self.current_id = None

    def add(self, book):
        self._db.cursor().execute('''
            INSERT INTO books(title, author, genre, year, publisher)
            VALUES(:title, :author, :genre, :year, :publisher)''',
                                  book)
        self._db.commit()

    def get_summary(self):
        return self._db.cursor().execute(
            "SELECT title, id from books").fetchall()

    def get_book(self, book_id):
        return self._db.cursor().execute(
            "SELECT * from books WHERE id=:id", {"id": book_id}).fetchone()

    def get_current_book(self):
        if self.current_id is None:
            return {"title": "", "author": "", "genre": "", "year": "", "publisher": ""}
        else:
            return self.get_book(self.current_id)

    def update_current_book(self, details):
        if self.current_id is None:
            self.add(details)
        else:
            self._db.cursor().execute('''
                UPDATE books SET title=:title, author=:author, genre=:genre,
                year=:year, publisher=:publisher WHERE id=:id''', details
                                      )
            self._db.commit()

    def delete_book(self, book_id):
        self._db.cursor().execute('''
            DELETE FROM books WHERE id=:id''', {"id": book_id})
        self._db.commit()


class ListView(Frame):
    def __init__(self, screen, model):
        super(ListView, self).__init__(screen,
                                       screen.height,
                                       screen.width,
                                       on_load=self._reload_list,
                                       hover_focus=True,
                                       can_scroll=False,
                                       title="Books List")
        # Save off the model that accesses the books database.
        self._model = model

        # Create the form for displaying the list of books.
        self._list_view = ListBox(
            Widget.FILL_FRAME,
            model.get_summary(),
            name="books",
            add_scroll_bar=True,
            on_change=self._on_pick,
            on_select=self._edit)
        self._edit_button = Button("Edit", self._edit)
        self._delete_button = Button("Delete", self._delete)
        layout = Layout([100], fill_frame=True)
        self.add_layout(layout)
        layout.add_widget(self._list_view)
        layout.add_widget(Divider())
        layout2 = Layout([1, 1, 1, 1])
        self.add_layout(layout2)
        layout2.add_widget(Button("Add", self._add), 0)
        layout2.add_widget(self._edit_button, 1)
        layout2.add_widget(self._delete_button, 2)
        layout2.add_widget(Button("Quit", self._quit), 3)
        self.fix()
        self._on_pick()

    def _on_pick(self):
        self._edit_button.disabled = self._list_view.value is None
        self._delete_button.disabled = self._list_view.value is None

    def _reload_list(self, new_value=None):
        self._list_view.options = self._model.get_summary()
        self._list_view.value = new_value

    def _add(self):
        self._model.current_id = None
        raise NextScene("Edit Book")

    def _edit(self):
        self.save()
        self._model.current_id = self.data["books"]
        raise NextScene("Edit Book")

    def _delete(self):
        self.save()
        self._model.delete_book(self.data["books"])
        self._reload_list()

    @staticmethod
    def _quit():
        raise StopApplication("User pressed quit")


class BookView(Frame):
    def __init__(self, screen, model):
        super(BookView, self).__init__(screen,
                                       screen.height * 2 // 3,
                                       screen.width * 2 // 3,
                                       hover_focus=True,
                                       can_scroll=False,
                                       title="Book Details",
                                       reduce_cpu=True)
        # Save off the model that accesses the books database.
        self._model = model

        # Create the form for displaying the list of books.
        layout = Layout([100], fill_frame=True)
        self.add_layout(layout)
        layout.add_widget(Text("Title    :", "title"))
        layout.add_widget(Text("Author   :", "author"))
        layout.add_widget(Text("Genre    :", "genre"))
        layout.add_widget(Text("Year     :", "year"))
        layout.add_widget(Text("Publisher:", "publisher"))
        layout2 = Layout([1, 1, 1, 1])
        self.add_layout(layout2)
        layout2.add_widget(Button("OK", self._ok), 0)
        layout2.add_widget(Button("Cancel", self._cancel), 3)
        self.fix()

    def reset(self):
        # Do standard reset to clear out form, then populate with new data.
        super(BookView, self).reset()
        self.data = self._model.get_current_book()

    def _ok(self):
        self.save()
        self._model.update_current_book(self.data)
        raise NextScene("Main")

    @staticmethod
    def _cancel():
        raise NextScene("Main")


def demo(screen, scene):
    scenes = [
        Scene([ListView(screen, books)], -1, name="Main"),
        Scene([BookView(screen, books)], -1, name="Edit Book")
    ]

    screen.play(scenes, stop_on_resize=True, start_scene=scene, allow_int=True)


books = Book()
last_scene = None
while True:
    try:
        Screen.wrapper(demo, catch_interrupt=True, arguments=[last_scene])
        sys.exit(0)
    except ResizeScreenError as e:
        last_scene = e.scene
