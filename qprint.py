# qprint = quick print :O
import sys

BLACK, RED, GREEN, YELLOW, BLUE, MAGENTA, CYAN, WHITE = [str(x) for x in range(30, 38)]  # terminal colors
# RED for errors
# YELLOW for warnings
# GREEN for successful executions
# BLUE for notifications
# to be completed when needed
AVAILABLE_COLORS = [BLACK, MAGENTA, CYAN, WHITE]
BOLD = ';1'  # use COLOR + BOLD to get bold text, in this order


def qprint(data, end='\n', color=WHITE):  # writes to stderr for immediate output
    sys.stderr.write('\x1b[%sm' % color + str(data) + '\x1b[0m' + end)
