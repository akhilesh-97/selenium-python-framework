import logging
import os


class LogGenerator:

    @staticmethod
    def log():

        log_dir = "logs"

        os.makedirs(log_dir, exist_ok=True)

        logging.basicConfig(
            filename=os.path.join(log_dir, "automation.log"),
            format="%(asctime)s : %(levelname)s : %(message)s",
            level=logging.INFO,
            force=True
        )

        return logging.getLogger()