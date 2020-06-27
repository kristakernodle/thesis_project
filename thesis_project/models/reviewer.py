from database.cursors import Cursor, TestingCursor


def list_all_scored_dirs(cursor):
    cursor.execute("SELECT scored_dir FROM reviewers;")
    return list(item for tup in cursor.fetchall() for item in tup)


class Reviewer:
    def __init__(self, first_name, last_name, toScore_dir, scored_dir, reviewer_id=None):
        self.first_name = first_name
        self.last_name = last_name
        self.toScore_dir = toScore_dir
        self.scored_dir = scored_dir
        self.reviewer_id = reviewer_id

    def __str__(self):
        return f"< Reviewer {self.first_name} {self.last_name} >"

    def __repr__(self):
        return f"< Reviewer {self.first_name} {self.last_name} >"

    def __eq__(self, compare_to):
        if not isinstance(compare_to, Reviewer):
            return NotImplemented
        return self.reviewer_id == compare_to.reviewer_id

    @classmethod
    def __from_db(cls, cursor, scored_dir):
        cursor.execute("SELECT * FROM reviewers WHERE scored_dir = %s;", (scored_dir,))
        reviewer_data = cursor.fetchone()
        if reviewer_data is None:
            print(f"No reviewer in the database with scored directory {scored_dir}")
            return None
        return cls(first_name=reviewer_data[1], last_name=reviewer_data[2], toScore_dir=reviewer_data[3],
                   scored_dir=reviewer_data[4], reviewer_id=reviewer_data[0])

    @classmethod
    def from_db(cls, scored_dir, testing=False, postgresql=None):
        if testing:
            with TestingCursor(postgresql) as cursor:
                return cls.__from_db(cursor, scored_dir)
        else:
            with Cursor() as cursor:
                return cls.__from_db(cursor, scored_dir)

    def __save_to_db(self, cursor):
        cursor.execute("INSERT INTO reviewers (first_name, last_name, toScore_dir, scored_dir) "
                       "VALUES (%s, %s, %s, %s);", (self.first_name, self.last_name, self.toScore_dir, self.scored_dir))

    def save_to_db(self, testing=False, postgresql=None):

        def save_to_db_main(scored_dir, a_cursor):
            if scored_dir not in list_all_scored_dirs(a_cursor):
                self.__save_to_db(a_cursor)
            return self.__from_db(a_cursor, scored_dir)

        if testing:
            with TestingCursor(postgresql) as cursor:
                return save_to_db_main(self.scored_dir, cursor)
        else:
            with Cursor() as cursor:
                return save_to_db_main(self.scored_dir, cursor)

    def __delete_from_db(self, cursor):
        cursor.execute("DELETE FROM reviewers WHERE reviewer_id = %s", (self.reviewer_id,))

    def delete_from_db(self, testing=False, postgresql=None):
        if testing:
            with TestingCursor(postgresql) as cursor:
                self.__delete_from_db(cursor)
        else:
            with Cursor() as cursor:
                self.__delete_from_db(cursor)
