from data.helper import run_game, setup
import data.elements as program


def main():
    setup()
    run_game()
    program.quit(program.SETTINGS, program.HIGH_SCORES)


if __name__ == '__main__':
    main()