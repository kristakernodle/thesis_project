# MOUSE TABLE
def seed_mouse_table(a_cursor, eartag, birthdate, genotype, sex):
    a_cursor.execute("INSERT INTO mouse (eartag, birthdate, genotype, sex) "
                     "VALUES (%s, %s, %s, %s);", (eartag, birthdate, genotype, sex))


# EXPERIMENTS TABLE
def seed_experiments_table(a_cursor, prepped_exp_one, prepped_exp_two):
    a_cursor.execute("INSERT INTO experiments (experiment_name, experiment_dir) VALUES (%s, %s);", prepped_exp_one)
    a_cursor.execute("INSERT INTO experiments (experiment_name, experiment_dir) VALUES (%s, %s);", prepped_exp_two)


# PARTICIPANT DETAILS TABLE
def seed_participant_details(a_cursor, mouse_id, experiment_id, start_date, end_date):
    a_cursor.execute("INSERT INTO participant_details (mouse_id, experiment_id, start_date, end_date) "
                     "VALUES (%s, %s, %s, %s);", (mouse_id, experiment_id, start_date, end_date))


# REVIEWERS TABLE
def seed_reviewers_table(cursor, first_name, last_name, toScore_dir, scored_dir):
    cursor.execute("INSERT INTO reviewers (first_name, last_name, toScore_dir, scored_dir) "
                   "VALUES (%s, %s, %s, %s);", (first_name, last_name, toScore_dir, scored_dir))


# SESSIONS TABLE
def seed_sessions_table(cursor, mouse_id, experiment_id, session_date, session_dir):
    cursor.execute("INSERT INTO sessions (mouse_id, experiment_id, session_date, session_dir) "
                   "VALUES (%s, %s, %s, %s);", (mouse_id, experiment_id, session_date, session_dir))


# FOLDERS TABLE
def seed_folders_table(cursor, session_id, folder_dir):
    cursor.execute("INSERT INTO folders (session_id, folder_dir) "
                   "VALUES (%s, %s);", (session_id, folder_dir))


# BLIND FOLDERS TABLE
def seed_blind_folders_table(cursor, folder_id, reviewer_id, blind_name):
    cursor.execute("INSERT INTO blind_folders (folder_id, reviewer_id, blind_name) "
                   "VALUES (%s, %s, %s);", (folder_id, reviewer_id, blind_name))


# TRIALS TABLE
def seed_trials_table(cursor, experiment_id, folder_id, trial_dir, trial_date):
    cursor.execute("INSERT INTO trials (experiment_id, folder_id, trial_dir, trial_date) "
                   "VALUES (%s, %s, %s, %s);", (experiment_id, folder_id, trial_dir, trial_date))


# BLIND TRIALS TABLE
def seed_blind_trials_table(cursor, trial_id, folder_id, full_path):
    cursor.execute("INSERT INTO blind_trials (trial_id, folder_id, full_path) "
                   "VALUES (%s, %s, %s);", (trial_id, folder_id, full_path))
