import sys
from PyQt5.QtWidgets import QApplication
from ui.login import LoginWindow
from ui.registration_logic import RegistrationWindow
from prj_utils.db_session import session as Session
from prj_utils.models import User

if __name__ == '__main__':
    app = QApplication(sys.argv)
    sess = Session()
    user_count = sess.query(User).count()

    if user_count > 0:
        login = LoginWindow()
    else:
        registration = RegistrationWindow()

    sys.exit(app.exec_())
