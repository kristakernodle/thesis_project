from database import Cursor
import utilities as util


class Experiments:
    def __init__(self, experiment_name, experiment_dir, experiment_id=None):
        self.experiment_name = util.prep_string_for_db(experiment_name)
        self.experiment_dir = experiment_dir
        self.experiment_id = experiment_id

    def __str__(self):
        return f"< Experiment {self.experiment_name} >"

    @classmethod
    def from_db(cls, experiment_name):
        experiment_name = util.prep_string_for_db(experiment_name)
        with Cursor() as cursor:
            cursor.execute("SELECT * FROM experiments WHERE experiment_name = %s;", (experiment_name,))
            exp = cursor.fetchone()
            return cls(experiment_name=exp[2], experiment_dir=exp[1], experiment_id=exp[0])

    def save_to_db(self):
        experiment_name = util.prep_string_for_db(self.experiment_name)
        with Cursor() as cursor:
            cursor.execute("INSERT INTO experiments(experiment_dir, experiment_name) VALUES(%s, %s);",
                           (self.experiment_dir, experiment_name))
        return self.from_db(experiment_name)

    def delete_from_db(self):
        with Cursor() as cursor:
            cursor.execute("DELETE FROM experiments WHERE experiment_id = %s", (self.experiment_id,))

    @classmethod
    def list_participants(cls, experiment_name=None):
        if experiment_name is not None:
            # Return all mice in THIS experiment, without duplicats, as a list

        else:
            # Return all mice in experiments, without duplicates, as a list
        return []
            



