import platform

class Nice:
    def __init__(self, niceness = 10, ignore_failure = False):
        if niceness > 20:
            niceness = 20
        elif niceness < -20:
            niceness = -20
        self.niceness = niceness
        self.ignore_failure = ignore_failure

    def get_command(self):
        # TODO: Get a more comprehensive list of platforms where nice command is available
        if platform.system() in ("Linux", "Darwin"):
            return "nice -n {}".format(self.niceness)

        if not self.ignore_failure:
            raise Exception("'nice' is not available on {}. Please raise a defect on github if you think it's available for your platform.".format(platform.system()))

        return ""
