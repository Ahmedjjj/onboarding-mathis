import datajoint as dj

schema = dj.schema('tutorial', locals())


@schema
class Mouse(dj.Manual):
    definition = """
      mouse_id: int                  # unique mouse id
      ---
      dob: date                      # mouse date of birth
      sex: enum('M', 'F', 'U')    # sex of mouse - Male, Female, or Unknown/Unclassified
      """


@schema
class Session(dj.Manual):
    definition = """
    # experiment session
    -> Mouse
    session_date: date            # session date
    ---
    experiment_setup: int         # experiment setup ID
    experimenter: varchar(128)    # name of the experimenter
    """
