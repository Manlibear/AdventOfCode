class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

def log_test(test):
    if test:
        print(bcolors.OKGREEN + bcolors.BOLD +  "[\u2713] Test Passed" + bcolors.ENDC)
    else:
        print(bcolors.FAIL + bcolors.BOLD + "[X] Test Failed" + bcolors.ENDC)


def log_answer(label, value, test_value, debug_mode):
    print(f"{label} {str(value)}")
    if debug_mode:
        log_test(value == test_value)